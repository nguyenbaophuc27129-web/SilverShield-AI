import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. CẤU HÌNH KHUNG MÀN HÌNH CHUẨN 1200PX */
        .block-container {
            max-width: 1200px !important;
            padding-top: 1rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        
        /* ẨN GIAO DIỆN CŨ */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        .stApp { background-color: #f8f9fa; } 

        /* 2. THANH TOP BAR (XANH ĐẬM) */
        .top-info {
            background-color: #002147;
            color: white;
            padding: 8px 0;
            font-size: 13px;
            width: 100vw;
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

        /* 3. MENU NAVIGATION - CANH GIỮA TUYỆT ĐỐI */
        /* Đây là đoạn code quan trọng nhất để hết 'lởn chởn' */
        [data-testid="column"] {
            display: flex !important;
            align-items: center !important; /* Canh giữa chiều dọc */
            justify-content: center !important; /* Canh giữa chiều ngang */
            height: 100% !important;
        }

        /* Biến nút bấm thường thành dạng Text Menu (Giống Olympic) */
        div.stButton > button {
            background-color: transparent !important;
            color: #444 !important; /* Màu chữ xám đen */
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            padding: 0px !important;
            margin: 0px !important;
            transition: 0.3s;
            box-shadow: none !important;
        }
        div.stButton > button:hover {
            color: #002147 !important; /* Hover ra màu xanh Navy */
            background-color: transparent !important;
            text-decoration: underline;
        }
        div.stButton > button:active, div.stButton > button:focus {
            color: #d32f2f !important;
            border-color: transparent !important;
            background-color: transparent !important;
        }

        /* Nút 'KIỂM TRA NGAY' - Nổi bật riêng biệt */
        .btn-check-ai button {
            background: linear-gradient(90deg, #D32F2F, #B71C1C) !important;
            color: white !important;
            padding: 10px 25px !important;
            border-radius: 50px !important;
            box-shadow: 0 4px 10px rgba(211, 47, 47, 0.3) !important;
            text-decoration: none !important;
        }
        .btn-check-ai button:hover {
            transform: translateY(-2px);
            color: white !important;
            text-decoration: none !important;
        }

        /* 4. BANNER & CARD */
        .stImage img {
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
        
        .section-header {
            color: #002147;
            border-left: 6px solid #FFB300;
            padding-left: 15px;
            margin: 40px 0 20px 0;
            font-weight: 800;
            text-transform: uppercase;
            font-size: 24px;
        }
        
        .card-box {
            background: white;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #eee;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            height: 100%;
        }

        /* 5. LOGO ĐỐI TÁC */
        .partner-img {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80px;
            filter: grayscale(100%);
            opacity: 0.6;
            transition: 0.3s;
        }
        .partner-img:hover { filter: grayscale(0%); opacity: 1; }
        
        hr { margin: 0 0 30px 0; border-color: #eee; }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown("""
        <div class="top-info">
            <div class="top-inner">
                <span>📧 Email: contact@silvershield.vn | 📞 Hotline: 156</span>
                <span>🇻🇳 HỘI THI AI YOUNG GURU 2026</span>
            </div>
        </div>
        <div style="height: 20px;"></div>
    """, unsafe_allow_html=True)
