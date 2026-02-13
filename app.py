import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
styles.apply_styles()
styles.render_header_structure()
try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR (MENU TRẮNG) ---
st.markdown('<div class="olympic-navbar"><div style="width:1200px;">', unsafe_allow_html=True)
c_spacer, c_menu = st.columns([2, 8]) # Cột 1 để trống chừa chỗ cho Logo treo

with c_menu:
    # Menu nằm lệch phải
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("🏠 TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("👥 GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("📰 TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("🛡️ VỆ SĨ AI", use_container_width=True): st.session_state['page'] = 'VỆ SĨ AI'

st.markdown('</div></div>', unsafe_allow_html=True)

# --- 3. DÒNG CHỮ CHẠY (MARQUEE) ---
st.markdown("""
    <div class="marquee-container">
        <div class="marquee-content">
            📢 SILVERSHIELD - AI: "Vì an toàn trên không gian mạng" &nbsp;&nbsp;&nbsp;&nbsp; 🚀 CẢNH BÁO: Cẩn trọng với các cuộc gọi giả danh cơ quan chức năng &nbsp;&nbsp;&nbsp;&nbsp; 🛡️ HÃY KIỂM TRA TIN NHẮN NGHI NGỜ NGAY HÔM NAY!
        </div>
    </div>
""", unsafe_allow_html=True)


# ==================== TRANG CHỦ (BANNER + CONTENT) ====================
if st.session_state['page'] == 'TRANG CHỦ':
    
    # --- HERO BANNER (KẾT CẤU PHỨC TẠP: NỀN + LOGO TREO + 2 CỘT) ---
    # Container bao quanh toàn bộ banner
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    
    # 1. LOGO TREO (Nằm đè lên ranh giới Menu và Banner)
    # Bạn thay link logo TRÒN của bạn vào đây
    st.markdown("""
        <div class="hanging-logo">
            <img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png">
        </div>
        <div class="stem-watermark">STEM</div>
    """, unsafe_allow_html=True)

    # 2. CHIA CỘT 70% - 30% (Sử dụng code HTML bên trong để kiểm soát layout tốt hơn st.columns)
    # Vì st.columns sẽ bị padding của Streamlit làm hỏng layout background
    # Nên ta dùng HTML + Streamlit Button chèn vào sau
    
    col_hero_L, col_hero_R = st.columns([7, 3])
    
    with col_hero_L:
        # Cột Trái: Ảnh Banner (Trong suốt/Gradient)
        # Thay link banner chữ/hình minh họa vào đây
        st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True)
        
    with col_hero_R:
        # Cột Phải: Glass Box Vệ Sĩ Silver
        st.markdown("""
        <div class="glass-box-container">
            <div class="glass-title">VỆ SĨ SILVER</div>
            <p style="color:#ddd; font-size:14px; margin-bottom:25px;">Hệ thống AI bảo vệ người cao tuổi</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Nút bấm (Hack vị trí để nó chui vào cái hộp ở trên)
        # CSS margin-top âm để đẩy nút lên
        st.markdown('<div style="margin-top: -80px; position: relative; z-index: 20; padding: 0 40px;" class="btn-check-now">', unsafe_allow_html=True)
        if st.button("🌐 KIỂM TRA NGAY", use_container_width=True):
            st.session_state['page'] = 'VỆ SĨ AI'
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Đóng hero-container


    # --- PHẦN NỘI DUNG DƯỚI (GIỮ NGUYÊN NHƯ CŨ - CHỈ BỌC CONTAINER) ---
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

    # KHỐI: VỀ ỨNG DỤNG & HƯỚNG DẪN
    st.markdown("<br>", unsafe_allow_html=True)
    c_intro, c_guide = st.columns(2, gap="large")
    with c_intro:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">VỀ ỨNG DỤNG SILVERSHIELDAI</div>
            <div class="banner-divider"></div>
            <p style="text-align:justify; color:#555;">
                SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c_guide:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">HƯỚNG DẪN SỬ DỤNG SILVERSHIELDAI</div>
            <div class="banner-divider"></div>
            <ul style="text-align:left; color:#555; padding-left:20px;">
                <li>Bước 1: Truy cập mục "Vệ sĩ AI".</li>
                <li>Bước 2: Nhập văn bản hoặc tải ảnh cần kiểm tra.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # KHỐI: QUY TẮC AN TOÀN
    st.markdown("""
    <div class="rules-main-header">
        <img src="https://cdn-icons-png.flaticon.com/512/2092/2092663.png" width="30" style="filter: brightness(0) invert(1);">
        CÁC QUY TẮC AN TOÀN TRÊN KHÔNG GIAN MẠNG
    </div>
    """, unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3, gap="medium")
    with r1:
        st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div class="rule-body"><div class="rule-item">1. KHÔNG chuyển tiền</div><div class="rule-item">2. KHÔNG bấm link lạ</div></div></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div class="rule-body"><div class="rule-item">1. NÊN gọi xác thực</div><div class="rule-item">2. NÊN hỏi con cháu</div></div></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý</div><div class="rule-body"><div class="rule-item">1. Bình tĩnh xử lý</div><div class="rule-item">2. Cập nhật tin tức</div></div></div>', unsafe_allow_html=True)

    # KHỐI: TIN TỨC
    st.markdown('<div class="news-header-bar">TIN TỨC</div>', unsafe_allow_html=True)
    news_data = [
        {"title": "🚀 Cảnh báo thủ đoạn lừa đảo 'Con đang cấp cứu'", "img": "https://img.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_138676-2387.jpg"},
        {"title": "💡 5 Cách nhận biết website giả mạo ngân hàng", "img": "https://img.freepik.com/free-vector/cyber-security-concept_23-2148532223.jpg"},
        {"title": "🔥 Giả danh công an gọi video call: Chiêu trò mới", "img": "https://img.freepik.com/free-vector/scam-alert-background_23-2148079148.jpg"},
        {"title": "🚀 Bộ Công an ra mắt cẩm nang phòng chống tội phạm", "img": "https://img.freepik.com/free-vector/internet-security-concept_23-2148532222.jpg"},
        {"title": "💡 Deepfake là gì? Tại sao người già dễ bị lừa?", "img": "https://img.freepik.com/free-vector/cyber-attack-concept-illustration_114360-1934.jpg"},
        {"title": "🔥 Hướng dẫn cài đặt sinh trắc học an toàn", "img": "https://img.freepik.com/free-vector/biometric-security-concept_23-2148532221.jpg"},
    ]
    for i in range(0, 6, 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < 6:
                news = news_data[i+j]
                with cols[j]:
                    if st.button(f"btn_news_{i+j}", key=f"k_news_{i+j}", label_visibility="collapsed"): st.session_state['page'] = 'TIN TỨC'
                    st.markdown(f'<div class="news-card"><img src="{news["img"]}" class="news-thumb"><div class="news-content"><div class="news-title">{news["title"]}</div></div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # End content wrapper


# ==================== CÁC TRANG CON (GIỮ NGUYÊN) ====================
elif st.session_state['page'] == 'VỆ SĨ AI':
    st.markdown('<div class="content-wrapper"><div class="rules-main-header">🛡️ TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        txt = st.text_area("Nhập nội dung cần kiểm tra:", height=200)
        img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
        if st.button("PHÂN TÍCH NGAY", type="primary", use_container_width=True):
            if txt or img:
                with st.spinner("AI đang quét dữ liệu..."):
                    i = Image.open(img) if img else None
                    st.session_state['res'] = logic.analyze_content(model, txt, i)
    with c2:
        if 'res' in st.session_state:
            st.success("KẾT QUẢ PHÂN TÍCH")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("Kết quả sẽ hiển thị tại đây.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="content-wrapper"><div class="news-header-bar">TIN TỨC AN NINH MẠNG</div><p>Danh sách tin tức chi tiết...</p></div>', unsafe_allow_html=True)

elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="content-wrapper"><div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN</div><h3>DVT - EMPIRE CBZ X</h3></div>', unsafe_allow_html=True)

# --- FOOTER ---
styles.render_footer_structure()
