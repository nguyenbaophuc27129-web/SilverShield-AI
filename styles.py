import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. GLOBAL & LAYOUT --- */
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif; /* Font chữ rõ ràng, mạnh mẽ */
            background-color: #f0f2f5; /* Nền xám nhạt */
        }
        .block-container {
            max-width: 1200px !important;
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER & MENU --- */
        .top-header {
            background-color: #0d2a4f; /* Màu xanh Navy đậm */
            color: white;
            padding: 10px 0;
            font-size: 14px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 9999;
            border-bottom: 3px solid #FFB300;
            display: flex;
            justify-content: center;
        }
        .header-content {
            width: 1200px;
            display: flex;
            justify-content: space-between;
            padding: 0 15px;
        }
        .nav-bar {
            background: white;
            padding: 15px 0;
            margin-top: 30px; /* Né header */
            border: 1px solid #ddd; /* Viền rõ ràng */
            box-shadow: none; /* Bỏ đổ bóng */
        }
        div.stButton > button {
            background-color: transparent !important;
            color: #0d2a4f !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            border-radius: 0 !important; /* KHÔNG BO GÓC */
            padding: 10px 20px !important;
        }
        div.stButton > button:hover {
            color: #D32F2F !important;
            background-color: #f0f2f5 !important;
        }

        /* --- 3. CONTENT BLOCKS --- */
        .section-title {
            color: #0d2a4f;
            font-weight: 700;
            font-size: 22px;
            text-transform: uppercase;
            border-left: 5px solid #D32F2F; /* Vạch đỏ bên trái */
            padding-left: 15px;
            margin: 30px 0 20px 0;
        }
        /* Đây là class quan trọng nhất để mọi thứ vuông vức */
        .info-card {
            background: white;
            padding: 20px;
            border-radius: 0 !important; /* KHÔNG BO GÓC */
            border: 1px solid #ccc !important; /* Viền xám rõ ràng */
            box-shadow: none !important; /* Bỏ đổ bóng */
            height: 100%;
        }

        /* --- 4. FOOTER --- */
        .footer {
            background-color: #0d2a4f;
            color: white;
            padding: 30px 0;
            margin-top: 40px;
            border-top: 5px solid #FFB300;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
        <div class="top-header">
            <div class="header-content">
                <div>🛠️ Phát triển bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></div>
                <div style="font-weight:bold;">🛡️ SILVERSHIELD</div>
            </div>
        </div>
        <div style="height: 40px;"></div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="footer">
            <h3 style="margin:0;">SILVERSHIELD</h3>
            <p style="font-style: italic; margin-top: 5px;">"Vì một không gian mạng an toàn"</p>
            <p style="font-size: 13px; margin-top: 20px;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
        </div>
    """, unsafe_allow_html=True)
