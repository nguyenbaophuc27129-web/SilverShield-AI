import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        .stApp { background-color: #ffffff; }
        .block-container { padding: 0rem; max-width: 100%; }
        .top-info {
            background-color: #002147;
            color: white;
            padding: 10px 10%;
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            border-bottom: 3px solid #FFB300;
        }
        .main-banner {
            width: 100%;
            height: 350px;
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
        }
        .section-container { padding: 40px 10%; }
        .card-pro {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            border-top: 5px solid #002147;
            margin-bottom: 30px;
        }
        div.stButton > button {
            background-color: transparent !important;
            color: #333 !important;
            border: none !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
        }
        div.stButton > button:hover { color: #007bff !important; }
        .btn-check-ai button {
            background: #d32f2f !important;
            color: white !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
        }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown(f"""
        <div class="top-info">
            <div>🚀 Phát triển và xây dựng bởi <b>DVT-Empire X CBZ - Trường THPT Dương Văn Thì</b></div>
            <div>🛡️ <b>Silvershield - Vì an toàn không gian mạng</b></div>
        </div>
    """, unsafe_allow_html=True)
