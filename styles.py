import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. CẤU HÌNH CHUNG --- */
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

        /* --- 2. TOPBAR & MARQUEE --- */
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
        
        .marquee-strip {
            background: white;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            border-bottom: 1px solid #eee;
            overflow: hidden;
            padding: 5px 0;
        }
        .marquee-text {
            display: inline-block;
            white-space: nowrap;
            animation: marquee 25s linear infinite;
            color: #d32f2f;
            font-weight: bold;
        }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        /* --- 3. NAVBAR OLYMPIC (THANH MENU NGANG) --- */
        .olympic-navbar {
            background-color: white;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            z-index: 1000;
            border-bottom: 4px solid #d32f2f;
        }

        /* Tác động vào các nút bấm trong thanh Menu */
        .navbar-container div.stButton > button {
            background: transparent !important;
            color: #002147 !important;
            border: none !important;
            border-radius: 0px !important;
            font-weight: 800 !important;
            height: 60px !important;
            font-size: 14px !important;
            transition: 0.3s !important;
        }
        .navbar-container div.stButton > button:hover {
            background-color: #d32f2f !important;
            color: white !important;
        }

        /* --- 4. HERO BANNER & BUTTON --- */
        .hero-container {
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            height: 450px;
            background: #002147;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hero-bg-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20190220/ourmid/pngtree-technology-cool-digital-light-effect-business-background-image_6960.jpg');
            background-size: cover;
            opacity: 0.2;
        }
        
       /* Đảm bảo nội dung nằm chính giữa vùng xanh */
        .hero-content-wrapper {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 1200px;
            z-index: 20;
            display: flex;
            align-items: center;
        }

        /* Kéo nút bấm lên đè lên Banner */
        div.btn-check-now {
            display: flex;
            justify-content: flex-end; /* Căn nút sang phải cho khớp với khối chữ */
            width: 1200px;
            margin: -110px auto 50px auto !important; /* Số âm để kéo nút lên */
            padding-right: 80px;
            position: relative;
            z-index: 1001;
        }

        div.btn-check-now div.stButton > button {
            background: linear-gradient(90deg, #ff8a00, #e52e71) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 12px 40px !important;
            font-size: 18px !important;
            font-weight: 900 !important;
            border: 2px solid white !important;
        }

        /* --- 5. BANNER STRIPS & CARDS --- */
        .banner-strip { background: white; border-top: 4px solid #002147; padding: 25px; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .banner-header { color: #d32f2f; font-weight: 900; font-size: 18px; margin-bottom: 10px; }
        .rules-main-header { background: #002147; color: white; padding: 12px 20px; font-weight: bold; margin-top: 30px; text-transform: uppercase; }
        .rule-card { background: white; border: 1px solid #ddd; height: 100%; }
        .rule-header { padding: 10px; text-align: center; color: white; font-weight: bold; }
        .bg-red { background: #d32f2f; }
        .bg-green { background: #2e7d32; }
        .bg-teal { background: #00695c; }
        .footer { background: #002147; color: white; padding: 40px; text-align: center; margin-top: 50px; width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; border-top: 5px solid #d32f2f; }
        </style>
    """, unsafe_allow_html=True)

def render_header_structure():
    st.markdown('<div class="olympic-topbar"><div style="width:1200px; display:flex; justify-content:space-between; padding:0 15px;"><span>🛠️ DVT - Empire CBZ X - THPT Dương Văn Thì</span><span>🛡️ SILVERSHIELD AI</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="marquee-strip"><div class="marquee-text">📢 CHÀO MỪNG BẠN ĐẾN VỚI HỆ THỐNG SILVERSHIELD AI - PHÒNG CHỐNG LỪA ĐẢO TRỰC TUYẾN CHO NGƯỜI LỚN TUỔI! LUÔN GIỮ BÌNH TĨNH TRƯỚC MỌI TÌNH HUỐNG</div></div>', unsafe_allow_html=True)
def render_footer_structure():
    st.markdown('<div class="footer"><h2>SILVERSHIELD</h2><p>"Vì một không gian mạng an toàn"</p><p style="font-size:12px; opacity:0.6;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p></div>', unsafe_allow_html=True)
