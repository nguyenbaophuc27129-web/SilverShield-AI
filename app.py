import streamlit as st
from PIL import Image
import styles
import logic

# 1. Cấu hình ban đầu
styles.apply_styles()
styles.render_top_bar()
model = logic.init_ai()

# 2. Quản lý trạng thái chuyển trang (Session State)
if 'page' not in st.session_state:
    st.session_state['page'] = '🏠 TRANG CHỦ'

# 3. TẠO THANH MENU NGANG (Dùng st.columns)
st.markdown("<br>", unsafe_allow_html=True)
col_logo, col_m1, col_m2, col_m3, col_m4, col_btn = st.columns([1, 1, 1, 1, 1, 1.5])

with col_logo:
    st.image("https://olympicenglish.vn/images/logo.png", width=70)

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
    if st.button("🔥 KIỂM TRA NGAY"):
        st.session_state['page'] = '🛡️ Vệ Sĩ AI'
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- NỘI DUNG TỪNG TRANG ---

# TRANG CHỦ
if st.session_state['page'] == '🏠 TRANG CHỦ':
    st.markdown("""
        <div class="main-banner">
            <h1 style="font-size: 50px;">SILVERSHIELD</h1>
            <p style="font-size: 22px;">Lá chắn AI bảo vệ người cao tuổi Việt Nam</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("""
            <div class="card-pro">
                <h3>Về dự án</h3>
                <p>SilverShield là giải pháp ứng dụng trí tuệ nhân tạo nhằm hỗ trợ người cao tuổi 
                nhận diện và phòng chống các hình thức lừa đảo trực tuyến đang ngày càng tinh vi.</p>
                <p>Đội ngũ <b>DVT-Empire X CBZ</b> cam kết mang lại một môi trường mạng an toàn hơn cho mọi người.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_r:
        st.image("https://baochinhphu.vn/Uploaded/tranducmanh/2023_03_14/lua-dao-con-cap-cuu-2.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# TRANG GIỚI THIỆU THÀNH VIÊN
elif st.session_state['page'] == '👥 GIỚI THIỆU':
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#002147;'>👥 ĐỘI NGŨ DVT-EMPIRE X CBZ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Chúng em đến từ Trường THPT Dương Văn Thì</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    # Bạn thay tên và ảnh của các thành viên vào đây nhé
    with c1:
        st.markdown('<div class="card-pro" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        st.markdown("<h4>Thành viên 1</h4><p>Trưởng nhóm / Developer</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-pro" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        st.markdown("<h4>Thành viên 2</h4><p>AI Researcher</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card-pro" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        st.markdown("<h4>Thành viên 3</h4><p>UI/UX Design</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# TRANG VỆ SĨ AI
elif st.session_state['page'] == '🛡️ Vệ Sĩ AI':
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#002147;'>🛡️ TRUNG TÂM PHÂN TÍCH VỆ SĨ AI</h2>", unsafe_allow_html=True)
    
    col_in, col_out = st.columns([1, 1])
    with col_in:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        txt = st.text_area("Nhập nội dung cần kiểm tra:", height=150)
        img_file = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        if st.button("🔍 BẮT ĐẦU PHÂN TÍCH"):
            with st.spinner("Đang quét dữ liệu..."):
                img = Image.open(img_file) if img_file else None
                st.session_state['res'] = logic.analyze_content(model, txt, img)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_out:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        if 'res' in st.session_state:
            st.success(st.session_state['res'])
            audio = logic.text_to_speech(st.session_state['res'])
            st.audio(audio)
        else:
            st.info("Kết quả sẽ hiển thị tại đây...")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# TRANG TIN TỨC
elif st.session_state['page'] == '📰 TIN TỨC':
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#002147;'>📰 TIN TỨC CHÍNH THỐNG</h2>", unsafe_allow_html=True)
    
    # Mẫu tin tức
    st.markdown("""
        <div class="card-pro">
            <h4 style="color:#d32f2f;">🚨 Cảnh báo lừa đảo Deepfake từ Bộ Công an</h4>
            <p>Các đối tượng sử dụng AI để giả mạo khuôn mặt, giọng nói của người thân nhằm lừa đảo chuyển tiền...</p>
            <a href="https://baochinhphu.vn" target="_blank">Xem thêm trên Báo Chính Phủ →</a>
        </div>
        <div class="card-pro">
            <h4 style="color:#d32f2f;">🛡️ Cẩm nang phòng chống lừa đảo trên không gian mạng</h4>
            <p>Hãy ghi nhớ 5 quy tắc vàng để bảo vệ chính mình và gia đình...</p>
            <a href="https://tinnhiemmang.vn" target="_blank">Xem chi tiết →</a>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div style="background:#002147; color:white; padding:30px 10%; text-align:center;">
        <p>© 2026 SilverShield Project - THPT Dương Văn Thì</p>
        <p style="font-size:12px;">Được bảo trợ bởi Hội thi AI YOUNG GURU Toàn Quốc</p>
    </div>
""", unsafe_allow_html=True)
        </div>
    </div>
""", unsafe_allow_html=True)

