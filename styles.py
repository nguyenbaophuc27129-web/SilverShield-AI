import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. GLOBAL RESET & LAYOUT --- */
        html, body, [class*="css"] {
            font-family: 'Arial', sans-serif;
            background-color: #f0f2f5;
        }
        .block-container {
            max-width: 1200px !important;
            padding: 1rem 1rem 3rem 1rem !important;
            margin: 0 auto !important;
        }
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER & MENU --- */
        .top-bar {
            background-color: #0d2a4f;
            color: white;
            padding: 8px 0;
            font-size: 13px;
        }
        .nav-bar {
            background: white;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }
        div.stButton > button {
            background: transparent !important;
            color: #0d2a4f !important;
            border: none !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
        }
        div.stButton > button:hover { color: #c53030 !important; }

        /* --- 3. CONTENT STYLING --- */
        .section-header {
            color: #0d2a4f;
            font-size: 22px;
            font-weight: bold;
            border-left: 5px solid #c53030;
            padding-left: 10px;
            margin: 30px 0 15px 0;
        }
        .content-box {
            background: white;
            padding: 20px;
            border: 1px solid #ddd;
            margin-bottom: 15px;
            height: 100%;
        }
        .content-box h3 {
            color: #0d2a4f;
            font-size: 18px;
            margin-top: 0;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }

        /* --- 4. FOOTER --- */
        .footer {
            background: #0d2a4f;
            color: white;
            padding: 30px 0;
            margin-top: 40px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
        <div style="background-color:#0d2a4f; width:100vw; position:relative; left:50%; right:50%; margin-left:-50vw; margin-right:-50vw;">
            <div class="block-container top-bar">
                <div style="display:flex; justify-content:space-between;">
                    <span>Phát triển bởi: DVT-Empire CBZ X</span>
                    <span>SILVERSHIELD</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
