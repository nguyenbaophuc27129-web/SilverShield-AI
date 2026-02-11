import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. KHUNG MÀN HÌNH CHUẨN 1200PX */
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }

        /* ẨN GIAO DIỆN MẶC ĐỊNH */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        .stApp { background-color: #f4f7f9; font-family: 'Arial', sans-serif; }

        /* 2. THANH TOP BAR (MÀU XANH ĐẬM TRÊN CÙNG) */
        .top-bar-container {
            background-color: #002147;
            color: white;
            font-size: 13px;
            padding: 8px 0;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: center;
        }
        .top-bar-content {
            width: 1200px;
            display: flex;
            justify-content: space-between;
            padding: 0 15px;
        }

        /* 3. MENU NAVIGATION */
        .nav-container {
            background: white;
            margin-top: 0px;
            border-bottom: 4px solid #FFB300; /* Viền vàng dưới menu */
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            padding: 10px 0;
        }
        div.stButton > button {
            background-color: transparent !important;
            color: #002147 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            border-radius: 0 !important;
            transition: 0.2s;
        }
        div.stButton > button:hover {
            color: #D32F2F !important;
            background-color: #f0f2f5 !important;
        }

        /* 4. TIÊU ĐỀ KHỐI (GIỐNG MẪU OLYMPIC 'ĐƠN VỊ TỔ CHỨC') */
        .olympic-header {
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-bottom: none;
            color: #D32F2F; /* Màu đỏ đô sang trọng */
            font-weight: 800;
            text-transform: uppercase;
            padding: 12px 20px;
            font-size: 16px;
            text-align: center;
            margin-top: 30px;
            border-radius: 5px 5px 0 0;
            position: relative;
        }
        /* Kẻ vạch màu xanh dưới tiêu đề */
        .olympic-header::after {
            content: '';
            display: block;
            width: 50px;
            height: 3px;
            background: #002147;
            margin: 5px auto 0;
        }

        /* 5. NỘI DUNG KHỐI (BOX) */
        .olympic-box {
            background: white;
            border: 1px solid #ddd;
            padding: 25px;
            border-radius: 0 0 5px 5px; /* Bo góc dưới */
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
            margin-bottom: 20px;
        }

        /* 6. LOGO ĐỐI TÁC */
        .partner-img {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100px;
        }
        .partner-label {
            font-size: 12px;
            font-weight: bold;
            color: #002147;
            margin-top: 10px;
            text-align: center;
            text-transform: uppercase;
        }

        /* FOOTER */
        .footer-container {
            background: #002147;
            color: white;
            text-align: center;
            padding: 40px 0;
            margin-top: 50px;
            border-top: 5px solid #FFB300;
        }
        </style>
    """, unsafe_allow_html=True)

# ĐÂY LÀ HÀM BẠN ĐANG BỊ LỖI - TUI ĐÃ THÊM VÀO RỒI
def render_top_bar():
    st.markdown("""
        <div class="top-bar-container">
            <div class="top-bar-content">
                <div>🛠️ Phát triển bởi <b>DVT - Empire CBZ X</b> - THPT Dương Văn Thì</div>
                <div>🛡️ <b>SILVERSHIELD</b> - VÌ KHÔNG GIAN MẠNG AN TOÀN</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Hàm tạo tiêu đề giống Olympic
def section_header(title):
    st.markdown(f'<div class="olympic-header">{title}</div>', unsafe_allow_html=True)

def open_box():
    st.markdown('<div class="olympic-box">', unsafe_allow_html=True)

def close_box():
    st.markdown('</div>', unsafe_allow_html=True)
