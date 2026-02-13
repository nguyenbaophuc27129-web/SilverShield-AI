import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. CẤU HÌNH KHUNG MÀN HÌNH CHUẨN --- */
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

        /* --- 2. HEADER OLYMPIC --- */
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
        
        /* --- CHỮ CHẠY --- */
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

        /* --- 3. HERO BANNER CHUẨN (SỬ DỤNG ABSOLUTE POSITION) --- */
        .hero-container {
            width: 100vw;
            position: relative; /* Quan trọng để con cái định vị theo nó */
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            height: 500px; /* Chiều cao cố định */
            background: linear-gradient(135deg, #002147 0%, #004080 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden; /* Cắt bỏ phần thừa */
        }
        
        .hero-bg-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://img.freepik.com/free-vector/dark-blue-technology-background_23-2148443372.jpg');
            background-size: cover;
            opacity: 0.3;
            z-index: 1;
        }

        /* KHỐI GLASS BOX (Định vị tuyệt đối ở giữa) */
        .glass-box {
            position: absolute;
            top: 45%; /* Đẩy xuống giữa màn hình */
            left: 50%;
            transform: translate(-50%, -50%); /* Căn giữa hoàn hảo */
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            padding: 40px 60px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            text-align: center;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            z-index: 10; /* Nằm trên nền */
            min-width: 400px;
        }

        /* --- 4. XỬ LÝ NÚT BẤM (QUAN TRỌNG NHẤT) --- */
        /* Kéo nút bấm bay lên đè vào banner */
        div.stButton {
            position: relative;
            z-index: 999; /* Luôn nổi lên trên cùng */
            text-align: center;
            margin-top: -110px !important; /* KÉO NÚT LÊN 110PX */
        }

        div.stButton > button {
            background: linear-gradient(to right, #00c6ff, #0072ff) !important;
            color: white !important;
            border-radius: 50px !important;
            border: 2px solid white !important;
            padding: 12px 40px !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3) !important;
            transition: all 0.3s ease;
        }
        
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 25px rgba(0,0,0,0.4) !important;
            background: linear-gradient(to right, #0072ff, #00c6ff) !important;
        }
        
        div.stButton > button:active {
            color: white !important;
            border-color: white !important;
        }

        /* --- 5. FOOTER VÀ CÁC THÀNH PHẦN KHÁC --- */
        .footer { 
            background-color: #002147; 
            color: white; 
            padding: 40px 0; 
            text-align: center; 
            border-top: 5px solid #d32f2f; 
            margin-top: 50px; 
            width: 100vw; 
            position: relative; 
            left: 50%; right: 50%; 
            margin-left: -50vw; margin-right: -50vw; 
        }
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
