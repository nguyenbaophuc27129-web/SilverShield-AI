import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. GLOBAL & FONT --- */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f4f4; /* Nền xám nhạt toàn trang */
            color: #333;
        }
        
        /* Căn giữa trang web chuẩn 1200px */
        .block-container {
            max-width: 1200px !important;
            padding: 0 !important;
            margin: 0 auto !important;
            background-color: white; /* Nội dung nằm trên nền trắng */
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        
        /* ẨN GIAO DIỆN MẶC ĐỊNH */
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER SYSTEM --- */
        
        /* Top Bar (Xanh đậm trên cùng) */
        .top-bar {
            background-color: #003366; /* Deep Navy Blue */
            color: white;
            padding: 8px 30px;
            font-size: 12px;
            font-weight: 500;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Navbar (Thanh menu trắng) */
        .navbar-container {
            background: white;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Menu nằm bên phải */
            padding-right: 30px;
            position: relative; /* Để định vị logo */
            border-bottom: 1px solid #ddd;
        }

        /* Logo treo (Hanging Logo) */
        .hanging-logo {
            position: absolute;
            top: 10px; /* Treo từ trên xuống */
            left: 50px;
            z-index: 1000; /* Nổi lên trên tất cả */
            background: white;
            border-radius: 50%;
            padding: 5px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            width: 120px;
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hanging-logo img { width: 100%; border-radius: 50%; }

        /* Style cho nút Menu */
        div.stButton > button {
            background-color: transparent !important;
            color: #333 !important;
            border: none !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
            margin: 0 5px !important;
            border-radius: 0 !important;
            padding: 10px 15px !important;
        }
        div.stButton > button:hover {
            color: #003366 !important;
            background-color: #f0f8ff !important;
        }

        /* Marquee (Dòng chữ chạy) */
        .marquee-container {
            background-color: #002147;
            color: white;
            padding: 8px 0;
            white-space: nowrap;
            overflow: hidden;
            font-size: 13px;
            font-weight: bold;
            border-top: 3px solid #FFCC00; /* Viền vàng ngăn cách */
        }

        /* --- 3. HERO BANNER --- */
        .hero-section {
            background: linear-gradient(180deg, #003366 0%, #001a33 100%);
            /* Giả lập họa tiết chìm */
            background-image: radial-gradient(circle at 10% 20%, rgba(255,255,255,0.1) 0%, transparent 20%),
                              radial-gradient(circle at 90% 80%, rgba(255,255,255,0.1) 0%, transparent 20%);
            min-height: 500px;
            position: relative;
            display: flex;
            align-items: center;
            padding: 40px;
            overflow: hidden;
        }
        
        /* Chữ STEM chìm */
        .bg-text-stem {
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%) rotate(-90deg);
            font-size: 150px;
            font-weight: 900;
            color: rgba(255,255,255,0.05);
            z-index: 0;
            pointer-events: none;
        }

        /* Khối Glassmorphism bên phải */
        .glass-box {
            background: rgba(0, 30, 60, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 10px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            color: white;
            z-index: 10;
        }
        
        /* Nút kiểm tra ngay */
        .btn-check-now button {
            background: linear-gradient(90deg, #007bff, #00c6ff) !important;
            color: white !important;
            border: none !important;
            padding: 12px 30px !important;
            border-radius: 50px !important;
            font-weight: bold !important;
            font-size: 16px !important;
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.4) !important;
            width: 100% !important;
        }
        .btn-check-now button:hover { transform: translateY(-2px); }

        /* --- 4. CONTENT SECTIONS --- */
        
        /* Tiêu đề Đỏ giữa trang (Intro & Hướng dẫn) */
        .header-red-strip {
            text-align: center;
            border-bottom: 1px solid #E0E0E0;
            margin-bottom: 20px;
            padding-bottom: 10px;
        }
        .header-red-text {
            color: #D32F2F;
            font-weight: 700;
            font-size: 24px;
            text-transform: uppercase;
            background: white;
            padding: 0 20px;
            position: relative;
            top: 22px; /* Đè lên đường kẻ */
        }

        /* Khối Quy tắc (Màu xanh đậm) */
        .rules-header {
            background-color: #003366;
            color: white;
            padding: 15px 20px;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 18px;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 40px;
        }
        
        /* Thẻ trạng thái (Rules Card) */
        .rule-card-header {
            padding: 10px;
            text-align: center;
            font-weight: bold;
            color: white;
            text-transform: uppercase;
        }
        .bg-red { background-color: #e57373; }
        .bg-green { background-color: #81c784; }
        .bg-teal { background-color: #26a69a; }
        
        .rule-card-body {
            background: white;
            border: 1px solid #ddd;
            padding: 15px;
            min-height: 200px;
        }
        .rule-item {
            border-bottom: 1px solid #eee;
            padding: 8px 0;
            font-size: 14px;
        }

        /* --- 5. NEWS SECTION --- */
        .news-header-bar {
            background-color: #003366; /* Royal Blue */
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 50px;
            margin-bottom: 30px;
            border-top: 3px solid #D32F2F;
        }
        .news-header-text {
            color: white;
            font-weight: 700;
            font-size: 20px;
            text-transform: uppercase;
            font-family: 'Times New Roman', serif; /* Font có chân trang trọng */
        }
        
        .news-card {
            display: flex;
            background: white;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
            transition: 0.3s;
            cursor: pointer;
            height: 110px;
            overflow: hidden;
        }
        .news-card:hover { box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-color: #003366; }
        .news-thumb {
            width: 40%;
            background-size: cover;
            background-position: center;
        }
        .news-content {
            width: 60%;
            padding: 10px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .news-title {
            color: #003366;
            font-weight: 700;
            font-size: 14px;
            line-height: 1.4;
            text-transform: uppercase;
            margin-bottom: 5px;
        }

        /* --- 6. FOOTER --- */
        .footer {
            background-color: #003366;
            color: white;
            padding: 40px 20px;
            text-align: center;
            border-top: 5px solid #FFCC00;
            margin-top: 60px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_top_bar():
    st.markdown("""
        <div class="top-bar">
            <div>🛠️ Phát triển và xây dựng bởi <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></div>
            <div style="font-weight:bold;">🛡️ SILVERSHIELD</div>
        </div>
    """, unsafe_allow_html=True)

def render_hanging_logo():
    # Logo treo lơ lửng - Chỗ này bạn dán link logo vào
    st.markdown("""
        <div class="hanging-logo">
            <img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" alt="Logo">
        </div>
    """, unsafe_allow_html=True)

def render_marquee():
    st.markdown("""
        <div class="marquee-container">
            <marquee scrollamount="8">
                🔔 SILVERSHIELD - AI: "Vì an toàn trên không gian mạng" — Cập nhật các thủ đoạn lừa đảo mới nhất 2026 — Hotline hỗ trợ: 156
            </marquee>
        </div>
    """, unsafe_allow_html=True)
