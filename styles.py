import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* IMPORT FONT ROBOTO */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

        /* 1. CẤU HÌNH CHUNG */
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5; /* Màu nền xám nhạt hiện đại */
        }
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        
        /* ẨN GIAO DIỆN MẶC ĐỊNH */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* 2. TOP BAR (Màu xanh Deep Blue #003366) */
        .top-bar-container {
            background-color: #003366;
            color: white;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 8px 0;
            border-bottom: 3px solid #ffcc00; /* Viền vàng Gold */
        }
        .top-bar-content {
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
