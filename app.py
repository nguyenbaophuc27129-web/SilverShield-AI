import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
st.set_page_config(layout="wide", page_title="SilverShield - Vì an toàn không gian mạng", page_icon="🛡️")
styles.apply_styles()

# --- 2. HEADER ---
# TOP BAR
st.markdown("""
<div class="top-bar">
    <div class="top-bar-content">
        <span>📧 Email: contact@silvershield.vn | 🌐 Fanpage: DVT.SilverShield</span>
        <div>
            <a href="#" class="top-bar-btn btn-red">HƯỚNG DẪN</a>
            <a href="#" class="top-bar-btn btn-gold">KẾT NỐI AI</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# NAVBAR
with st.container():
    c_logo, c_menu = st.columns([2, 8])
    with c_logo:
        # Thay link logo của bạn vào
        st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=60)
    with c_menu:
        # Menu ngang
        m1,m2,m3,m4,m5,m6,m7,m8 = st.columns(8)
        if 'page' not in st.session_state:
            st.session_state['page'] = 'Trang chủ'

        with m1:
            if st.button("Trang chủ", use_container_width=True): st.session_state['page'] = 'Trang chủ'
        with m2:
            if st.button("Giới thiệu", use_container_width=True): st.session_state['page'] = 'Giới thiệu'
        with m3:
            if st.button("Thể lệ an toàn", use_container_width=True): st.session_state['page'] = 'Thể lệ an toàn'
        with m4:
            if st.button("Vệ sĩ Silver", use_container_width=True): st.session_state['page'] = 'Vệ sĩ Silver'
        with m5:
            if st.button("Tin tức", use_container_width=True): st.session_state['page'] = 'Tin tức'
        with m6:
            if st.button("FAQs", use_container_width=True): st.session_state['page'] = 'FAQs'
        with m7:
            if st.button("Đội ngũ", use_container_width=True): st.session_state['page'] = 'Đội ngũ'
        with m8:
            if st.button("Liên hệ", use_container_width=True): st.session_state['page'] = 'Liên hệ'

# --- 3. NỘI DUNG CHÍNH ---

# ================ TRANG CHỦ ================
if st.session_state['page'] == 'Trang chủ':
    
    # HERO SECTION
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <div style="display: flex; align-items: center; gap: 30px;">
                <div style="flex: 2;">
                    <h1 style="font-size: 48px; font-weight: 700; line-height: 1.2;">BẢO VỆ NGƯỜI THÂN<br>TRÊN KHÔNG GIAN MẠNG</h1>
                    <p style="font-size: 18px; opacity: 0.9; margin: 20px 0;">Phân tích tin nhắn, phát hiện lừa đảo và cảnh báo bằng giọng nói.</p>
                </div>
                <div style="flex: 1;">
                    <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 20px; border-radius: 12px; text-align: center;">
                        <h3 style="margin-top: 0;">Bắt đầu phân tích</h3>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Website", type="primary", key="hero_cta"):
        st.session_state['page'] = 'Vệ sĩ Silver'

    # SECTION: ĐƠN VỊ TỔ CHỨC
    st.markdown("""
    <div class="section-header"><div class="section-title">ĐƠN VỊ PHÁT TRIỂN</div></div>
    <div style="display: flex; justify-content: center; align-items: center; gap: 50px;">
        <img src="https://link-logo-truong.png" height="60" alt="Logo THPT Dương Văn Thì">
        <h3 style="margin:0; color:#1a365d;">DVT - EMPIRE CBZ X</h3>
    </div>
    """, unsafe_allow_html=True)

# ================ VỆ SĨ SILVER (AI TOOL) ================
elif st.session_state['page'] == 'Vệ sĩ Silver':
    st.markdown("""
    <div class="section-header">
        <div class="section-title">TRUNG TÂM PHÂN TÍCH AI</div>
        <div class="section-subtitle">Dán nội dung hoặc tải ảnh để kiểm tra độ an toàn</div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">1. Nhập thông tin</h3>', unsafe_allow_html=True)
        user_text = st.text_area("Dán nội dung tin nhắn:", height=150)
        uploaded_file = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
        if st.button("PHÂN TÍCH NGAY", type="primary", use_container_width=True):
            st.success("Đang phân tích...")
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card" style="background: #e3f2fd;">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">2. Kết quả phân tích</h3>', unsafe_allow_html=True)
        st.info("Kết quả sẽ hiển thị ở đây...")
        st.markdown('</div>', unsafe_allow_html=True)

# ================ ĐỘI NGŨ ================
elif st.session_state['page'] == 'Đội ngũ':
    st.markdown("""
    <div class="section-header">
        <div class="section-title">ĐỘI NGŨ PHÁT TRIỂN</div>
        <div class="section-subtitle">Những con người tạo nên SilverShield</div>
    </div>
    """, unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns(3, gap="medium")
    with t1:
        st.markdown('<div class="card" style="text-align:center;"><img src="https://link-anh-thanh-vien-1.png" style="width:100px; height:100px; border-radius:50%;"><h3 class="card-title" style="margin-top:15px;">Thành viên 1</h3><p>Trưởng nhóm</p></div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="card" style="text-align:center;"><img src="https://link-anh-thanh-vien-2.png" style="width:100px; height:100px; border-radius:50%;"><h3 class="card-title" style="margin-top:15px;">Thành viên 2</h3><p>Nội dung</p></div>', unsafe_allow_html=True)
    with t3:
        st.markdown('<div class="card" style="text-align:center;"><img src="https://link-anh-thanh-vien-3.png" style="width:100px; height:100px; border-radius:50%;"><h3 class="card-title" style="margin-top:15px;">Thành viên 3</h3><p>Thiết kế</p></div>', unsafe_allow_html=True)

# --- 4. FOOTER ---
st.markdown("""
<div class="footer">
    <h2 style="margin:0; color:white;">SILVERSHIELD</h2>
    <p style="opacity:0.8; margin-top:10px;">“Vì một không gian mạng an toàn”</p>
    <div style="margin:20px 0; border-top:1px solid #4a5568; width:100px; margin:20px auto;"></div>
    <p style="font-size:13px; opacity:0.6;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
</div>
""", unsafe_allow_html=True)
