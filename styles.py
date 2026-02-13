import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. GLOBAL SETUP --- */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f6f9;
            color: #333;
        }
        
        .block-container {
            max-width: 100% !important; /* Full width để xử lý banner */
            padding: 0 !important;
            margin: 0 !important;
        }
        
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER 2 TẦNG --- */
        .olympic-topbar {
            background-color: #002147;
            color: white;
            padding: 8px 0;
            font-size: 13px;
            font-weight: 500;
            display: flex; justify-content: center;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .olympic-navbar {
            background-color: white;
            display: flex; justify-content: center;
            padding: 10px 0;
            position: relative;
            z-index: 100; /* Thấp hơn logo treo */
        }

        /* Nút menu */
        div.stButton > button {
            background: transparent !important;
            color: #002147 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 15px !important;
            padding: 10px 20px !important;
            border-radius: 4px !important;
            transition: all 0.3s;
        }
        div.stButton > button:hover {
            color: #d32f2f !important;
            background-color: #f0f4f8 !important;
        }

        /* --- 3. MARQUEE (DÒNG CHỮ CHẠY) --- */
        .marquee-container {
            background-color: #003366; /* Xanh đậm hơn banner */
            color: white;
            overflow: hidden;
            white-space: nowrap;
            padding: 8px 0;
            font-size: 14px;
            font-weight: bold;
            border-bottom: 1px solid #004080;
            position: relative;
            z-index: 90;
        }
        .marquee-content {
            display: inline-block;
            animation: scroll-left 20s linear infinite;
            padding-left: 100%;
        }
        @keyframes scroll-left {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }

        /* --- 4. HERO SECTION (BANNER CAO CẤP) --- */
        .hero-container {
            position: relative;
            height: 550px; /* Tăng chiều cao để chứa đủ nội dung */
            /* Gradient Xanh Đậm + Ảnh nền công nghệ */
            background: 
                linear-gradient(90deg, rgba(0,26,51,0.95) 0%, rgba(0,51,102,0.8) 50%, rgba(0,26,51,0.95) 100%),
                url('https://img.freepik.com/free-vector/digital-technology-background-with-abstract-wave-border_53876-117508.jpg');
            background-size: cover;
            background-position: center top;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: visible !important; /* Để logo treo không bị cắt */
        }

        /* LOGO TREO (HANGING LOGO) */
        .hanging-logo {
            position: absolute;
            top: -50px; /* Treo lên trên, đè lên thanh menu */
            left: 50%;
            transform: translateX(-380px); /* Căn chỉnh vị trí so với tâm (khoảng 20% bên trái) */
            width: 140px;
            height: 140px;
            background: white;
            border-radius: 50%;
            padding: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            z-index: 200; /* Nổi lên trên cùng */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hanging-logo img {
            width: 100%;
            height: auto;
        }

        /* BỐ CỤC 2 CỘT TRONG BANNER */
        .hero-inner {
            width: 1200px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 100%;
            padding: 0 15px;
            margin-top: 20px;
        }

        /* CỘT TRÁI: BANNER TITLE */
        .hero-left {
            width: 65%;
            color: white;
            padding-right: 20px;
        }
        .hero-left h1 {
            font-size: 48px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        .stem-watermark {
            font-size: 120px;
            font-weight: 900;
            color: rgba(255,255,255,0.05);
            position: absolute;
            left: -50px;
            top: 50px;
            z-index: 0;
            pointer-events: none;
        }

        /* CỘT PHẢI: GLASS BOX (VỆ SĨ SILVER) */
        .glass-box-container {
            width: 30%;
            background: rgba(0, 30, 60, 0.85); /* Xanh đen đậm bán trong suốt */
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            position: relative;
            z-index: 10;
        }
        .glass-title {
            color: white;
            font-size: 20px;
            font-weight: 500;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Nút 'KIỂM TRA NGAY' */
        .btn-check-now button {
            background-color: #007bff !important; /* Xanh dương tươi */
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            padding: 12px 0 !important;
            width: 100% !important;
            border-radius: 5px !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.4) !important;
            transition: 0.3s;
        }
        .btn-check-now button:hover {
            background-color: #0056b3 !important;
            transform: translateY(-2px);
        }

        /* --- 5. CÁC KHỐI CONTENT BÊN DƯỚI (GIỮ NGUYÊN) --- */
        .content-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 15px;
        }
        .banner-strip {
            background: white;
            border: 1px solid #e0e0e0;
            padding: 30px;
            text-align: center;
            height: 100%;
        }
        .banner-header {
            color: #d32f2f;
            font-weight: 700;
            font-size: 20px;
            text-transform: uppercase;
            margin-bottom: 15px;
        }
        .banner-divider {
            height: 1px;
            background-color: #e0e0e0;
            width: 50px;
            margin: 0 auto 15px auto;
        }
        .rules-main-header {
            background-color: #002147;
            color: white;
            padding: 15px 20px;
            font-size: 18px;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 40px;
            display: flex; align-items: center; gap: 10px;
        }
        .rule-card {
            background: white; border: 1px solid #ddd; height: 100%;
        }
        .rule-header {
            padding: 15px; text-align: center; color: white; font-weight: bold; font-size: 18px; text-transform: uppercase;
        }
        .bg-red { background-color: #e53935; }
        .bg-green { background-color: #43a047; }
        .bg-teal { background-color: #00897b; }
        .rule-body { padding: 20px; font-size: 14px; line-height: 1.8; }
        .rule-item { border-bottom: 1px solid #eee; padding: 5px 0; }
        
        .news-header-bar {
            background-color: #0044cc;
            border-top: 3px solid #d32f2f;
            color: white;
            text-align: center;
            padding: 10px;
            font-weight: 700;
            font-size: 20px;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .news-card {
            background: white; display: flex; border: 1px solid #eee; margin-bottom: 15px; transition: 0.3s;
        }
        .news-thumb { width: 40%; object-fit: cover; }
        .news-content { width: 60%; padding: 15px; }
        .news-title {
            color: #003366; font-weight: 700; font-size: 14px; text-transform: uppercase;
        }

        /* FOOTER */
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
                <span>🛡️ <b>Silvershield</b></span>
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
