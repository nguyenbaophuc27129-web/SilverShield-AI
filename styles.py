import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f6f9;
        }
        
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            margin: 0 auto !important;
        }
        
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- NAVBAR CHUẨN --- */
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
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex; justify-content: center;
            padding: 5px 0;
            z-index: 999;
            border-bottom: 2px solid #eee;
        }

        /* Nút menu sát nhau giống web thật */
        div.stButton > button {
            background: transparent !important;
            color: #333 !important;
            border: none !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            color: #d32f2f !important;
        }

        /* --- HERO BANNER CẢI TIẾN --- */
        .hero-container {
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            background: #0044cc url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
            padding: 40px 0;
            display: flex; justify-content: center;
        }
        
        .glass-box {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 25px;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            text-align: center;
        }

        /* --- TIN TỨC --- */
        .news-header-bar {
            background-color: #0044cc;
            color: white;
            text-align: center;
            padding: 10px;
            font-weight: 700;
            margin: 30px 0;
        }
        .news-card {
            background: white;
            border: 1px solid #eee;
            border-radius: 5px;
            overflow: hidden;
            height: 280px;
        }
        .news-thumb { width: 100%; height: 150px; object-fit: cover; }
        .news-title {
            padding: 10px;
            font-weight: bold;
            font-size: 14px;
            color: #002147;
        }

        .footer {
            background-color: #002147;
            color: white;
            padding: 30px 0;
            text-align: center;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header_structure():
    st.markdown("""
        <div class="olympic-topbar">
            <div style="width:1200px; display:flex; justify-content:space-between; padding:0 15px;">
                <span>🛠️ Phát triển bởi <b>DVT - Empire CBZ X</b></span>
                <span>📞 Hỗ trợ: 1900 xxxx</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer_structure():
    st.markdown("""
        <div class="footer">
            <p>© 2026 SilverShield AI - An toàn cho người cao tuổi</p>
        </div>
    """, unsafe_allow_html=True)
