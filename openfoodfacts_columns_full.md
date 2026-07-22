| STT | Column | Meaning |
|-----|---------|----------|
| 1 | `code` | Mã sản phẩm duy nhất (barcode hoặc mã vạch). |
| 2 | `url` | Liên kết đến trang sản phẩm trên Open Food Facts. |
| 3 | `creator` | Người hoặc hệ thống tạo bản ghi. |
| 4 | `created_t` | Thời điểm tạo bản ghi (timestamp UNIX). |
| 5 | `created_datetime` | Thời điểm tạo bản ghi (ISO 8601). |
| 6 | `last_modified_t` | Thời điểm chỉnh sửa gần nhất (timestamp UNIX). |
| 7 | `last_modified_datetime` | Thời điểm chỉnh sửa gần nhất (ISO 8601). |
| 8 | `last_modified_by` | Người cập nhật cuối cùng. |
| 9 | `last_updated_t` | Giống last_modified_*, dùng cho đồng bộ dữ liệu |
| 10 | `last_updated_datetime` | CGiống last_modified_*, dùng cho đồng bộ dữ liệu |
| 11 | `product_name` | Tên thương mại của sản phẩm. |
| 12 | `abbreviated_product_name` | Tên rút gọn của sản phẩm. |
| 13 | `generic_name` | Tên mô tả loại thực phẩm. |
| 14 | `quantity` | Khối lượng hoặc thể tích ghi trên bao bì. |
| 15 | `packaging` | Mô tả loại bao bì (chai, hộp, túi...). |
| 16 | `packaging_tags` | Thẻ bao bì (dạng tag, có thể dùng để phân tích môi trường)["en:glass", "en:jar"]  |
| 17 | `packaging_en` | Thẻ bao bì (dạng tag, có thể dùng để phân tích môi trường)["en:glass", "en:jar"]  |
| 18 | `packaging_text` | Ghi chú thêm về bao bì ("Recyclable jar")|
| 19 | `brands` | Thương hiệu sản phẩm. |
| 20 | `brands_tags` | Tag thương hiệu |
| 21 | `brands_en` | Tag thương hiệu |
| 22 | `categories` | Danh mục sản phẩm. |
| 23 | `categories_tags` | Tag danh mục sản phẩm |
| 24 | `categories_en` | Tag danh mục sản phẩm |
| 25 | `origins` | Nguồn gốc sản phẩm hoặc nguyên liệu. |
| 26 | `origins_tags` | Tag nguồn gốc |
| 27 | `origins_en` | Tag nguồn gốc |
| 28 | `manufacturing_places` | Nơi sản xuất hoặc đóng gói. |
| 29 | `manufacturing_places_tags` | Tag nơi sản xuất |
| 30 | `labels` | Nhãn đặc biệt (organic, fair trade, halal...). |
| 31 | `labels_tags` | Tag nhãn |
| 32 | `labels_en` | Tag nhãn |
| 33 | `emb_codes` | Mã nhà máy / cơ sở đóng gói |
| 34 | `emb_codes_tags` | Tag mã nhà máy / cơ sở đóng gói |
| 35 | `first_packaging_code_geo` | Mã địa lý của nơi đóng gói đầu tiên |
| 36 | `cities` | Thành phố bán/ phân phối |
| 37 | `cities_tags` | Tag thành phố |
| 38 | `purchase_places` | Khu vực hoặc quốc gia nơi mua hàng. |
| 39 | `stores` | Tên cửa hàng / chuỗi |
| 40 | `countries` | Quốc gia có sản phẩm |
| 41 | `countries_tags` | Tag quốc gia có sản phẩm |
| 42 | `countries_en` | Quốc gia (tiếng Anh). |
| 43 | `ingredients_text` | Danh sách thành phần sản phẩm (chuỗi văn bản). |
| 44 | `ingredients_tags` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 45 | `ingredients_analysis_tags` | Phân tích thành phần (vegan, palm-oil...). |
| 46 | `allergens` | Các chất gây dị ứng có trong sản phẩm. |
| 47 | `allergens_en` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 48 | `traces` | Dấu vết dị ứng có thể có. |
| 49 | `traces_tags` | Tag dấu vết dị ứng |
| 50 | `traces_en` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 51 | `serving_size` | Kích thước khẩu phần (ví dụ: 30g). |
| 52 | `serving_quantity` | Số lượng khẩu phần thực tế (g/ml) |
| 53 | `no_nutrition_data` | =1 nếu không có dữ liệu dinh dưỡng |
| 54 | `additives_n` | Số lượng chất phụ gia |
| 55 | `additives` | Danh sách phụ gia (E-code). |
| 56 | `additives_tags` | Tag chất phụ gia |
| 57 | `additives_en` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 58 | `nutriscore_score` | Điểm NutriScore (số, càng thấp càng tốt). |
| 59 | `nutriscore_grade` | Xếp hạng NutriScore (A–E). |
| 60 | `nova_group` | Nhóm NOVA (mức độ chế biến 1–4): 1: tự nhiên → 4: siêu chế biến. |
| 61 | `pnns_groups_1` | Nhóm PNNS cấp 1 (Pháp). "Sweetened products" |
| 62 | `pnns_groups_2` | Nhóm PNNS cấp 2 (chi tiết hơn). "Chocolate products" |
| 63 | `food_groups` | Nhóm thực phẩm chính |
| 64 | `food_groups_tags` | Tag nhóm thực phẩm chính |
| 65 | `food_groups_en` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 66 | `states` | Trạng thái dữ liệu (hoàn thiện, cần kiểm duyệt) |
| 67 | `states_tags` | Tag trạng thái dữ liệu (hoàn thiện, cần kiểm duyệt) |
| 68 | `states_en` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 69 | `brand_owner` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 70 | `environmental_score_score` | Điểm tác động môi trường |
| 71 | `environmental_score_grade` | Xếp loại môi trường (A–E). |
| 72 | `nutrient_levels_tags` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 73 | `product_quantity` | Tổng khối lượng sản phẩm |
| 74 | `owner` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 75 | `data_quality_errors_tags` | Lỗi dữ liệu (nếu có) |
| 76 | `unique_scans_n` | Số lần người dùng quét mã sản phẩm |
| 77 | `popularity_tags` | Mức độ phổ biến (low, medium, high): "en:top-5000" |
| 78 | `completeness` | Tỷ lệ hoàn thiện dữ liệu (0–1) |
| 79 | `last_image_t` | Thời điểm cập nhật ảnh |
| 80 | `last_image_datetime` | Thời điểm cập nhật ảnh |
| 81 | `main_category` | Danh mục chính "en:chocolate-spreads" |
| 82 | `main_category_en` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 83 | `image_url` | Ảnh chính của sản phẩm. |
| 84 | `image_small_url` | Ảnh nhỏ |
| 85 | `image_ingredients_url` | Ảnh danh sách thành phần. |
| 86 | `image_ingredients_small_url` | Ảnh nhỏ danh sách thành phần |
| 87 | `image_nutrition_url` | Ảnh bảng dinh dưỡng. |
| 88 | `image_nutrition_small_url` | Ảnh bảng dinh dưỡng nhỏ |
| 89 | `energy-kj_100g` | Năng lượng (kilojoule/100g). |
| 90 | `energy-kcal_100g` | Năng lượng (kilocalorie/100g). |
| 91 | `energy_100g` | Tổng năng lượng /100g. |
| 92 | `energy-from-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 93 | `fat_100g` | Tổng chất béo /100g. |
| 94 | `saturated-fat_100g` | Chất béo bão hòa /100g. |
| 95 | `butyric-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 96 | `caproic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 97 | `caprylic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 98 | `capric-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 99 | `lauric-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 100 | `myristic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 101 | `palmitic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 102 | `stearic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 103 | `arachidic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 104 | `behenic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 105 | `lignoceric-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 106 | `cerotic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 107 | `montanic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 108 | `melissic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 109 | `unsaturated-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 110 | `monounsaturated-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 111 | `omega-9-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 112 | `polyunsaturated-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 113 | `omega-3-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 114 | `omega-6-fat_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 115 | `alpha-linolenic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 116 | `eicosapentaenoic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 117 | `docosahexaenoic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 118 | `linoleic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 119 | `arachidonic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 120 | `gamma-linolenic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 121 | `dihomo-gamma-linolenic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 122 | `oleic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 123 | `elaidic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 124 | `gondoic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 125 | `mead-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 126 | `erucic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 127 | `nervonic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 128 | `trans-fat_100g` | Chất béo chuyển hóa /100g. |
| 129 | `cholesterol_100g` | Cholesterol /100g. |
| 130 | `carbohydrates_100g` | Tổng carbohydrate /100g. |
| 131 | `sugars_100g` | Tổng lượng đường /100g. |
| 132 | `added-sugars_100g` | Lượng đường thêm vào /100g. |
| 133 | `sucrose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 134 | `glucose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 135 | `fructose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 136 | `galactose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 137 | `lactose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 138 | `maltose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 139 | `maltodextrins_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 140 | `psicose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 141 | `starch_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 142 | `polyols_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 143 | `erythritol_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 144 | `isomalt_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 145 | `maltitol_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 146 | `sorbitol_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 147 | `fiber_100g` | Chất xơ /100g. |
| 148 | `soluble-fiber_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 149 | `polydextrose_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 150 | `insoluble-fiber_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 151 | `proteins_100g` | Protein /100g. |
| 152 | `casein_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 153 | `serum-proteins_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 154 | `nucleotides_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 155 | `salt_100g` | Muối /100g. |
| 156 | `added-salt_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 157 | `sodium_100g` | Natri /100g. |
| 158 | `alcohol_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 159 | `vitamin-a_100g` | Vitamin A /100g. |
| 160 | `beta-carotene_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 161 | `vitamin-d_100g` | Vitamin D /100g. |
| 162 | `vitamin-e_100g` | Vitamin E /100g. |
| 163 | `vitamin-k_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 164 | `vitamin-c_100g` | Vitamin C /100g. |
| 165 | `vitamin-b1_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 166 | `vitamin-b2_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 167 | `vitamin-pp_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 168 | `vitamin-b6_100g` | Vitamin B6 /100g. |
| 169 | `vitamin-b9_100g` | Vitamin B9 (folate) /100g. |
| 170 | `folates_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 171 | `vitamin-b12_100g` | Vitamin B12 /100g. |
| 172 | `biotin_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 173 | `pantothenic-acid_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 174 | `silica_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 175 | `bicarbonate_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 176 | `potassium_100g` | Kali /100g. |
| 177 | `chloride_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 178 | `calcium_100g` | Canxi /100g. |
| 179 | `phosphorus_100g` | Phốt pho /100g. |
| 180 | `iron_100g` | Sắt /100g. |
| 181 | `magnesium_100g` | Magie /100g. |
| 182 | `zinc_100g` | Kẽm /100g. |
| 183 | `copper_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 184 | `manganese_100g` | Mangan /100g. |
| 185 | `fluoride_100g` | Flo /100g. |
| 186 | `selenium_100g` | Selen /100g. |
| 187 | `chromium_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 188 | `molybdenum_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 189 | `iodine_100g` | I-ốt /100g. |
| 190 | `caffeine_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 191 | `taurine_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 192 | `methylsulfonylmethane_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 193 | `ph_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 194 | `fruits-vegetables-nuts_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 195 | `fruits-vegetables-nuts-dried_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 196 | `fruits-vegetables-nuts-estimate_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 197 | `fruits-vegetables-nuts-estimate-from-ingredients_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 198 | `collagen-meat-protein-ratio_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 199 | `cocoa_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 200 | `chlorophyl_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 201 | `carbon-footprint_100g` | Dấu chân carbon /100g sản phẩm. |
| 202 | `carbon-footprint-from-meat-or-fish_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 203 | `nutrition-score-fr_100g` | Điểm NutriScore (chuẩn Pháp). |
| 204 | `nutrition-score-uk_100g` | Điểm NutriScore (chuẩn Anh). |
| 205 | `glycemic-index_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 206 | `water-hardness_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 207 | `choline_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 208 | `phylloquinone_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 209 | `beta-glucan_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 210 | `inositol_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 211 | `carnitine_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 212 | `sulphate_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 213 | `nitrate_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |
| 214 | `acidity_100g` | Độ axit /100g. |
| 215 | `carbohydrates-total_100g` | Chưa có mô tả cụ thể – cột metadata, nhãn hoặc dinh dưỡng chi tiết. |