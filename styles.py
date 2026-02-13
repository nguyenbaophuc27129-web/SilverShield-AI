import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* IMPORT FONT CHUẨN */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

        /* 1. RESET LAYOUT & CẤU HÌNH CHUNG */
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f7f9;
        }
        .block-container {
            max-width: 100% !important; /* Full màn hình để làm banner */
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* ẨN MẶC ĐỊNH */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* 2. TOP BAR (THANH TRÊN CÙNG - MÀU XANH ĐẬM) */
        .top-bar {
            background-color: #003366; /* Màu xanh Olympic */
            color: white;
            padding: 8px 0;
            font-size: 13px;
            font-weight: 500;
        }
        .top-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            padding: 0 15px;
        }

        /* 3. NAVBAR (MENU CHÍNH - MÀU TRẮNG) */
        .nav-wrapper {
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 999;
        }
        .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 10px 15px;
        }

        /* Nút menu Streamlit chỉnh lại cho giống Text Link */
        div.stButton > button {
            background: transparent !important;
            color: #003366 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            margin: 0 !important;
            padding: 10px 15px !important;
            border-radius: 0 !important;
        }
        div.stButton > button:hover {
            color: #d32f2f !important; /* Hover đỏ giống Olympic */
            background: #f8f9fa !important;
        }
        div.stButton > button:focus {
            color: #d32f2f !important;
            box-shadow: none !important;
        }

        /* 4. HERO SECTION (BANNER + NỀN ĐEN MỜ) */
        .hero-section {
            position: relative;
            /* Ảnh nền công nghệ chìm phía sau */
            background-image: url('https://img.freepik.com/free-vector/gradient-technological-background_23-2148884155.jpg'); 
            background-size: cover;
            background-position: center;
            padding: 60px 0;
            color: white;
            overflow: hidden;
        }
        
        /* Lớp phủ đen mờ (Overlay) */
        .hero-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(90deg, rgba(0,51,102,0.9) 0%, rgba(0,51,102,0.7) 100%);
            z-index: 1;
        }

        /* Nội dung Banner nổi lên trên */
        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        /* Khối đen mờ bên phải (Giống khung 'Bắt đầu thi' của Olympic) */
        .glass-box {
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 8px;
            padding: 30px;
            text-align: center;
        }

        /* 5. CÁC SECTION NỘI DUNG */
        .content-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 15px;
        }
        
        .section-header {
            color: #003366;
            font-size: 24px;
            font-weight: 700;
            text-transform: uppercase;
            border-left: 5px solid #d32f2f; /* Vạch đỏ bên trái */
            padding-left: 15px;
            margin-bottom: 25px;
            background: #eef2f6;
            padding-top: 5px;
            padding-bottom: 5px;
        }

        /* Card tin tức */
        .news-card {
            background: white;
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
            transition: 0.3s;
        }
        .news-card:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border-color: #003366;
        }

        /* 6. FOOTER */
        .footer {
            background: #003366;
            color: white;
            padding: 40px 0;
            margin-top: 50px;
            text-align: center;
            border-top: 4px solid #d32f2f;
        }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown("""
        <div class="top-bar">
            <div class="top-content">
                <div>🛠️ Phát triển và xây dựng bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></div>
                <div>🛡️ SILVERSHIELD</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
