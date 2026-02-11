import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* RESET & FIX OVERFLOW */
        * { box-sizing: border-box; }
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        .stApp { background-color: #ffffff; overflow-x: hidden; }
        .block-container { padding: 0rem !important; max-width: 100%; }

        /* TOP BAR - GỌN GÀNG */
        .top-info {
            background-color: #002147;
            color: white;
            padding: 8px 5%; /* Giảm padding để không tràn */
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            border-bottom: 3px solid #FFB300;
            width: 100%;
        }

        /* BANNER - FIX CHIỀU CAO */
        .main-banner {
            width: 100%;
            height: 300px;
            background: linear-gradient(rgba(0,33,71,0.6), rgba(0,33,71,0.6)), 
                        url('https://olympicenglish.vn/upload/banner-olympic-2025.png');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            flex-direction: column;
            padding: 0 20px;
        }

        /* KHUNG NỘI DUNG - FIX TRÀN */
        .section-container { 
            padding: 30px 5%; 
            width: 100%;
            margin: 0 auto;
        }
        
        .card-pro {
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            border-top: 4px solid #002147;
            margin-bottom: 20px;
            height: 100%; /* Đảm bảo các card cao bằng nhau */
        }

        /* MENU BUTTONS - SÁT NHAU HƠN */
        div.stButton > button {
            background-color: transparent !important;
            color: #333 !important;
            border: none !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            font-size: 13px !important;
            padding: 5px !important;
        }
        div.stButton > button:hover { color: #007bff !important; }
        
        .btn-check-ai button {
            background: #d32f2f !important;
            color: white !important;
            border-radius: 4px !important;
            padding: 8px 15px !important;
        }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown(f"""
        <div class="top-info">
            <div>🚀 <b>DVT-Empire X CBZ</b> - THPT Dương Văn Thì</div>
            <div>🛡️ <b>Silvershield</b> - Vì an toàn không gian mạng</div>
        </div>
    """, unsafe_allow_html=True)
