import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
import os

st.set_page_config(page_title="Food Knowledge Mining System", layout="wide")

st.sidebar.header('MENU')
st.sidebar.page_link('trang_chu.py', label='Trang chủ') 
st.sidebar.page_link('pages/phanlop_gomcum.py', label='Phân loại - Gom cụm') 

st.markdown("""
    <style>
    .stButton>button {
        background-color: #457b9d !important;
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
    }
    [data-testid="stMetricLabel"] {
        color: #1d3557 !important;
        font-weight: bold !important;
    }
    hr {
        margin-top: 1rem !important;
        margin-bottom: 1rem !important;
        border-color: #a8dadc !important;
    }
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

COOL_CONTINUOUS = "GnBu"
COOL_DISCRETE = ["#1d3557", "#457b9d", "#a8dadc", "#f1faee", "#1d3557"]

PLOT_CONFIG = {
    'scrollZoom': True,
    'displayModeBar': True,
    'modeBarButtonsToAdd': ['drawline', 'drawopenpath', 'eraseshape'],
    'showTips': False
}

def add_border(fig, chart_type="bar"):
    if chart_type in ["bar", "hist"]:
        fig.update_traces(marker_line_color='white', marker_line_width=1, opacity=0.8)
    elif chart_type in ["scatter", "strip"]:
        fig.update_traces(marker_line_color='white', marker_line_width=0.5, opacity=0.7)
    elif chart_type == "box":
        fig.update_traces(line=dict(width=1.5))
    elif chart_type == "heatmap":
        fig.update_traces(xgap=1, ygap=1)
    return fig

MODELS_DIR = 'models'

@st.cache_resource
def load_assets():
    try:
        df = pd.read_csv("df_final (1).csv")
        def p(file_name): return os.path.join(MODELS_DIR, file_name)
        scaler = joblib.load(p("nutri_scaler.pkl"))
        nutrigrade_model = joblib.load(p("nutriscore_grade_model.pkl"))
        healthy_model = joblib.load(p("healthy_model.pkl"))
        kmeans_model = joblib.load(p("kmeans_model.pkl"))
        nutrigrade_label = joblib.load(p("nutrigrade_label.pkl"))
        healthy_label = joblib.load(p("healthy_label.pkl"))
        return df, scaler, nutrigrade_model, healthy_model, kmeans_model, nutrigrade_label, healthy_label
    except Exception as e:
        st.error(f"Loi tai du lieu: {e}")
        return [None] * 7

assets = load_assets()
(df, scaler, nutrigrade_model, healthy_model, kmeans_model, nutrigrade_label, healthy_label) = assets

if df is not None:
    nutr_features = ['fat_100g', 'sugars_100g', 'proteins_100g', 'fiber_100g', 'saturated-fat_100g', 'carbohydrates_100g']
    cat_cols = ['general_category', 'countries_en', 'nutriscore_grade', 'nova_group']

    st.title("Hệ thống thông tin Thực phẩm")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Tổng sản phẩm", f"{len(df):,}", 'Trên thị trường Pháp và Hoa Kỳ')
    with m2:
        st.metric("Số nhóm thực phẩm phổ biến", f"{df['general_category'].nunique()}")
    with m3:
        top_cat = df['general_category'].value_counts().idxmax()
        top_count = df['general_category'].value_counts().max()
        st.metric("Nhóm thực phẩm phổ biến nhất", f"{top_cat}", f"{top_count} sản phẩm")
    with m4:
        health_pct = (df['nutriscore_grade'].isin(['a', 'b'])).mean() * 100
        st.metric("Tỷ lệ Lành mạnh", f"{health_pct:.1f}%", "Sản phẩm Nutriscore A và B")

    st.divider()

    with st.sidebar:
        st.subheader("Mục tiêu phân tích về dữ liệu thực phẩm")
        analysis_type = st.radio(
            "Lựa chọn mục tiêu bạn muốn xem xét",
            options=[
                "1. Phân tích chi tiết đơn biến",
                "2. Phân tích dinh dưỡng theo Phân loại sản phẩm",
                "3. Tỷ lệ sản phẩm theo Quốc gia",
                "4. Tỷ lệ Nutriscore theo Quốc gia",
                "5. Mối quan hệ NOVA và Nutri-Score",
                "6. Tương quan giữa các thành phần dinh dưỡng",
                "7. Hồ sơ dinh dưỡng của Pháp và Hoa Kỳ",
                "8. Tương quan năng lượng và thành phần dinh dưỡng",
                "9. Mức độ nhận diện từng loại sản phẩm theo Quốc gia"
            ]
        )

        params = {}
        if "1." in analysis_type:
            params['var'] = st.selectbox("Biến cần phần tích:", options=nutr_features + cat_cols)
        elif "2." in analysis_type:
            params['nutr'] = st.multiselect("Thành phần dinh dưỡng:", nutr_features, default=nutr_features[:1])
            params['cats'] = st.multiselect("Phân loại sản phẩm:", df['general_category'].unique(), default=df['general_category'].unique()[:3])
        elif "3." in analysis_type:
            params['countries'] = st.multiselect("Quốc gia:", ['France', 'United States'], default=['France', 'United States'])
        elif "4." in analysis_type:
            params['country'] = st.selectbox("Quốc gia:", ['France', 'United States'])
            params['cats'] = st.multiselect("Phân loại sản phẩm:", df['general_category'].unique(), default=df['general_category'].unique()[:5])
        elif "5." in analysis_type:
            params['country'] = st.multiselect("Lọc theo quốc gia:", ['France', 'United States'], default=['France', 'United States'])
            params['cats'] = st.multiselect("Lọc theo nhóm sản phẩm:", df['general_category'].unique(), default=df['general_category'].unique()[:5])
        elif "6." in analysis_type:
            params['nutr'] = st.multiselect("Thành phần dinh dưỡng:", nutr_features, default=nutr_features[:3])
        elif "7." in analysis_type:
            params['nutr'] = st.multiselect("Chọn các thành phần để vẽ Radar:", nutr_features, default=nutr_features)
        elif "8." in analysis_type:
            params['nutr_target'] = st.selectbox("Thành phần dinh dưỡng so sánh:", nutr_features)
            params['cats'] = st.multiselect("Phân loại sản phẩm:", df['general_category'].unique(), default=df['general_category'].unique()[:3])
        elif "9." in analysis_type:
            params['country'] = st.selectbox("Quốc gia khảo sát:", ['France', 'United States'])

        btn_analyze = st.button("PHÂN TÍCH", use_container_width=True)

    if btn_analyze:
        st.subheader(analysis_type)
        
        # 1. PHÂN TÍCH ĐƠN BIẾN
        if "1." in analysis_type:
            fig = px.histogram(df, x=params['var'], marginal="box", color_discrete_sequence=[COOL_DISCRETE[0]])
            st.plotly_chart(add_border(fig, "hist"), use_container_width=True, config=PLOT_CONFIG)

        # 2. DINH DƯỠNG THEO CATEGORY
        elif "2." in analysis_type:
            df_sub = df[df['general_category'].isin(params['cats'])]
            for nt in params['nutr']:
                c1, c2 = st.columns(2)
                with c1: 
                    fig = px.histogram(df_sub, x=nt, color="general_category", barmode="overlay", color_discrete_sequence=px.colors.sequential.GnBu_r)
                    st.plotly_chart(add_border(fig, "hist"), use_container_width=True)
                with c2: 
                    fig = px.box(df_sub, x="general_category", y=nt, color="general_category", color_discrete_sequence=px.colors.sequential.Blues_r)
                    st.plotly_chart(add_border(fig, "box"), use_container_width=True)
            
            if len(params['nutr']) >= 2:
                df_heat = df_sub.groupby('general_category')[params['nutr']].mean()
                fig = px.imshow(df_heat, text_auto=".2f", color_continuous_scale=COOL_CONTINUOUS)
                st.plotly_chart(add_border(fig, "heatmap"), use_container_width=True)

        # 3. TỶ LỆ THEO QUỐC GIA
        elif "3." in analysis_type:
            df_c = df[df['countries_en'].isin(params['countries'])]
            df_pct = df_c.groupby(['countries_en', 'general_category']).size().reset_index(name='count')
            df_pct['percent'] = df_pct.groupby('countries_en')['count'].transform(lambda x: (x/x.sum())*100)
            fig = px.bar(df_pct, x='general_category', y='percent', color='countries_en', barmode='group', color_discrete_sequence=['#1d3557', '#a8dadc'])
            st.plotly_chart(add_border(fig, "bar"), use_container_width=True)

        # 4. NUTRISCORE THEO QUỐC GIA
        elif "4." in analysis_type:
            df_ns = df[(df['countries_en'] == params['country']) & (df['general_category'].isin(params['cats']))]
            fig = px.histogram(df_ns, x="general_category", color="nutriscore_grade", barnorm='percent',
                               category_orders={"nutriscore_grade": ["a", "b", "c", "d", "e"]},
                               color_discrete_map={'a':'#2a9d8f', 'b':'#8ab17d', 'c':'#e9c46a', 'd':'#f4a261', 'e':'#e76f51'})
            st.plotly_chart(add_border(fig, "hist"), use_container_width=True)

        # 5. NOVA & NUTRISCORE
        elif "5." in analysis_type:
            fig = px.histogram(df, x="nova_group", color="nutriscore_grade", barnorm='percent',
                               category_orders={"nutriscore_grade": ["a", "b", "c", "d", "e"]},
                               color_discrete_map={'a':'#2a9d8f', 'b':'#8ab17d', 'c':'#e9c46a', 'd':'#f4a261', 'e':'#e76f51'},
                               title="Mối quan hệ NOVA (Chế biến) và Nutri-Score (Lành mạnh)")
            st.plotly_chart(fig, use_container_width=True, config=PLOT_CONFIG) 

        # 6. TƯƠNG QUAN DINH DƯỠNG
        elif "6." in analysis_type:
            fig_corr = px.imshow(df[params['nutr']].corr(), text_auto=".2f", color_continuous_scale="RdBu_r")
            st.plotly_chart(add_border(fig_corr, "heatmap"), use_container_width=True)

        # 7. RADAR CHART (HỒ SƠ DINH DƯỠNG)
        elif "7." in analysis_type:
            if not params['nutr']:
                st.warning("Vui lòng chọn ít nhất 1 thành phần dinh dưỡng.")
            else:
                df_radar = df.groupby('countries_en')[params['nutr']].mean().loc[['France', 'United States']].reset_index()
                fig = go.Figure()
                for i, row in df_radar.iterrows():
                    fig.add_trace(go.Scatterpolar(
                        r=row[params['nutr']].values, 
                        theta=params['nutr'], 
                        fill='toself', 
                        name=row['countries_en']
                    ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True)),
                    title="Hồ sơ dinh dưỡng trung bình: France vs United States"
                )
                st.plotly_chart(fig, use_container_width=True, config=PLOT_CONFIG)
                

        # 8. TƯƠNG QUAN NĂNG LƯỢNG
        elif "8." in analysis_type:
            df_reg = df[df['general_category'].isin(params['cats'])]
            fig = px.scatter(df_reg, x=params['nutr_target'], y="energy_100g", color="general_category", 
                             trendline="ols", title=f"Tương quan Năng lượng và {params['nutr_target']} theo nhóm")
            st.plotly_chart(add_border(fig, "scatter"), use_container_width=True, config=PLOT_CONFIG)

        # 9. MỨC ĐỘ PHỔ BIẾN TỪNG LOẠI SẢN PHẨM THEO QUỐC GIA
        elif "9." in analysis_type:
            df_scan = df[df['countries_en'] == params['country']]
            scan_stats = df_scan.groupby('general_category')['unique_scans_n'].apply(
                lambda x: (x == 1).sum() / len(x) * 100
            ).reset_index(name='pct')
            
            fig = px.bar(scan_stats, x='general_category', y='pct', text_auto='.1f', 
                         color='pct', color_continuous_scale=COOL_CONTINUOUS,
                         labels={'pct': '% Sản phẩm được biết tới (Scan=1)'},
                         title=f"Mức độ nhận diện sản phẩm tại {params['country']}")
            st.plotly_chart(add_border(fig, "bar"), use_container_width=True, config=PLOT_CONFIG) 

    else:
        st.info("Lựa chọn mục tiêu cần phân tích ở Sidebar và nhấn nút 'PHÂN TÍCH' để xem kết quả.")
        fig_intro = px.histogram(df, x='nutriscore_grade', 
                                 category_orders={"nutriscore_grade": ["a", "b", "c", "d", "e"]},
                                 color_discrete_sequence=[COOL_DISCRETE[1]])
        st.plotly_chart(add_border(fig_intro, "hist"), use_container_width=True)

else:
    st.error("Không thể tải dữ liệu.")