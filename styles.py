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

        /* --- 2. HEADER 2 TẦNG (FIXED THEO MẪU) --- */
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
            border-bottom: 3px solid #d32f2f; /* Gạch chân đỏ chuẩn mẫu */
            z-index: 100;
        }

        /* --- 3. HIỆU ỨNG CHỮ CHẠY (MARQUEE) --- */
        .marquee-container {
            background: #fff;
            padding: 5px 0;
            border-bottom: 1px solid #eee;
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
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

        /* --- 4. HERO BANNER (XẾP LỚP CHUẨN ẢNH C1DE18) --- */
        .hero-bg {
            background: linear-gradient(135deg, #002147 0%, #004080 100%);
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            padding: 50px 0;
            display: flex; justify-content: center;
        }
        .hero-inner {
            width: 1200px;
            display: flex;
            gap: 20px;
            align-items: center;
            padding: 0 15px;
        }
        .banner-img-box img {
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        /* Glass box cho nút bắt đầu thi */
        .glass-box {
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            text-align: center;
        }

        /* Style nút Streamlit trong Header/Banner */
        div.stButton > button {
            font-weight: 700 !important;
            text-transform: uppercase !important;
            transition: all 0.3s;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    # TẦNG 1: TOP BAR
    st.markdown("""
        <div class="olympic-topbar">
            <div style="width:1200px; display:flex; justify-content:space-between; padding:0 15px;">
                <span>🛠️ Phát triển: <b>DVT - Empire CBZ X - THPT Dương Văn Thì</b></span>
                <span>📍 Vị trí: <b>SILVERSHIELD</b></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # TẦNG 2: NAVBAR (Sử dụng columns để đặt logo và menu)
    st.markdown('<div class="olympic-navbar">', unsafe_allow_html=True)
    nav_col1, nav_col2 = st.columns([1, 4])
    with nav_col1:
        st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=50)
    with nav_col2:
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.button("Trang chủ", key="nav_home")
        m2.button("Giới thiệu", key="nav_intro")
        m3.button("Tin tức", key="nav_news")
        m4.button("Vệ sĩ AI", key="nav_ai")
        m5.button("Liên hệ", key="nav_contact")
    st.markdown('</div>', unsafe_allow_html=True)

    # CHỮ CHẠY
    st.markdown("""
        <div class="marquee-container">
            <div class="marquee-text">
                📢 CHÀO MỪNG BẠN ĐẾN VỚI HỆ THỐNG SILVERSHIELD AI - BẢO VỆ NGƯỜI CAO TUỔI TRÊN KHÔNG GIAN MẠNG. HÃY CẨN THẬN VỚI CÁC CUỘC GỌI LẠ VÀ LINK GIẢ MẠO!
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_hero_banner():
    # KHỐI BANNER CHÍNH
    st.markdown('<div class="hero-bg"><div class="hero-inner">', unsafe_allow_html=True)
    
    col_banner, col_action = st.columns([2.5, 1])
    
    with col_banner:
        # Ảnh banner chính (giống ảnh c1d736)
        st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True)
        
    with col_action:
        st.markdown("""
            <div class="glass-box">
                <h3 style="color:white; margin-bottom:10px;">Bắt đầu thi</h3>
                <p style="font-size:13px; opacity:0.9; margin-bottom:20px;">
                    Vui lòng nhấn nút bên dưới để tham gia hệ thống kiểm tra an ninh mạng.
                </p>
            </div>
        """, unsafe_allow_html=True)
        # Nút kiểm tra ngay (Dùng style gradient như yêu cầu của bạn)
        if st.button("🚀 KIỂM TRA NGAY", use_container_width=True, type="primary"):
            st.switch_page("pages/ai_check.py") # Hoặc logic của bạn

    st.markdown('</div></div>', unsafe_allow_html=True)

# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    st.set_page_config(layout="wide", page_title="SilverShield AI")
    apply_styles()
    
    # Render Header & Banner
    render_header()
    render_hero_banner()
    
    # Thêm các phần Section khác của bạn ở dưới này...
    st.markdown('<div class="news-header-bar">TIN MỚI NHẤT</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
