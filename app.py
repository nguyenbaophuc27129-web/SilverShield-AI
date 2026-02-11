import streamlit as st
from PIL import Image
import styles
import logic

# 1. KHỞI TẠO
styles.apply_styles()
styles.render_top_bar()
model = logic.init_ai()

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# 2. MENU ĐIỀU HƯỚNG (FINAL VERSION - THẲNG TẮP)
# Chia làm 3 khu vực lớn: Logo | Các Link Menu | Nút Hành Động
c_logo_area, c_menu_area, c_action_area = st.columns([1.5, 6, 2.5])

with c_logo_area:
    # Logo của bạn (Tui để link icon tạm vì link cũ bị lỗi)
    st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=70)

with c_menu_area:
    # Chia nhỏ khu vực giữa thành 4 phần bằng nhau cho 4 menu
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("TRANG CHỦ"): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("GIỚI THIỆU"): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("TIN TỨC"): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("LIÊN HỆ"): st.session_state['page'] = 'LIÊN HỆ'

with c_action_area:
    st.markdown('<div class="btn-check-ai">', unsafe_allow_html=True)
    if st.button("🚀 KIỂM TRA NGAY"): st.session_state['page'] = 'VỆ SĨ AI'
    st.markdown('</div>', unsafe_allow_html=True)

# Đường gạch ngang mờ phân cách menu
st.markdown("<hr>", unsafe_allow_html=True)


# --- NỘI DUNG CHÍNH ---

if st.session_state['page'] == 'TRANG CHỦ':
    # Banner
    st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True)
    
    st.markdown('<h2 class="section-header">VỀ DỰ ÁN SILVERSHIELD</h2>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        st.markdown("""
        <div class="card-box">
            <h3 style="color:#002147; margin-top:0;">Sứ mệnh bảo vệ người cao tuổi</h3>
            <p style="font-size:16px; line-height:1.6; color:#555;">
                Trong kỷ nguyên số, người cao tuổi đang trở thành mục tiêu yếu thế trước các thủ đoạn lừa đảo công nghệ cao. 
                <b>SilverShield</b> ra đời như một "người vệ sĩ ảo" 24/7, sử dụng AI để phân tích tin nhắn, hình ảnh và đưa ra cảnh báo kịp thời.
            </p>
            <p style="margin-top:20px;">
                ✅ <b>Phát triển bởi:</b> Nhóm DVT-Empire X CBZ (THPT Dương Văn Thì)<br>
                ✅ <b>Công nghệ:</b> Generative AI (Google Gemini) + Voice Processing
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        # Ảnh minh họa bên phải
        st.image("https://img.freepik.com/free-vector/old-woman-using-laptop_1308-133534.jpg", use_container_width=True)

    # ĐƠN VỊ ĐỒNG HÀNH
    st.markdown('<h2 class="section-header">ĐƠN VỊ CHỨC NĂNG & ĐỒNG HÀNH</h2>', unsafe_allow_html=True)
    
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="partner-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Logo_bo_cong_an.png/120px-Logo_bo_cong_an.png" width="60"></div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:12px; font-weight:bold;'>BỘ CÔNG AN</p>", unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="partner-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg/120px-Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg.png" width="60"></div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:12px; font-weight:bold;'>BỘ GD&ĐT</p>", unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="partner-img"><img src="https://tinnhiemmang.vn/handle_cert/images/logo.png" width="100"></div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:12px; font-weight:bold;'>TÍN NHIỆM MẠNG</p>", unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="partner-img"><img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" width="60"></div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:12px; font-weight:bold;'>SILVERSHIELD AI</p>", unsafe_allow_html=True)

# --- TRANG VỆ SĨ AI ---
elif st.session_state['page'] == 'VỆ SĨ AI':
    st.markdown('<h2 class="section-header">🛡️ TRUNG TÂM PHÂN TÍCH</h2>', unsafe_allow_html=True)
    
    c_in, c_out = st.columns([1, 1], gap="large")
    with c_in:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.subheader("1. Nhập thông tin cần kiểm tra")
        txt = st.text_area("Dán nội dung tin nhắn vào đây:", height=150)
        img_f = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        
        if st.button("🔍 PHÂN TÍCH NGAY", type="primary"):
            if txt or img_f:
                with st.spinner("Đang kết nối vệ sĩ AI..."):
                    img = Image.open(img_f) if img_f else None
                    st.session_state['res'] = logic.analyze_content(model, txt, img)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c_out:
        st.markdown('<div class="card-box" style="background-color:#f8f9fa;">', unsafe_allow_html=True)
        st.subheader("2. Kết quả phân tích")
        if 'res' in st.session_state:
            st.success("Đã có kết quả!")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("👈 Vui lòng nhập dữ liệu bên trái để kiểm tra.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TRANG TIN TỨC ---
elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<h2 class="section-header">📰 TIN TỨC AN NINH MẠNG</h2>', unsafe_allow_html=True)
    st.info("Đang cập nhật tin tức mới nhất từ Cục An toàn thông tin...")

# FOOTER
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="background:#002147; color:white; padding:30px; text-align:center;">
        <b>© 2026 SILVERSHIELD PROJECT - THPT DƯƠNG VĂN THÌ</b><br>
        <small>Vì một không gian mạng an toàn cho người cao tuổi</small>
    </div>
""", unsafe_allow_html=True)
