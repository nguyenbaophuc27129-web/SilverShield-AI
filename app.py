import streamlit as st
from PIL import Image
import styles
import logic

# --- KHỞI TẠO ---
styles.apply_styles()
styles.render_header()
try:
    model = logic.init_ai()
except:
    pass

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- MENU ---
with st.container():
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
    if c2.button("GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
    if c3.button("TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
    if c4.button("VỆ SĨ SILVER", use_container_width=True): st.session_state['page'] = 'VỆ SĨ SILVER'
st.markdown("<hr>", unsafe_allow_html=True)

# --- NỘI DUNG CHÍNH ---

# ================= TRANG CHỦ =================
if st.session_state['page'] == 'TRANG CHỦ':
    st.image("https://link-banner-cua-ban.png", use_container_width=True) # Thay link banner
    
    st.markdown('<div class="section-header">TỔNG QUAN DỰ ÁN</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1], gap="medium")
    with c1:
        st.markdown("""
        <div class="content-box">
            <h3>Về SilverShield</h3>
            <p>SilverShield là giải pháp công nghệ giúp người cao tuổi phòng chống lừa đảo trực tuyến. 
            Chúng tôi sử dụng AI để phân tích tin nhắn, hình ảnh và đưa ra cảnh báo kịp thời.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="content-box">
            <h3>Hướng dẫn nhanh</h3>
            <p>1. Chọn "Vệ sĩ Silver".<br>2. Nhập thông tin.<br>3. Bấm "Kiểm tra".</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">THÔNG TIN & QUY TẮC AN TOÀN</div>', unsafe_allow_html=True)
    n1, n2, n3 = st.columns(3, gap="medium")
    with n1:
        st.markdown('<div class="content-box"><h3>Tin tức nổi bật</h3><p>Cảnh báo thủ đoạn giả danh công an...</p></div>', unsafe_allow_html=True)
    with n2:
        st.markdown('<div class="content-box"><h3>5 KHÔNG</h3><p>Không chuyển tiền, không bấm link lạ...</p></div>', unsafe_allow_html=True)
    with n3:
        st.markdown('<div class="content-box"><h3>3 NÊN</h3><p>Nên gọi xác thực, nên hỏi con cháu...</p></div>', unsafe_allow_html=True)

# ================= TRANG VỆ SĨ SILVER =================
elif st.session_state['page'] == 'VỆ SĨ SILVER':
    st.markdown('<div class="section-header">TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        c_in, c_out = st.columns(2, gap="medium")
        
        with c_in:
            st.markdown("<h3>1. Nhập thông tin</h3>", unsafe_allow_html=True)
            user_text = st.text_area("Dán nội dung tin nhắn:", height=150)
            uploaded_file = st.file_uploader("Tải ảnh chụp màn hình:")
            if st.button("PHÂN TÍCH NGAY", type="primary", use_container_width=True):
                st.session_state['analyzing'] = True

        with c_out:
            st.markdown("<h3>2. Kết quả</h3>", unsafe_allow_html=True)
            if 'analyzing' in st.session_state:
                with st.spinner("Đang phân tích..."):
                    img = Image.open(uploaded_file) if uploaded_file else None
                    st.session_state['result'] = logic.analyze_content(model, user_text, img)
                    st.success("Đã có kết quả!")
                    st.write(st.session_state['result'])
                    st.audio(logic.text_to_speech(st.session_state['result']))
            else:
                st.info("Kết quả sẽ hiển thị tại đây.")

        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="width:100vw; position:relative; left:50%; right:50%; margin-left:-50vw; margin-right:-50vw;">
        <div class="footer">
            <h3>SILVERSHIELD</h3>
            <p>"Vì một không gian mạng an toàn"</p>
            <p>© 2026 Đội ngũ DVT - Empire CBZ X</p>
        </div>
    </div>
""", unsafe_allow_html=True)
