import streamlit as st
from PIL import Image
import styles
import logic

# ================= KHỞI TẠO =================
styles.apply_styles()
styles.render_header()

try:
    model = logic.init_ai()
except:
    pass

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'


# ================= HERO BANNER =================
st.markdown("""
<div style="
    width:100%;
    border-radius:16px;
    overflow:hidden;
    box-shadow:0 6px 25px rgba(0,0,0,0.15);
    margin-bottom:30px;">
    <img src="https://olympicenglish.vn/upload/banner-olympic-2025.png"
         style="width:100%; display:block;">
</div>
""", unsafe_allow_html=True)


# ================= MENU ĐIỀU HƯỚNG =================
st.markdown("<div style='margin-bottom:40px;'>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    if st.button("🏠 TRANG CHỦ", use_container_width=True):
        st.session_state['page'] = 'TRANG CHỦ'

with m2:
    if st.button("👥 GIỚI THIỆU", use_container_width=True):
        st.session_state['page'] = 'GIỚI THIỆU'

with m3:
    if st.button("📰 TIN TỨC", use_container_width=True):
        st.session_state['page'] = 'TIN TỨC'

with m4:
    if st.button("🛡️ VỆ SĨ SILVER", use_container_width=True):
        st.session_state['page'] = 'VỆ SĨ SILVER'

st.markdown("</div>", unsafe_allow_html=True)


# ================= TRANG CHỦ =================
if st.session_state['page'] == 'TRANG CHỦ':

    st.markdown("""
    <h2 style="
        border-left:6px solid #D32F2F;
        padding-left:12px;
        font-weight:800;
        color:#002147;">
        TỔNG QUAN SILVERSHIELD
    </h2>
    """, unsafe_allow_html=True)

    left, right = st.columns([2,1], gap="large")

    with left:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.subheader("🛡️ SilverShield là gì?")
        st.write("""
        SilverShield là nền tảng AI giúp người cao tuổi phòng tránh lừa đảo trực tuyến.
        Hệ thống có thể phân tích tin nhắn và hình ảnh để đưa ra cảnh báo tức thì.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.subheader("📖 Hướng dẫn nhanh")
        st.write("1. Vào tab Vệ sĩ Silver")
        st.write("2. Nhập nội dung hoặc tải ảnh")
        st.write("3. Nhấn Kiểm tra")
        st.write("4. Xem kết quả AI")
        st.markdown("</div>", unsafe_allow_html=True)


# ================= TRANG GIỚI THIỆU =================
elif st.session_state['page'] == 'GIỚI THIỆU':

    st.markdown("""
    <h2 style="
        border-left:6px solid #D32F2F;
        padding-left:12px;
        font-weight:800;
        color:#002147;">
        ĐỘI NGŨ PHÁT TRIỂN
    </h2>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)
        st.markdown("### Thành viên 1\n*Lập trình*")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140047.png", width=120)
        st.markdown("### Thành viên 2\n*Nội dung AI*")
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140037.png", width=120)
        st.markdown("### Thành viên 3\n*Thiết kế*")
        st.markdown("</div>", unsafe_allow_html=True)


# ================= TRANG VỆ SĨ SILVER =================
elif st.session_state['page'] == 'VỆ SĨ SILVER':

    st.markdown("""
    <h2 style="
        border-left:6px solid #D32F2F;
        padding-left:12px;
        font-weight:800;
        color:#002147;">
        VỆ SĨ AI PHÂN TÍCH
    </h2>
    """, unsafe_allow_html=True)

    col_input, col_result = st.columns([1,1], gap="large")

    with col_input:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.subheader("1. Nhập nội dung nghi ngờ")
        user_text = st.text_area("Dán nội dung vào đây:", height=150)
        uploaded_file = st.file_uploader("Hoặc tải ảnh:", type=['jpg','png','jpeg'])

        if st.button("🔍 KIỂM TRA NGAY", use_container_width=True):
            if user_text or uploaded_file:
                with st.spinner("Đang phân tích..."):
                    try:
                        img = Image.open(uploaded_file) if uploaded_file else None
                        st.session_state['result'] = logic.analyze_content(model, user_text, img)
                    except Exception as e:
                        st.error(f"Lỗi: {e}")
            else:
                st.warning("Bạn chưa nhập nội dung.")

        st.markdown("</div>", unsafe_allow_html=True)

    with col_result:
        st.markdown("<div class='info-card' style='background:#f1f8e9;'>", unsafe_allow_html=True)
        st.subheader("2. Kết quả")

        if 'result' in st.session_state:
            st.success("Hoàn tất phân tích")
            st.write(st.session_state['result'])
        else:
            st.info("Nhập nội dung bên trái để bắt đầu.")

        st.markdown("</div>", unsafe_allow_html=True)


# ================= FOOTER =================
styles.render_footer()
