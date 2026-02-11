import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f4f7f9; }

        /* Header Navy Blue xịn */
        .header-bar {
            background-color: #002147;
            padding: 15px 50px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 5px solid #FFB300;
            margin: -6rem -5rem 2rem -5rem;
        }

        /* Khung nội dung trắng */
        .content-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-top: 5px solid #002147;
            margin-bottom: 25px;
        }

        /* Nút bấm đỏ Gold */
        .stButton button {
            background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%) !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
            font-weight: bold !important;
            height: 3em;
            width: 100%;
        }

        /* Thẻ tin tức có link */
        .news-card {
            border-left: 5px solid #FFB300;
            background: #fff;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 5px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
        .news-link {
            color: #002147;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2rem;
        }
        .news-link:hover { color: #D32F2F; }
        </style>
    """, unsafe_allow_html=True)

def header_component():
    st.markdown("""
        <div class="header-bar">
            <div style="font-size: 14px;">🛡️ HỆ THỐNG BẢO VỆ NGƯỜI CAO TUỔI TRÊN KHÔNG GIAN SỐ</div>
            <div style="font-size: 14px;">DỰ ÁN DỰ THI: <b>SILVERSHIELD</b></div>
        </div>
    """, unsafe_allow_html=True)
