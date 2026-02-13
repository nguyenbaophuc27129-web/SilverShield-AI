import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. CẤU HÌNH KHUNG MÀN HÌNH CHUẨN 1200PX --- */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f6f9;
            color: #333;
        }
        
        .block-container {
            max-width: 1200px !important;
            padding-top: 0rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER 2 TẦNG (OLYMPIC STYLE) --- */
        .olympic-topbar {
            background-color: #002147;
            color: white;
            padding: 8px 0;
            font-size: 13px;
            font-weight: 500;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            display: flex; justify-content: center;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .olympic-navbar {
            background-color: white;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            display: flex; justify-content: center;
            padding: 10px 0;
            z-index: 100;
            border-bottom: 3px solid #d32f2f;
        }

        /* --- HIỆU ỨNG CHỮ CHẠY --- */
        .marquee-strip {
            background: white;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            border-bottom: 1px solid #eee;
            padding: 5px 0;
            overflow: hidden;
        }
        .marquee-text {
            display: inline-block;
            white-space: nowrap;
            animation: marquee 25s linear infinite;
            color: #d32f2f;
            font-weight: 500;
            font-size: 14px;
        }
        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }

        div.stButton > button {
            background: transparent !important;
            color: #002147 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            padding: 10px 20px !important;
            transition: all 0.3s;
        }
        div.stButton > button:hover {
            background-color: #f0f4f8 !important;
            color: #d32f2f !important;
        }
        
        /* --- 3. HERO BANNER (ĐÃ FIX LỖI BANNER NẰM DƯỚI) --- */
        .hero-container {
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            min-height: 400px; /* Cố định chiều cao nền */
            background: linear-gradient(135deg, #002147 0%, #004080 100%);
            z-index: 1;
            margin-bottom: 0px;
        }
        .hero-bg-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://img.freepik.com/free-vector/dark-blue-technology-background_23-2148443372.jpg');
            background-size: cover;
            opacity: 0.2;
            z-index: 2;
        }

        /* Lớp trung gian để kéo cái box lên trên nền */
        .glass-box {
            background: rgba(0, 0, 0, 0.7) !important;
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.5);
            max-width: 500px;
            margin: -320px auto 100px auto !important; /* KÉO LÊN TRÊN NỀN 320PX */
            position: relative;
            z-index: 99; /* Đảm bảo nổi lên trên cùng */
        }
        
        .btn-check-now button {
            background: linear-gradient(to right, #00c6ff, #0072ff) !important;
            color: white !important;
            border-radius: 50px !important;
            border: 2px solid white !important;
            padding: 12px 30px !important;
            font-size: 18px !important;
        }

        /* --- 4. CÁC KHỐI KHÁC --- */
        .banner-strip { background: white; border: 1px solid #e0e0e0; padding: 30px; text-align: center; height: 100%; }
        .banner-header { color: #d32f2f; font-weight: 700; font-size: 20px; text-transform: uppercase; margin-bottom: 15px; }
        .banner-divider { height: 1px; background-color: #e0e0e0; width: 50px; margin: 0 auto 15px auto; }
        .rules-main-header { background-color: #002147; color: white; padding: 15px 20px; font-size: 18px; font-weight: 700; text-transform: uppercase; margin-top: 40px; display: flex; align-items: center; gap: 10px; }
        .rule-card { background: white; border: 1px solid #ddd; height: 100%; }
        .rule-header { padding: 15px; text-align: center; color: white; font-weight: bold; font-size: 18px; text-transform: uppercase; }
        .bg-red { background-color: #e53935; }
        .bg-green { background-color: #43a047; }
        .bg-teal { background-color: #00897b; }
        .rule-body { padding: 20px; font-size: 14px; line-height: 1.8; }
        .rule-item { border-bottom: 1px solid #eee; padding: 5px 0; }
        .news-header-bar { background-color: #0044cc; border-top: 3px solid #d32f2f; color: white; text-align: center; padding: 10px; font-weight: 700; font-size: 20px; margin-top: 40px; margin-bottom: 20px; }
        .news-card { background: white; border: 1px solid #eee; margin-bottom: 15px; transition: 0.3s; }
        .footer { background-color: #002147; color: white; padding: 40px 0; text-align: center; border-top: 5px solid #d32f2f; margin-top: 50px; width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; }
        </style>
    """, unsafe_allow_html=True)

def render_header_structure():
    # TẦNG 1: TOP BAR
    st.markdown("""
        <div class="olympic-topbar">
            <div style="width:1200px; display:flex; justify-content:space-between; padding:0 15px;">
                <span>🛠️ Phát triển và xây dựng bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></span>
                <span>🛡️ <b>SILVERSHIELD</b></span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # TẦNG CHỮ CHẠY
    st.markdown("""
        <div class="marquee-strip">
            <div class="marquee-text">
                📢 CHÀO MỪNG BẠN ĐẾN VỚI HỆ THỐNG SILVERSHIELD AI - PHÒNG CHỐNG LỪA ĐẢO TRỰC TUYẾN. HÃY CẨN THẬN VỚI CÁC YÊU CẦU CHUYỂN TIỀN VÀ CÀI ĐẶT ỨNG DỤNG LẠ!
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer_structure():
    st.markdown("""
        <div class="footer">
            <h2 style="margin:0;">SILVERSHIELD</h2>
            <p style="opacity:0.8; margin-top:5px;">"Vì một không gian mạng an toàn"</p>
            <div style="border-top:1px solid rgba(255,255,255,0.2); width:200px; margin:20px auto;"></div>
            <p style="font-size:13px;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
        </div>
    """, unsafe_allow_html=True)
