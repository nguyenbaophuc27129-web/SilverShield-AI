import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. CĂN CHỈNH KHUNG NHÌN CHUẨN OLYMPIC (1200px) */
        .block-container {
            max-width: 1200px !important;
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        
        /* ẨN GIAO DIỆN MẶC ĐỊNH */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
        .stApp { background-color: #f4f7f9; }

        /* 2. TOP HEADER (MÀU XANH ĐẬM) */
        .top-header {
            background-color: #002147;
            color: white;
            padding: 10px 0;
            font-size: 14px;
            font-weight: 500;
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

        /* 3. THANH MENU (NAVIGATION BAR) */
        .nav-bar {
            background: white;
            padding: 15px 0;
            margin-top: 30px; /* Né cái header fixed */
            border-radius: 0 0 10px 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
        }
        
        /* Biến nút bấm thành Text Link sang trọng */
        div.stButton > button {
            background-color: transparent !important;
            color: #002147 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            border-radius: 0 !important;
            padding: 10px 20px !important;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            color: #D32F2F !important;
            background-color: #f0f2f5 !important;
            border-bottom: 2px solid #D32F2F !important;
        }
        /* Nút đang được chọn (Active) */
        div.stButton > button:focus {
            color: #D32F2F !important;
            border-bottom: 2px solid #D32F2F !important;
        }

        /* 4. ĐỊNH DẠNG KHỐI NỘI DUNG (CARD) */
        .section-title {
            color: #002147;
            font-weight: 800;
            font-size: 24px;
            text-transform: uppercase;
            border-left: 6px solid #FFB300;
            padding-left: 15px;
            margin: 30px 0 20px 0;
            background: linear-gradient(90deg, #e3f2fd 0%, transparent 100%);
            padding-top: 5px;
            padding-bottom: 5px;
        }

        .info-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border: 1px solid #eee;
            height: 100%;
            transition: transform 0.3s;
        }
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
            border-color: #FFB300;
        }

        /* 5. FOOTER */
        .footer {
            background-color: #002147;
            color: white;
            padding: 40px 0;
            margin-top: 50px;
            border-top: 5px solid #D32F2F;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
        <div class="top-header">
            <div class="header-content">
                <div>🛠️ Phát triển và xây dựng bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></div>
                <div style="font-weight:bold; letter-spacing: 1px;">🛡️ SILVERSHIELD</div>
            </div>
        </div>
        <div style="height: 40px;"></div> <!-- Khoảng trống để không bị che nội dung -->
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="footer">
            <h2 style="margin:0; font-size: 28px;">SILVERSHIELD</h2>
            <p style="font-size: 16px; font-style: italic; margin-top: 10px;">"Vì một không gian mạng an toàn"</p>
            <hr style="width: 200px; margin: 20px auto; border-color: #FFB300;">
            <p style="font-size: 14px;">© 2026 Bản quyền thuộc về <b>Đội ngũ DVT - Empire CBZ X</b></p>
        </div>
    """, unsafe_allow_html=True)
