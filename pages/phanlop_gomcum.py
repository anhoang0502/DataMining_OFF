import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import joblib
import os

st.set_page_config(page_title="Bài toán Khai phá dữ liệu phân lớp - phân cụm", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .prediction-card {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        border-left: 5px solid #1d3557;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

MODELS_DIR = 'models'
NUTR_COLS = ['energy_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g', 'sugars_100g', 
             'fiber_100g', 'proteins_100g']

@st.cache_resource
def load_mining_assets():
    try:
        df = pd.read_csv("df_final (1).csv") 
        def p(name): return os.path.join(MODELS_DIR, name)
        
        scaler = joblib.load(p("nutri_scaler.pkl"))
        model_nutri = joblib.load(p("nutriscore_grade_model.pkl")) 
        model_healthy = joblib.load(p("healthy_model.pkl"))        
        model_kmeans = joblib.load(p("kmeans_model.pkl"))       
        
        return df, scaler, model_nutri, model_healthy, model_kmeans
    except Exception as e:
        st.error(f"Lỗi tải assets: {e}")
        return [None] * 5

df, scaler, model_nutri, model_healthy, model_kmeans = load_mining_assets()

if df is not None:
    st.title("Bài toán khai phá dữ liệu sản phâm thực phẩm")
    
    col_ctrl, col_chart = st.columns([1, 3])
    
    with col_ctrl:
        st.subheader("Cài đặt thuật toán")
        k_val = st.slider("Chọn số lượng cụm (k):", 2, 10, value=model_kmeans.n_clusters)
        btn_run_k = st.button("Chọn k")

    X_data = df[NUTR_COLS]
    
    if btn_run_k:
        current_km = KMeans(n_clusters=k_val, random_state=42, n_init=10)
        df['Cluster'] = current_km.fit_predict(X_data).astype(str)
    else:
        df['Cluster'] = model_kmeans.predict(X_data).astype(str)

    pca = PCA(n_components=2)
    pca_res = pca.fit_transform(X_data)
    df['PCA1'] = pca_res[:, 0]
    df['PCA2'] = pca_res[:, 1]

    with col_chart:
        fig_clusters = px.scatter(
            df, x='PCA1', y='PCA2', color='Cluster',
            title=f"Biểu đồ gom cụm loại sản phẩm thực phẩm  (k={k_val})",
            color_discrete_sequence=px.colors.sequential.GnBu_r,
            opacity=0.9, hover_data=['general_category']
        )
        fig_clusters.update_traces(marker=dict(line=dict(width=1, color='white'), size=8))
        fig_clusters.update_layout(
            xaxis_title="PCA Component 1",
            yaxis_title="PCA Component 2",
            legend_title_text='Cluster'
        )
        st.plotly_chart(fig_clusters, use_container_width=True)

    st.subheader("Đặc trưng các thành phần dinh dưỡng theo cụm")
    cluster_means = df.groupby('Cluster')[NUTR_COLS].mean()
    
    fig_heat = px.imshow(
        cluster_means,
        text_auto=".2f",
        color_continuous_scale="GnBu",
        labels=dict(x="Thành phần dinh dưỡng", y="Cụm", color="Giá trị mean"),
        aspect="auto"
    )
    st.plotly_chart(fig_heat, use_container_width=True)
    
    st.divider()
    st.title("Kiểm tra thông tin sản phẩm")
    
    st.write("Nhập các chỉ số dinh dưỡng của sản phẩm trên bao bì:")
    with st.form("input_product"):
        c1, c2, c3, c4 = st.columns(4)
        in_energy = c1.number_input("Energy_100g", value=0.0)
        in_fat = c2.number_input("Fat_100g", value=0.0)
        in_sfat = c3.number_input("Sat-Fat_100g", value=0.0)
        in_sugar = c4.number_input("Sugars_100g", value=0.0)
        
        c5, c6, c7, _ = st.columns(4)
        in_fiber = c5.number_input("Fiber_100g", value=0.0)
        in_prot = c6.number_input("Proteins_100g", value=0.0)
        in_carb = c7.number_input("Carbohydrates_100g", value=0.0)
        
        submit_predict = st.form_submit_button("PHÂN TÍCH")

    if submit_predict:
        raw_input = np.array([[in_energy, in_fat, in_sfat, in_sugar, in_fiber, in_prot, in_carb]])
        input_scaled = scaler.transform(raw_input)
        
        grade_pred = model_nutri.predict(input_scaled)[0]
        healthy_pred = model_healthy.predict(input_scaled)[0]
        
        cluster_pred = model_kmeans.predict(input_scaled)[0]
        
        st.subheader("Thông tin sản phẩm")
        res_c1, res_c2, res_c3 = st.columns(3)
        with res_c1:
            st.metric("Xếp hạng Nutriscore", f"Loại {grade_pred}")
        with res_c2:
            status = "Lành mạnh" if healthy_pred == 1 else "Không lành mạnh"
            st.metric("Đánh giá", status)
        with res_c3:
            st.metric("Phân loại cụm", f"Cụm {cluster_pred}")

        new_point_pca = pca.transform(input_scaled)
        
        fig_loc = go.Figure()
        
        for c in sorted(df['Cluster'].unique()):
            sub = df[df['Cluster'] == c]
            fig_loc.add_trace(go.Scatter(
                x=sub['PCA1'], y=sub['PCA2'],
                mode='markers', name=f"Cụm {c}",
                marker=dict(size=5, opacity=0.2)
            ))
            
        fig_loc.add_trace(go.Scatter(
            x=[new_point_pca[0, 0]], 
            y=[new_point_pca[0, 1]],
            mode='markers+text',
            name="Sản phẩm",
            text=["Sản phẩm"],
            textposition="top center",
            marker=dict(color='yellow', size=18, symbol='circle', line=dict(width=2, color='white'))
        ))
        
        fig_loc.update_layout(
            title="Vị trí sản phẩm trên biểu đồ gom cụm",
            height=600
        )
        st.plotly_chart(fig_loc, use_container_width=True)
        
else:
    st.error("Không tìm thấy dữ liệu để hiển thị.")