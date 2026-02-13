import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
styles.apply_styles()
styles.render_header_structure() # Top Bar Xanh
try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR (Thanh trắng chứa Logo và Menu) ---
st.markdown('<div class="olympic-navbar"><div style="width:1200px;">', unsafe_allow_html=True)
c_logo, c_menu = st.columns([1.5, 8.5])

with c_logo:
    # Logo tròn bên trái (Thay link logo của bạn)
    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" style="height:60px; margin-top:-10px;">', unsafe_allow_html=True)

with c_menu:
    # Menu ngang phải (Trang chủ, Giới thiệu...)
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


# ==================== TRANG CHỦ (CHÍNH) ====================
if st.session_state['page'] == 'TRANG CHỦ':
    
    # --- PHẦN 1, 2, 3: BANNER CHÍNH (XẾP LỚP) ---
    st.markdown('<div class="hero-container"><div class="hero-bg-overlay"></div>', unsafe_allow_html=True)
    
    # Tạo layout 1200px bên trong nền xanh
    col_hero_1, col_hero_2 = st.columns([2.5, 1])
    
    with col_hero_1:
        # PHẦN 2: Khối Banner kích thước nhỏ hơn nằm trọn trong nền
        # Bạn thay link banner THẬT của bạn vào đây
        st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True)
        
    with col_hero_2:
        # PHẦN 3: Khối đen mờ + Nút kiểm tra
        st.markdown("""
        <div class="glass-box">
            <h2 style="color:#FFB300; margin-top:0;">VỆ SĨ SILVER</h2>
            <p style="font-size:14px; margin-bottom:20px;">Hệ thống AI bảo vệ người cao tuổi</p>
        </div>
        """, unsafe_allow_html=True)
        # Nút bấm nổi lên
        st.markdown('<div class="btn-check-now">', unsafe_allow_html=True)
        if st.button("KIỂM TRA NGAY", use_container_width=True):
            st.session_state['page'] = 'VỆ SĨ AI'
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Đóng hero-container


    # --- KHỐI: VỀ ỨNG DỤNG & HƯỚNG DẪN (BANNER STRIP) ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_intro, c_guide = st.columns(2, gap="large")
    
    with c_intro:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">VỀ ỨNG DỤNG SILVERSHIELDAI</div>
            <div class="banner-divider"></div>
            <p style="text-align:justify; color:#555;">
                SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến, 
                được thiết kế chuyên biệt cho người cao tuổi với giao diện đơn giản, dễ sử dụng.
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
                <li>Bước 3: Nhận kết quả và lời khuyên từ AI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


    # --- KHỐI: QUY TẮC AN TOÀN (3 CỘT MÀU) ---
    st.markdown("""
    <div class="rules-main-header">
        <img src="https://cdn-icons-png.flaticon.com/512/2092/2092663.png" width="30" style="filter: brightness(0) invert(1);">
        CÁC QUY TẮC AN TOÀN TRÊN KHÔNG GIAN MẠNG
    </div>
    """, unsafe_allow_html=True)
    
    r1, r2, r3 = st.columns(3, gap="medium")
    
    with r1:
        st.markdown("""
        <div class="rule-card">
            <div class="rule-header bg-red">5 KHÔNG</div>
            <div class="rule-body">
                <div class="rule-item">1. KHÔNG chuyển tiền cho người lạ</div>
                <div class="rule-item">2. KHÔNG bấm link lạ</div>
                <div class="rule-item">3. KHÔNG cung cấp mã OTP</div>
                <div class="rule-item">4. KHÔNG cài app lạ</div>
                <div class="rule-item">5. KHÔNG sợ hãi lời đe dọa</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with r2:
        st.markdown("""
        <div class="rule-card">
            <div class="rule-header bg-green">3 NÊN</div>
            <div class="rule-body">
                <div class="rule-item">1. NÊN gọi điện xác thực lại</div>
                <div class="rule-item">2. NÊN hỏi ý kiến con cháu</div>
                <div class="rule-item">3. NÊN báo cơ quan chức năng (156)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with r3:
        st.markdown("""
        <div class="rule-card">
            <div class="rule-header bg-teal">LƯU Ý QUAN TRỌNG</div>
            <div class="rule-body">
                <div class="rule-item">1. Bình tĩnh trước mọi tình huống</div>
                <div class="rule-item">2. Cập nhật tin tức thường xuyên</div>
                <div class="rule-item">3. Sử dụng SilverShield để kiểm tra</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


    # --- KHỐI: TIN TỨC (GRID 6 BÀI) ---
    st.markdown('<div class="news-header-bar">TIN TỨC</div>', unsafe_allow_html=True)
    
    # Tạo dữ liệu giả lập cho 6 bài tin
    # Bạn thay link ảnh thumbnail và tiêu đề thật vào đây
    news_data = [
        {"title": "🚀 Cảnh báo thủ đoạn lừa đảo 'Con đang cấp cứu' quay trở lại", "img": "https://img.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_138676-2387.jpg"},
        {"title": "💡 5 Cách nhận biết website giả mạo ngân hàng", "img": "https://img.freepik.com/free-vector/cyber-security-concept_23-2148532223.jpg"},
        {"title": "🔥 Giả danh công an gọi video call: Chiêu trò mới", "img": "https://img.freepik.com/free-vector/scam-alert-background_23-2148079148.jpg"},
        {"title": "🚀 Bộ Công an ra mắt cẩm nang phòng chống tội phạm mạng", "img": "https://img.freepik.com/free-vector/internet-security-concept_23-2148532222.jpg"},
        {"title": "💡 Deepfake là gì? Tại sao người già dễ bị lừa?", "img": "https://img.freepik.com/free-vector/cyber-attack-concept-illustration_114360-1934.jpg"},
        {"title": "🔥 Hướng dẫn cài đặt sinh trắc học an toàn", "img": "https://img.freepik.com/free-vector/biometric-security-concept_23-2148532221.jpg"},
    ]
    
    # Tạo lưới 3 cột x 2 hàng
    for i in range(0, 6, 3): # Vòng lặp tạo từng hàng
        cols = st.columns(3)
        for j in range(3):
            if i + j < 6:
                news = news_data[i+j]
                with cols[j]:
                    # Nút ẩn để bấm vào tin tức (giả lập link)
                    if st.button(f"news_btn_{i+j}", key=f"news_{i+j}", label_visibility="collapsed"):
                        st.session_state['page'] = 'TIN TỨC'
                    
                    # Render thẻ tin tức HTML
                    st.markdown(f"""
                    <div class="news-card">
                        <img src="{news['img']}" class="news-thumb">
                        <div class="news-content">
                            <div class="news-title">{news['title']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)


# ==================== CÁC TRANG KHÁC (GIỮ NGUYÊN CODE CŨ CỦA BẠN) ====================
elif st.session_state['page'] == 'VỆ SĨ AI':
    st.markdown('<div class="rules-main-header">🛡️ TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
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

elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="news-header-bar">TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
    st.info("Danh sách bài báo chi tiết sẽ được cập nhật tại đây...")

elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN</div>', unsafe_allow_html=True)
    st.markdown("### DVT - EMPIRE CBZ X")

# --- FOOTER ---
styles.render_footer_structure()






