import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. CẤU HÌNH GIAO DIỆN & CSS CAO CẤP (STYLES) ---
styles.apply_styles()

# Ẩn header mặc định và cấu hình lại layout để Footer luôn ở đáy
st.markdown("""
    <style>
        /* --- CẤU HÌNH LAYOUT CHÍNH --- */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        
        .stApp {
            background-color: #ffffff; /* Nền trắng sạch */
        }

        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* --- NAVBAR STYLE (MẪU CREATIVE STUDIO) --- */
        .creative-navbar {
            background-color: #ffffff;
            border-bottom: 1px solid #e0e0e0;
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 999;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        
        /* Style lại nút bấm Streamlit thành Menu Text */
        div.stButton > button {
            background: transparent !important;
            border: none !important;
            color: #333 !important;
            font-family: 'Arial', sans-serif;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
            padding: 10px 15px !important;
            margin: 0 !important;
            border-radius: 0 !important;
            transition: all 0.3s ease;
        }
        
        /* Hiệu ứng Hover gạch chân xanh (Giống mẫu) */
        div.stButton > button:hover {
            color: #76c720 !important; /* Màu xanh lá mạ của mẫu Focuson */
            background-color: transparent !important;
        }
        div.stButton > button:focus {
            color: #76c720 !important;
            box-shadow: none !important;
        }

        /* --- HERO BANNER STYLE --- */
        .hero-wrapper {
            position: relative;
            width: 100%;
            overflow: hidden;
        }
        .hero-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.1); /* Lớp phủ nhẹ */
            z-index: 1;
        }
        .hero-img {
            width: 100%;
            height: auto;
            display: block;
            min-height: 400px;
            object-fit: cover;
        }

        /* --- CÁC KHỐI NỘI DUNG --- */
        .banner-strip {
            background: #fff;
            border: 1px solid #eee;
            padding: 25px;
            border-radius: 4px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            height: 100%;
            transition: transform 0.3s;
        }
        .banner-strip:hover {
            transform: translateY(-5px);
            border-bottom: 3px solid #76c720;
        }
        .banner-header {
            color: #333;
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 15px;
            border-left: 4px solid #76c720;
            padding-left: 10px;
        }

        .rules-main-header {
            background-color: #002147;
            color: white;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            margin-top: 40px;
            margin-bottom: 20px;
        }

        .rule-card, .news-card {
            background: white;
            border: 1px solid #eee;
            border-radius: 0px; /* Vuông vức theo yêu cầu */
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            height: 100%;
        }
        .rule-header {
            padding: 10px; text-align: center; color: white; font-weight: bold;
        }
        .bg-red { background: #e74c3c; }
        .bg-green { background: #27ae60; }
        .bg-teal { background: #16a085; }

        /* FOOTER FIX */
        footer {visibility: hidden;}
        .custom-footer {
            background-color: #222;
            color: #999;
            padding: 40px 0;
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Gọi logic khởi tạo AI
try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. HEADER & NAVBAR (GIAO DIỆN CREATIVE STUDIO) ---
# Top Bar nhỏ phía trên
styles.render_header_structure() 

# Navbar chính
st.markdown('<div class="creative-navbar"><div style="max-width:1200px; margin:0 auto; padding: 0 15px;">', unsafe_allow_html=True)
col_nav_1, col_nav_2 = st.columns([2, 8])

with col_nav_1:
    # Logo bên trái
    st.markdown("""
        <div style="display:flex; align-items:center; height:100%;">
            <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:50px;">
            <span style="font-weight:bold; font-size:20px; margin-left:10px; color:#333;">SILVERSHIELD</span>
        </div>
    """, unsafe_allow_html=True)

with col_nav_2:
    # Menu bên phải
    m1, m2, m3, m4, m5 = st.columns([1.5, 1.5, 1.5, 2, 2])
    with m1:
        if st.button("HOME"): 
            st.session_state['page'] = 'TRANG CHỦ'
            st.rerun()
    with m2:
        if st.button("ABOUT"): 
            st.session_state['page'] = 'GIỚI THIỆU'
            st.rerun()
    with m3:
        if st.button("NEWS"): 
            st.session_state['page'] = 'TIN TỨC'
            st.rerun()
    with m4:
        if st.button("AI SHIELD", help="Vệ sĩ AI"): 
            st.session_state['page'] = 'VỆ SĨ AI'
            st.rerun()
    with m5:
        # Nút nổi bật
        st.markdown("""
            <a href="#" style="background-color:#76c720; color:white; padding:10px 20px; text-decoration:none; font-weight:bold; border-radius:3px; display:inline-block; margin-top:5px;">GET A QUOTE</a>
        """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)


# --- 3. NỘI DUNG CHÍNH (CONTAINER 1200PX) ---
# Bắt đầu container nội dung
st.markdown('<div style="max-width:1200px; margin:0 auto; padding:0 15px;">', unsafe_allow_html=True)

if st.session_state['page'] == 'TRANG CHỦ':
    st.markdown('</div>', unsafe_allow_html=True) # Tạm đóng container để Banner tràn viền
    
    # --- HERO BANNER (FULL WIDTH) ---
    # Banner tràn màn hình giống mẫu, có lớp overlay nhẹ
    banner_html = """
    <div class="hero-wrapper">
        <div class="hero-overlay"></div>
        <img class="hero-img" src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png">
        <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; color:white; z-index:2; text-shadow: 2px 2px 4px rgba(0,0,0,0.7);">
            <h1 style="font-size:48px; font-weight:900; margin:0; text-transform:uppercase;">WE ARE SILVERSHIELD</h1>
            <p style="font-size:20px; margin-top:10px;">POWERFUL & SMART AI GUARDIAN FOR ELDERS</p>
        </div>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)
    
    # Mở lại container nội dung
    st.markdown('<div style="max-width:1200px; margin:0 auto; padding:40px 15px;">', unsafe_allow_html=True)
    
    # --- KHỐI GIỚI THIỆU & HƯỚNG DẪN ---
    c_intro, c_guide = st.columns(2, gap="large")
    with c_intro:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">VỀ ỨNG DỤNG SILVERSHIELDAI</div>
            <p style="text-align:justify; color:#555; line-height:1.6;">
                SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để tạo hàng rào giúp nhận diện lừa đảo, bảo vệ người cao tuổi an tâm sử dụng mạng internet mỗi ngày.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c_guide:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">HƯỚNG DẪN SỬ DỤNG</div>
            <ul style="text-align:left; color:#555; padding-left:20px; line-height:1.8;">
                <li>• Bước 1: Truy cập mục "AI SHIELD" trên thanh menu.</li>
                <li>• Bước 2: Nhập văn bản hoặc tải ảnh cần kiểm tra.</li>
                <li>• Bước 3: Nhận kết quả và lời khuyên từ AI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # --- KHỐI QUY TẮC AN TOÀN ---
    st.markdown('<div class="rules-main-header">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3, gap="medium")
    with r1:
        st.markdown("""
        <div class="rule-card">
            <div class="rule-header bg-red">5 KHÔNG</div>
            <div style="padding:20px; font-weight:600; font-size:14px; color:#444;">
                1. Không chuyển tiền<br>
                2. Không bấm link lạ<br>
                3. Không đưa OTP<br>
                4. Không cài app lạ<br>
                5. Không sợ đe dọa
            </div>
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.markdown("""
        <div class="rule-card">
            <div class="rule-header bg-green">3 NÊN</div>
            <div style="padding:20px; font-weight:600; font-size:14px; color:#444;">
                1. Nên gọi xác thực<br>
                2. Nên hỏi con cháu<br>
                3. Nên báo công an
            </div>
        </div>
        """, unsafe_allow_html=True)
    with r3:
        st.markdown("""
        <div class="rule-card">
            <div class="rule-header bg-teal">LƯU Ý</div>
            <div style="padding:20px; font-weight:600; font-size:14px; color:#444;">
                1. Luôn bình tĩnh<br>
                2. Đọc tin an ninh<br>
                3. Dùng SilverShield
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- KHỐI TIN TỨC ---
    st.markdown('<div style="margin-top:50px; text-align:center;"><h2 style="color:#333;">TIN TỨC MỚI NHẤT</h2><div style="width:50px; height:3px; background:#76c720; margin:10px auto;"></div></div>', unsafe_allow_html=True)
    
    news_data = [
        {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
        {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/canh-bao-thu-doan-lua-dao-bang-cong-nghe-deepfake-2023032711054321.htm"},
        {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/bay-viec-nhe-luong-cao-tren-mang-4478144.html"}
    ]
    
    cols = st.columns(3)
    for idx, item in enumerate(news_data):
        with cols[idx]:
            st.markdown(f"""
            <div class="news-card">
                <img src="{item["img"]}" style="width:100%; height:200px; object-fit:cover;">
                <div style="padding:15px;">
                    <h4 style="margin:0 0 10px 0; font-size:16px;">{item["title"]}</h4>
                    <a href="{item['url']}" target="_blank" style="color:#76c720; font-weight:bold; text-decoration:none;">ĐỌC THÊM &rarr;</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN & SỨ MỆNH</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown('<div class="banner-strip"><div class="banner-header">SỨ MỆNH</div><p style="padding:20px; text-align:justify; color:#333;">SilverShield ra đời để bảo vệ người cao tuổi Việt Nam trước vấn nạn lừa đảo mạng ngày càng tinh vi. Chúng tôi cam kết sử dụng AI để tạo ra "lá chắn thép" cho mọi gia đình.</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="banner-strip"><div class="banner-header">ĐỘI NGŨ DVT</div><p style="padding:20px; text-align:justify; color:#333;">Đội ngũ Empire CBZ X hội tụ các cá nhân đam mê công nghệ tại THPT Dương Văn Thì, hướng tới những giải pháp vì cộng đồng.</p></div>', unsafe_allow_html=True)

elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="rules-main-header">📰 BẢN TIN AN NINH TOÀN CẢNH</div>', unsafe_allow_html=True)
    st.info("Đang cập nhật danh sách tin tức...")

elif st.session_state['page'] == 'VỆ SĨ AI':
    st.markdown('<div class="rules-main-header">🛡️ TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown('<div class="banner-strip" style="text-align:left;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#333;">NHẬP DỮ LIỆU</h3>', unsafe_allow_html=True)
        txt = st.text_area("Nhập nội dung cần kiểm tra:", height=200, placeholder="Dán tin nhắn hoặc văn bản nghi ngờ vào đây...")
        img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
        if st.button("PHÂN TÍCH NGAY", type="primary", use_container_width=True):
            if txt or img:
                with st.spinner("AI đang quét dữ liệu..."):
                    i = Image.open(img) if img else None
                    st.session_state['res'] = logic.analyze_content(model, txt, i)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="banner-strip" style="text-align:left; background:#f9f9f9;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#333;">KẾT QUẢ</h3>', unsafe_allow_html=True)
        if 'res' in st.session_state:
            st.success("ĐÃ CÓ KẾT QUẢ PHÂN TÍCH")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else: 
            st.info("Kết quả phân tích từ AI sẽ hiển thị tại đây.")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Đóng container chính

# --- 4. FOOTER (ĐÃ KHÓA CỐ ĐỊNH Ở ĐÁY VÀ FULL WIDTH) ---
st.markdown("""
<div style="width:100%; background-color:#222; margin-top:50px;">
    <div class="custom-footer">
        <h2 style="color:white; margin:0;">SILVERSHIELD</h2>
        <p style="color:#777; margin-top:10px;">Vì một không gian mạng an toàn cho mọi người</p>
        <div style="border-top:1px solid #444; width:200px; margin:20px auto;"></div>
        <p style="color:#555; font-size:12px;">© 2026 Designed by DVT-Empire CBZ X</p>
    </div>
</div>
""", unsafe_allow_html=True)
