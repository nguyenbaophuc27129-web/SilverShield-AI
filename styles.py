import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. XÓA SẠCH GIAO DIỆN MẶC ĐỊNH CỦA STREAMLIT */
        [data-testid="stHeader"], [data-testid="stSidebar"], .st-emotion-cache-1av54u3 {
            display: none !important;
        }
        .stApp { background-color: #ffffff; }
        .block-container { padding-top: 0rem; padding-bottom: 0rem; max-width: 100%; }

        /* 2. THANH TOP-BAR (THÔNG TIN LIÊN HỆ) */
        .top-info {
            background-color: #002147;
            color: white;
            padding: 8px 10%;
            display: flex;
            justify-content: space-between;
            font-size: 13px;
        }

        /* 3. THANH MENU CHÍNH (NAVIGATION) */
        .navbar {
            display: flex;
            align-items: center;
            padding: 10px 10%;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .nav-logo { width: 80px; margin-right: 20px; }
        .nav-links {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
            flex-grow: 1;
        }
        .nav-item {
            padding: 10px 15px;
            color: #333;
            text-decoration: none;
            font-weight: 700;
            font-size: 14px;
            text-transform: uppercase;
            cursor: pointer;
        }
        .nav-item:hover { color: #007bff; }
        
        /* NÚT ĐĂNG KÝ / ĐĂNG NHẬP KIỂU OLYMPIC */
        .btn-group { display: flex; gap: 10px; }
        .btn-reg {
            background-color: #d32f2f;
            color: white !important;
            padding: 8px 20px;
            border-radius: 4px;
            font-weight: bold;
            text-decoration: none;
            font-size: 13px;
        }
        .btn-login {
            background-color: #ff9800;
            color: white !important;
            padding: 8px 20px;
            border-radius: 4px;
            font-weight: bold;
            text-decoration: none;
            font-size: 13px;
        }

        /* 4. BANNER KHỔ LỚN */
        .main-banner {
            width: 100%;
            height: 450px;
            background-image: linear-gradient(rgba(0,33,71,0.5), rgba(0,33,71,0.5)), 
                              url('https://olympicenglish.vn/upload/banner-olympic-2025.png'); /* Chỗ này lát bà thay link hình */
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            flex-direction: column;
        }
        .banner-btn {
            background-color: #007bff;
            padding: 12px 30px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
            text-decoration: none;
            margin-top: 20px;
            border: 2px solid white;
        }

        /* 5. KHUNG NỘI DUNG */
        .section-container { padding: 40px 10%; }
        .card-pro {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
            border-top: 4px solid #002147;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    # Top info
    st.markdown("""
        <div class="top-info">
            <div>Phát triển và xây dựng bởi DVT-Empire X CBZ - Trường THPT Dương Văn Thì</div>
            <div>SILVERSHIELD - Vì an toàn không gian mạng</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Navbar
    st.markdown("""
        <div class="navbar">
            <img class="nav-logo" src="https://olympicenglish.vn/images/logo.png">
            <div class="nav-links">
                <a class="nav-item">Giới thiệu</a>
                <a class="nav-item">Tin tức</a>
            </div>
    """, unsafe_allow_html=True)
