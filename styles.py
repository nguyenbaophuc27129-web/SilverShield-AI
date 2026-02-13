import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. IMPORT FONTS & GLOBAL RESET --- */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Inter:wght@400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #333;
            background-color: #f5f7fa; /* Nền xám nhạt hiện đại */
        }
        
        h1, h2, h3 { font-family: 'Poppins', sans-serif; }

        /* Căn giữa trang web chuẩn 1200px */
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 4rem !important;
            margin: 0 auto !important;
        }

        /* Ẩn Header mặc định */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER SYSTEM (Giống Olympic) --- */
        
        /* Tầng 1: Top Bar */
        .top-bar {
            background-color: #0c3c78; /* Dark Blue */
            color: white;
            padding: 8px 0;
            font-size: 13px;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            display: flex; justify-content: center;
        }
        
        /* Tầng 2: Navbar */
        .navbar-container {
            background: white;
            padding: 15px 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin-bottom: 0px;
            border-bottom: 1px solid #eee;
            position: sticky; top: 0; z-index: 100;
        }

        /* Styling cho các nút Menu (Streamlit Buttons) */
        div.stButton > button {
            background-color: transparent !important;
            color: #0c3c78 !important;
            border: none !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
            padding: 0px 15px !important;
            height: auto !important;
            border-bottom: 2px solid transparent !important;
            border-radius: 0 !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            color: #1b5fa7 !important;
            border-bottom: 2px solid #1b5fa7 !important;
            background-color: transparent !important;
        }
        div.stButton > button:focus {
            color: #1b5fa7 !important;
            border-bottom: 2px solid #1b5fa7 !important;
            box-shadow: none !important;
        }

        /* Nút Action (KIỂM TRA NGAY) nổi bật trên Menu */
        .btn-cta button {
            background: linear-gradient(90deg, #d32f2f, #b71c1c) !important;
            color: white !important;
            padding: 10px 25px !important;
            border-radius: 50px !important;
            border: none !important;
            box-shadow: 0 4px 10px rgba(211, 47, 47, 0.3) !important;
        }
        .btn-cta button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(211, 47, 47, 0.4) !important;
        }

        /* --- 3. HERO SECTION (Gradient Blue) --- */
        .hero-bg {
            background: linear-gradient(135deg, #0c3c78 0%, #1b5fa7 100%);
            color: white;
            padding: 60px 40px;
            border-radius: 20px;
            margin-top: 30px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(12, 60, 120, 0.2);
            position: relative;
            overflow: hidden;
        }
        .hero-title {
            font-size: 42px;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 20px;
        }
        .hero-desc {
            font-size: 18px;
            opacity: 0.9;
            margin-bottom: 30px;
            max-width: 600px;
        }

        /* --- 4. CARDS & SECTIONS --- */
        .section-wrapper {
            margin-bottom: 60px;
        }
        .section-title {
            color: #0c3c78;
            font-size: 28px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        .section-subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
        
        /* Card trắng sạch sẽ */
        .clean-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            border: 1px solid #eef2f6;
            box-shadow: 0 5px 15px rgba(0,0,0,0.03);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
        }
        .clean-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.08);
            border-color: #ffcc00; /* Viền vàng khi hover */
        }

        /* --- 5. AI TOOL INTERFACE --- */
        .ai-container {
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            padding: 40px;
            border-top: 5px solid #0c3c78;
        }
        .result-box {
            background-color: #f0f9ff;
            border-left: 4px solid #0c3c78;
            padding: 20px;
            border-radius: 4px;
            margin-top: 20px;
        }

        /* --- 6. FOOTER --- */
        .footer {
            background-color: #0c3c78;
            color: white;
            padding: 60px 0;
            margin-top: 80px;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            border-top: 4px solid #d32f2f; /* Line đỏ giống Olympic */
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown("""
        <div class="top-bar">
            <div style="width: 1200px; display: flex; justify-content: space-between; padding: 0 15px;">
                <span>🛠️ Phát triển bởi <b>DVT - Empire CBZ X</b></span>
                <span style="font-weight: 600;">🛡️ SILVERSHIELD 2026</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="footer">
            <h2 style="margin: 0; color: white;">SILVERSHIELD</h2>
            <p style="opacity: 0.8; margin-top: 10px;">"Vì một không gian mạng an toàn cho người cao tuổi"</p>
            <div style="margin: 30px 0;">
                <span style="margin: 0 10px; cursor: pointer;">Trang chủ</span> | 
                <span style="margin: 0 10px; cursor: pointer;">Điều khoản</span> | 
                <span style="margin: 0 10px; cursor: pointer;">Bảo mật</span>
            </div>
            <p style="font-size: 13px; opacity: 0.6;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CB2.X</p>
        </div>
    """, unsafe_allow_html=True)        .top-bar-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 1rem;
            font-size: 13px;
            font-weight: 500;
        }

        /* 3. NAVIGATION (MENU) */
        .nav-container {
            background: white;
            padding: 10px 20px;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 25px;
            display: flex;
            align-items: center;
        }
        /* Style cho nút bấm menu */
        div.stButton > button {
            background-color: transparent !important;
            color: #003366 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            margin: 0 5px !important;
            border-radius: 4px !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            color: #d32f2f !important;
            background-color: #e3f2fd !important;
        }
        div.stButton > button:focus {
            color: #d32f2f !important;
            box-shadow: none !important;
        }
        
        /* 4. HEADINGS & TITLES */
        .section-header {
            color: #003366;
            font-size: 20px;
            font-weight: 700;
            text-transform: uppercase;
            border-left: 5px solid #ffcc00;
            padding-left: 12px;
            margin: 30px 0 15px 0;
            line-height: 1.2;
        }

        /* 5. CARDS (KHUNG NỘI DUNG) */
        .olympic-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
            height: 100%;
            transition: transform 0.2s;
        }
        .olympic-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
            border-color: #00aeef;
        }
        .card-title-blue { color: #003366; font-weight: bold; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
        .card-title-red { color: #d32f2f; font-weight: bold; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
        .card-title-cyan { color: #00838f; font-weight: bold; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }

        /* 6. LIST STYLES */
        .custom-list { list-style-type: none; padding: 0; }
        .custom-list li {
            padding: 8px 0;
            border-bottom: 1px dashed #eee;
            font-size: 14px;
            color: #444;
        }
        .custom-list li:last-child { border-bottom: none; }

        /* 7. FOOTER */
        .footer-container {
            background-color: #003366;
            color: white;
            padding: 40px 0;
            margin-top: 50px;
            text-align: center;
            border-top: 5px solid #d32f2f;
        }
        </style>
    """, unsafe_allow_html=True)

# HÀM RENDER TOP BAR (Để sửa lỗi AttributeError)
def render_top_bar():
    st.markdown("""
        <div class="top-bar-container">
            <div class="top-bar-content">
                <div>🛠️ Phát triển và xây dựng bởi <b>DVT - Empire CBZ X</b></div>
                <div style="font-weight: 700; letter-spacing: 1px;">🛡️ SILVERSHIELD</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
