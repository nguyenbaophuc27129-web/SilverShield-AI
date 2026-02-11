import streamlit as st
from PIL import Image
import styles
import logic

# 1. KHỞI TẠO
styles.apply_styles()
styles.render_top_bar()
model = logic.init_ai()

if 'page' not in st.session_state:
    st.session_state['page'] = '🏠 TRANG CHỦ'

# 2. MENU ĐIỀU HƯỚNG (ĐÃ CĂN CHỈNH THẲNG HÀNG)
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
# Chia cột: Logo (1) | Khoảng trắng (0.5) | Menu (5) | Nút Button (1.5)
c_logo, c_pad, c_m1, c_m2, c_m3, c_m4, c_btn = st.columns([1, 0.5, 1.2, 1.2, 1.2, 1.2, 2])

with c_logo:
    st.image("https://olympicenglish.vn/images/logo.png", width=80) # Logo giả lập
with c_m1:
    if st.button("TRANG CHỦ"): st.session_state['page'] = '🏠 TRANG CHỦ'
with c_m2:
    if st.button("GIỚI THIỆU"): st.session_state['page'] = '👥 GIỚI THIỆU'
with c_m3:
    if st.button("VỆ SĨ AI"): st.session_state['page'] = '🛡️ VỆ SĨ AI'
with c_m4:
    if st.button("TIN TỨC"): st.session_state['page'] = '📰 TIN TỨC'
with c_btn:
    st.markdown('<div class="btn-check-ai">', unsafe_allow_html=True)
    if st.button("🚀 KIỂM TRA NGAY"): st.session_state['page'] = '🛡️ VỆ SĨ AI'
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- NỘI DUNG TRANG CHỦ ---
if st.session_state['page'] == '🏠 TRANG CHỦ':
    # BANNER LỚN
    st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True, className="hero-banner")
    
    # SECTION 1: SƠ LƯỢC (2 Cột)
    st.markdown('<h2 class="section-header">VỀ DỰ ÁN SILVERSHIELD</h2>', unsafe_allow_html=True)
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.markdown("""
        <div class="card-box">
            <h3 style="color:#002147; margin-top:0;">Sứ mệnh bảo vệ người cao tuổi</h3>
            <p style="font-size:16px; line-height:1.6; color:#555;">
                Trong kỷ nguyên số, người cao tuổi đang trở thành mục tiêu yếu thế trước các thủ đoạn lừa đảo công nghệ cao. 
                <b>SilverShield</b> ra đời như một "người vệ sĩ ảo" 24/7, sử dụng AI để phân tích tin nhắn, hình ảnh và đưa ra cảnh báo kịp thời.
            </p>
            <p><b>Được phát triển bởi:</b> Nhóm DVT-Empire X CBZ (THPT Dương Văn Thì).</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        # Thay ảnh thật của nhóm bạn vào đây thì tuyệt vời
        st.image("https://img.freepik.com/free-vector/cyber-security-risk-management-concept-illustration_114360-16147.jpg", use_container_width=True)

    # SECTION 2: CÁC ĐƠN VỊ ĐỒNG HÀNH (GIỐNG OLYMPIC)
    st.markdown('<br><h2 class="section-header">ĐƠN VỊ CHỨC NĂNG & ĐỒNG HÀNH</h2>', unsafe_allow_html=True)
    
    # Tạo lưới logo 4 cột
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="card-box partner-logo" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Logo_bo_cong_an.png/120px-Logo_bo_cong_an.png", width=80)
        st.caption("Bộ Công An")
        st.markdown('</div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card-box partner-logo" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg/120px-Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg.png", width=80)
        st.caption("Bộ GD & ĐT")
        st.markdown('</div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card-box partner-logo" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://tinnhiemmang.vn/handle_cert/images/logo.png", width=120)
        st.caption("Tín Nhiệm Mạng")
        st.markdown('</div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="card-box partner-logo" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=80)
        st.caption("SilverShield AI")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TRANG VỆ SĨ AI ---
elif st.session_state['page'] == '🛡️ VỆ SĨ AI':
    st.markdown('<h2 class="section-header">🛡️ TRUNG TÂM PHÂN TÍCH</h2>', unsafe_allow_html=True)
    c_in, c_out = st.columns([1, 1], gap="large")
    
    with c_in:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.subheader("1. Nhập thông tin nghi ngờ")
        txt = st.text_area("Dán tin nhắn vào đây:", height=150)
        img_f = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        if st.button("🔍 PHÂN TÍCH NGAY", type="primary"):
            if txt or img_f:
                with st.spinner("AI đang quét dữ liệu..."):
                    img = Image.open(img_f) if img_f else None
                    st.session_state['res'] = logic.analyze_content(model, txt, img)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_out:
        st.markdown('<div class="card-box" style="background:#f8f9fa;">', unsafe_allow_html=True)
        st.subheader("2. Kết quả từ SilverShield")
        if 'res' in st.session_state:
            st.success("Đã có kết quả phân tích:")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("👈 Hãy nhập liệu bên trái để cháu kiểm tra nhé!")
            st.image("https://cdn-icons-png.flaticon.com/512/2620/2620602.png", width=100)
        st.markdown('</div>', unsafe_allow_html=True)

# --- TRANG TIN TỨC ---
elif st.session_state['page'] == '📰 TIN TỨC':
    st.markdown('<h2 class="section-header">📰 TIN TỨC AN NINH MẠNG</h2>', unsafe_allow_html=True)
    
    n1, n2, n3 = st.columns(3)
    with n1:
        st.markdown("""
        <div class="card-box">
            <h4 style="color:#D32F2F">Cảnh báo Lừa đảo 2026</h4>
            <p>Các hình thức lừa đảo Deepfake mới nhất...</p>
            <a href="#">Xem chi tiết →</a>
        </div>
        """, unsafe_allow_html=True)
    with n2:
        st.markdown("""
        <div class="card-box">
            <h4 style="color:#002147">Kỹ năng phòng vệ</h4>
            <p>5 quy tắc vàng người cao tuổi cần nhớ...</p>
            <a href="#">Xem chi tiết →</a>
        </div>
        """, unsafe_allow_html=True)
    with n3:
        st.markdown("""
        <div class="card-box">
            <h4 style="color:#002147">Câu chuyện cảnh giác</h4>
            <p>Bà cụ suýt mất 200 triệu vì cuộc gọi giả...</p>
            <a href="#">Xem chi tiết →</a>
        </div>
        """, unsafe_allow_html=True)

# --- TRANG GIỚI THIỆU ---
elif st.session_state['page'] == '👥 GIỚI THIỆU':
    st.markdown('<h2 class="section-header">👥 ĐỘI NGŨ THỰC HIỆN</h2>', unsafe_allow_html=True)
    st.info("Đang cập nhật danh sách thành viên...")

# FOOTER ĐẸP
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="background:#002147; color:white; padding:40px 0; text-align:center; border-top: 5px solid #FFB300;">
        <p style="font-size:18px; font-weight:bold;">© 2026 SILVERSHIELD - VÌ AN TOÀN KHÔNG GIAN MẠNG</p>
        <p>Sản phẩm dự thi AI YOUNG GURU 2026 | THPT Dương Văn Thì</p>
        <p style="font-size:12px; opacity:0.7;">Email: contact@silvershield.vn</p>
    </div>
""", unsafe_allow_html=True)
