import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. CẤU HÌNH KHUNG MÀN HÌNH CHUẨN 1200PX --- */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f6f9;
        }
        
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER TẦNG --- */
        .olympic-topbar {
            background-color: #002147;
            color: white;
            padding: 8px 0;
            font-size: 13px;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            display: flex; justify-content: center;
        }
        
        .olympic-navbar {
            background-color: white;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
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
        }
        
        /* --- 3. HERO BANNER (XẾP LỚP - CHỈNH SỬA TẠI ĐÂY) --- */
        .hero-container {
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            min-height: 480px;
            background: linear-gradient(135deg, #002147 0%, #004080 100%);
            display: flex; justify-content: center; align-items: center;
            padding: 20px 0;
        }
        
        .hero-bg-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://img.freepik.com/free-vector/dark-blue-technology-background_23-2148443372.jpg');
            background-size: cover;
            opacity: 0.15;
        }

        /* Khối Glassmorphism bên phải */
        .glass-box {
            background: rgba(0, 15, 30, 0.7); 
            backdrop-filter: blur(10px);
            padding: 40px 25px;
            border-radius: 5px;
            border: 1px solid rgba(255,255,255,0.1);
            color: white;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        }

        /* Nút kiểm tra ngay chuẩn màu sáng */
        .btn-check-now button {
            background: #007bff !important; /* Xanh tươi y chang mẫu */
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            padding: 12px 0px !important;
            border-radius: 4px !important;
            border: none !important;
            width: 100% !important;
        }

        /* Các khối khác giữ nguyên của bạn */
        .banner-strip { background: white; border: 1px solid #e0e0e0; padding: 30px; text-align: center; height: 100%; }
        .banner-header { color: #d32f2f; font-weight: 700; font-size: 20px; text-transform: uppercase; margin-bottom: 15px; }
        .rules-main-header { background-color: #002147; color: white; padding: 15px 20px; font-weight: 700; margin-top: 40px; display: flex; align-items: center; gap: 10px; }
        .news-header-bar { background-color: #0044cc; border-top: 3px solid #d32f2f; color: white; text-align: center; padding: 10px; font-weight: 700; margin-top: 40px; }
        .news-card { background: white; display: flex; border: 1px solid #eee; margin-bottom: 15px; transition: 0.3s; }
        .news-thumb { width: 40%; object-fit: cover; }
        .news-content { width: 60%; padding: 15px; }
        .news-title { color: #003366; font-weight: 700; font-size: 14px; text-transform: uppercase; }
        
        .footer { background-color: #002147; color: white; padding: 40px 0; text-align: center; border-top: 5px solid #d32f2f; margin-top: 50px; width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw;}
        </style>
    """, unsafe_allow_html=True)

def render_header_structure():
    st.markdown("""
        <div class="olympic-topbar">
            <div style="width:1200px; display:flex; justify-content:space-between; padding:0 15px;">
                <span>🛠️ Phát triển bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></span>
                <span>🛡️ <b>SILVERSHIELD</b></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer_structure():
    st.markdown("""
        <div class="footer">
            <h2 style="margin:0;">SILVERSHIELD</h2>
            <p style="opacity:0.8; margin-top:5px;">"Vì một không gian mạng an toàn"</p>
            <p style="font-size:13px; margin-top:20px;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
        </div>
    """, unsafe_allow_html=True)
