import streamlit as st
from PIL import Image
import styles
import logic

# 1. Cấu hình & Áp dụng Style (Xóa sạch giao diện Streamlit cũ)
styles.apply_styles()
styles.render_header()
model = logic.init_ai()

# 2. Xử lý chuyển trang bằng Session State (Vì mình đã giấu Sidebar)
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

# --- PHẦN BANNER TO ĐÙNG ---
st.markdown(f"""
    <div class="main-banner">
        <h1 style="font-size: 45px; margin: 0;">SILVERSHIELD - LÁ CHẮN AI</h1>
        <p style="font-size: 20px; max-width: 700px;">Bảo vệ người cao tuổi Việt Nam trước các hiểm họa lừa đảo không gian mạng</p>
        <a class="banner-btn" href="#analysis-section">BẮT ĐẦU KIỂM TRA NGAY</a>
    </div>
""", unsafe_allow_html=True)

# --- PHẦN NỘI DUNG CHÍNH ---
st.markdown('<div class="section-container" id="analysis-section">', unsafe_allow_html=True)

col_info, col_ai = st.columns([1, 1.2], gap="large")

with col_info:
    st.markdown("""
        <div class="card-pro">
            <h2 style="color:#002147;">#ChinhPhucAI</h2>
            <p style="color:#666;">Dự án phát triển bởi nhóm <b>GenZ SilverShield</b> nhằm thu hẹp khoảng cách số và bảo vệ Ông Bà.</p>
            <hr>
            <h4>5 QUY TẮC VÀNG:</h4>
            <ul>
                <li>Giữ an toàn thông tin</li>
                <li>Không gặp gỡ người lạ</li>
                <li>Đừng chấp nhận yêu cầu chuyển tiền</li>
                <li>Kiểm tra độ tin cậy</li>
                <li>Hãy nói ra với con cháu</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col_ai:
    st.markdown('<div class="card-pro">', unsafe_allow_html=True)
    st.subheader("🛡️ TRUNG TÂM PHÂN TÍCH VỆ SĨ AI")
    
    # Khu vực Input
    user_text = st.text_area("Nhập nội dung tin nhắn hoặc bài viết nghi ngờ:", height=120)
    u_file = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
    
    if st.button("🔍 PHÂN TÍCH NGAY"):
        if user_text or u_file:
            with st.spinner("Hệ thống đang quét dữ liệu..."):
                img = Image.open(u_file) if u_file else None
                res = logic.analyze_content(model, user_text, img)
                st.session_state['result'] = res
        else:
            st.error("Bà ơi, bà chưa nhập dữ liệu để cháu kiểm tra ạ!")

    # Hiển thị kết quả
    if 'result' in st.session_state:
        st.markdown("---")
        st.markdown(f"#### 💌 Lời khuyên từ SilverShield:")
        st.info(st.session_state['result'])
        audio = logic.text_to_speech(st.session_state['result'])
        st.audio(audio, format='audio/mp3')
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Kết thúc section-container

# --- FOOTER ---
st.markdown("""
    <div style="background:#f8f9fa; padding: 50px 10%; border-top: 1px solid #ddd; margin-top: 50px;">
        <div style="display:flex; justify-content: space-between;">
            <div>
                <img src="https://olympicenglish.vn/images/logo.png" width="100">
                <p>© 2026 SilverShield - AI for Social Good</p>
            </div>
            <div>
                <h4>ĐƠN VỊ TỔ CHỨC</h4>
                <p>Hội thi AI YOUNG GURU Toàn Quốc</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
