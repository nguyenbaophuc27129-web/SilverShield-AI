import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. CẤU HÌNH KHUNG MÀN HÌNH CHUẨN 1200PX --- */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f6f9;
            color: #333;
        }
        
        /* Ép nội dung vào giữa màn hình chuẩn 1200px */
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        
        /* Ẩn Header mặc định của Streamlit */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER 2 TẦNG (OLYMPIC STYLE) --- */
        
        /* Tầng 1: Top Bar Xanh Đậm */
        .olympic-topbar {
            background-color: #002147; /* Navy Blue Olympic */
            color: white;
            padding: 8px 0;
            font-size: 13px;
            font-weight: 500;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            display: flex; justify-content: center;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        /* Tầng 2: Navbar Trắng */
        .olympic-navbar {
            background-color: white;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 0px;
            display: flex; justify-content: center;
            padding: 10px 0;
            z-index: 100;
        }

        /* Style nút bấm Menu */
        div.stButton > button {
            background: transparent !important;
            color: #002147 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            padding: 10px 20px !important;
            border-radius: 4px !important;
            transition: all 0.3s;
        }
        div.stButton > button:hover {
            background-color: #f0f4f8 !important;
            color: #d32f2f !important; /* Hover đỏ */
        }
        
        /* --- 3. HERO BANNER (XẾP LỚP) --- */
        .hero-container {
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            height: 450px;
            background: linear-gradient(135deg, #002147 0%, #004080 100%); /* Nền xanh digital */
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        /* Hiệu ứng hạt sáng background (giả lập) */
        .hero-bg-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://img.freepik.com/free-vector/dark-blue-technology-background_23-2148443372.jpg');
            background-size: cover;
            opacity: 0.3;
        }
        /* Khối đen mờ (Glass Box) */
        .glass-box {
            background: rgba(0, 0, 0, 0.6); /* Đen mờ */
            backdrop-filter: blur(5px);
            padding: 30px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            text-align: center;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .btn-check-now button {
            background: linear-gradient(to right, #00c6ff, #0072ff) !important;
            color: white !important;
            font-size: 18px !important;
            padding: 12px 30px !important;
            border-radius: 50px !important;
            box-shadow: 0 4px 15px rgba(0, 114, 255, 0.4) !important;
            border: 2px solid white !important;
        }

        /* --- 4. CÁC KHỐI NỘI DUNG (SECTIONS) --- */
        
        /* Banner Strip (Về ứng dụng / Hướng dẫn) */
        .banner-strip {
            background: white;
            border: 1px solid #e0e0e0;
            padding: 30px;
            text-align: center;
            height: 100%;
        }
        .banner-header {
            color: #d32f2f; /* Đỏ đô */
            font-weight: 700;
            font-size: 20px;
            text-transform: uppercase;
            margin-bottom: 15px;
        }
        .banner-divider {
            height: 1px;
            background-color: #e0e0e0;
            width: 50px;
            margin: 0 auto 15px auto;
        }

        /* Quy tắc an toàn (3 Cột màu) */
        .rules-main-header {
            background-color: #002147;
            color: white;
            padding: 15px 20px;
            font-size: 18px;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 40px;
            display: flex; align-items: center; gap: 10px;
        }
        .rule-card {
            background: white;
            border: 1px solid #ddd;
            height: 100%;
        }
        .rule-header {
            padding: 15px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 18px;
            text-transform: uppercase;
        }
        .bg-red { background-color: #e53935; }
        .bg-green { background-color: #43a047; }
        .bg-teal { background-color: #00897b; }
        .rule-body { padding: 20px; font-size: 14px; line-height: 1.8; }
        .rule-item { border-bottom: 1px solid #eee; padding: 5px 0; }

        /* Tin tức Grid */
        .news-header-bar {
            background-color: #0044cc; /* Royal Blue */
            border-top: 3px solid #d32f2f;
            color: white;
            text-align: center;
            padding: 10px;
            font-weight: 700;
            font-size: 20px;
            font-family: serif; /* Font có chân trang trọng */
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .news-card {
            background: white;
            display: flex;
            border: 1px solid #eee;
            margin-bottom: 15px;
            transition: 0.3s;
            cursor: pointer;
        }
        .news-card:hover { box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-color: #0044cc; }
        .news-thumb { width: 40%; object-fit: cover; }
        .news-content { width: 60%; padding: 15px; }
        .news-title {
            color: #003366;
            font-weight: 700;
            font-size: 14px;
            text-transform: uppercase;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        /* --- 5. FOOTER --- */
        .footer {
            background-color: #002147;
            color: white;
            padding: 40px 0;
            text-align: center;
            border-top: 5px solid #d32f2f;
            margin-top: 50px;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header_structure():
    # TẦNG 1: TOP BAR
    st.markdown("""
        <div class="olympic-topbar">
            <div style="width:1200px; display:flex; justify-content:space-between; padding:0 15px;">
                <span>🛠️ Phát triển và xây dựng bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></span>
                <span>🛡️ <b>SILVERSHIELD</b></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer_structure():
    st.markdown("""
        <div class="footer">
            <h2 style="margin:0;">SILVERSHIELD</h2>
            <p style="opacity:0.8; margin-top:5px;">"Vì một không gian mạng an toàn"</p>
            <div style="border-top:1px solid rgba(255,255,255,0.2); width:200px; margin:20px auto;"></div>
            <p style="font-size:13px;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
        </div>
    """, unsafe_allow_html=True)
