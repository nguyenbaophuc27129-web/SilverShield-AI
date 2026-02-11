import streamlit as st
from PIL import Image
import styles
import logic

# 1. Cấu hình ban đầu
styles.apply_styles()
styles.render_top_bar()
model = logic.init_ai()

if 'page' not in st.session_state:
    st.session_state['page'] = '🏠 TRANG CHỦ'

# 2. THANH MENU (Chia lại tỷ lệ cột để không bị tràn)
st.markdown("<div style='padding: 0 5%;'>", unsafe_allow_html=True) # Tạo lề cho menu
col_logo, col_m1, col_m2, col_m3, col_m4, col_spacer, col_btn = st.columns([0.8, 1, 1, 1, 1, 2, 1.5])

with col_logo:
    st.image("https://olympicenglish.vn/images/logo.png", width=60)
with col_m1:
    if st.button("🏠 TRANG CHỦ"): st.session_state['page'] = '🏠 TRANG CHỦ'
with col_m2:
    if st.button("👥 GIỚI THIỆU"): st.session_state['page'] = '👥 GIỚI THIỆU'
with col_m3:
    if st.button("🛡️ VỆ SĨ AI"): st.session_state['page'] = '🛡️ VỆ SĨ AI'
with col_m4:
    if st.button("📰 TIN TỨC"): st.session_state['page'] = '📰 TIN TỨC'
with col_btn:
    st.markdown('<div class="btn-check-ai">', unsafe_allow_html=True)
    if st.button("🚀 KIỂM TRA NGAY"): st.session_state['page'] = '🛡️ VỆ SĨ AI'
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='margin:0;'>", unsafe_allow_html=True)

# --- NỘI DUNG TỪNG TRANG ---

if st.session_state['page'] == '🏠 TRANG CHỦ':
    st.markdown('<div class="main-banner"><h1>SILVERSHIELD</h1><p>Lá chắn AI bảo vệ người cao tuổi</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    col_l, col_r = st.columns(2, gap="large")
    with col_l:
        st.markdown('<div class="card-pro"><h3>Về dự án</h3><p>SilverShield bảo vệ người cao tuổi trước các hiểm họa mạng. Phát triển bởi đội ngũ <b>DVT-Empire X CBZ</b>.</p></div>', unsafe_allow_html=True)
    with col_r:
        st.image("https://baochinhphu.vn/Uploaded/tranducmanh/2023_03_14/lua-dao-con-cap-cuu-2.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state['page'] == '👥 GIỚI THIỆU':
    st.markdown('<div class="section-container"><h1>👥 ĐỘI NGŨ DVT-EMPIRE X CBZ</h1><div class="card-pro"><h3>Trường THPT Dương Văn Thì</h3><p>Thông tin thành viên...</p></div></div>', unsafe_allow_html=True)

elif st.session_state['page'] == '🛡️ VỆ SĨ AI':
    st.markdown('<div class="section-container"><h2>🛡️ PHÂN TÍCH VỆ SĨ AI</h2>', unsafe_allow_html=True)
    c_in, c_out = st.columns(2, gap="large")
    with c_in:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        txt = st.text_area("Dán tin nhắn nghi ngờ:")
        img_f = st.file_uploader("Hoặc gửi ảnh:")
        if st.button("🔍 KIỂM TRA"):
            if txt or img_f:
                with st.spinner("Đang quét..."):
                    img = Image.open(img_f) if img_f else None
                    st.session_state['res'] = logic.analyze_content(model, txt, img)
        st.markdown('</div>', unsafe_allow_html=True)
    with c_out:
        if 'res' in st.session_state:
            st.markdown('<div class="card-pro">', unsafe_allow_html=True)
            st.success(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state['page'] == '📰 TIN TỨC':
    st.markdown('<div class="section-container"><h2>📰 TIN TỨC</h2><div class="card-pro"><h4>Cảnh báo từ Bộ Công An</h4><a href="https://baochinhphu.vn" target="_blank">Xem ngay →</a></div></div>', unsafe_allow_html=True)

# FOOTER
st.markdown('<div style="background:#002147; color:white; padding:30px; text-align:center;">© 2026 SilverShield - THPT Dương Văn Thì</div>', unsafe_allow_html=True)
