import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. CẤU HÌNH KHUNG MÀN HÌNH CHUẨN 1200PX (QUAN TRỌNG NHẤT) */
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 3rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            margin: 0 auto !important;
        }
        
        /* 2. ẨN GIAO DIỆN MẶC ĐỊNH */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        .stApp { background-color: #f4f6f9; } /* Màu nền xám nhẹ sang trọng */

        /* 3. THANH TOP BAR (XANH ĐẬM) */
        .top-info {
            background-color: #002147;
            color: white;
            padding: 8px 0;
            font-size: 13px;
            border-bottom: 3px solid #FFB300;
            width: 100vw; /* Tràn viền màn hình */
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: center;
        }
        .top-inner {
            width: 1200px;
            display: flex;
            justify-content: space-between;
            padding: 0 15px;
        }

        /* 4. THANH MENU (NAVIGATION) */
        .nav-container {
            background: white;
            padding: 15px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            border-radius: 0 0 10px 10px;
        }
        /* Chỉnh nút bấm menu cho sang */
        div.stButton > button {
            background-color: transparent !important;
            color: #333 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
            transition: 0.3s;
            margin-top: 5px;
        }
        div.stButton > button:hover {
            color: #002147 !important;
            background-color: #f0f2f5 !important;
            border-radius: 5px !important;
        }
        /* Nút Kiểm tra ngay nổi bật */
        .btn-check-ai button {
            background: linear-gradient(90deg, #D32F2F, #C62828) !important;
            color: white !important;
            padding: 10px 25px !important;
            border-radius: 50px !important;
            box-shadow: 0 4px 10px rgba(211, 47, 47, 0.3) !important;
        }

        /* 5. BANNER HERO */
        .hero-banner {
            width: 100%;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,33,71,0.15);
            margin-bottom: 30px;
        }

        /* 6. CÁC KHỐI NỘI DUNG (CARD) */
        .section-header {
            color: #002147;
            border-left: 5px solid #FFB300;
            padding-left: 15px;
            margin-bottom: 20px;
            margin-top: 20px;
            font-weight: 800;
            text-transform: uppercase;
        }
        
        .card-box {
            background: white;
            padding: 25px;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
            height: 100%;
            transition: transform 0.2s;
        }
        .card-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.08);
            border-color: #FFB300;
        }

        /* 7. LOGO ĐỐI TÁC (FOOTER STYLE) */
        .partner-logo img {
            filter: grayscale(100%);
            opacity: 0.7;
            transition: 0.3s;
        }
        .partner-logo img:hover {
            filter: grayscale(0%);
            opacity: 1;
        }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown("""
        <div class="top-info">
            <div class="top-inner">
                <span>🚀 Phát triển bởi <b>DVT-Empire X CBZ</b> - THPT Dương Văn Thì</span>
                <span>🛡️ <b>SilverShield</b> - Vì an toàn không gian mạng</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
