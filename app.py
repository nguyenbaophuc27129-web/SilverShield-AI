import streamlit as st
from PIL import Image
import styles
import logic
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
    pass # Bỏ qua nếu chưa config key để web vẫn hiện

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- BANNER LỚN & LOGO ---
# Banner Olympic mẫu (Bạn thay link ảnh banner thật của bạn vào đây)
st.image("https://github.com/nguyenbaophuc27129-web/SilverShield-AI/blob/5befa8d1b793de0b6934f56af0f4458a8967457b/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png", use_container_width=True)
st.image("https://github.com/nguyenbaophuc27129-web/SilverShield-AI/blob/5befa8d1b793de0b6934f56af0f4458a8967457b/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png", width=70)

# --- MENU ĐIỀU HƯỚNG (TASKBAR) ---
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
# Chia 4 cột đều nhau cho menu
m1, m2, m3, m4 = st.columns(4)
with m1:
    if st.button("🏠 TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
with m2:
    if st.button("👥 GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
with m3:
    if st.button("📰 TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
with m4:
    if st.button("🛡️ VỆ SĨ SILVER", use_container_width=True): st.session_state['page'] = 'VỆ SĨ SILVER'
st.markdown('</div>', unsafe_allow_html=True)

# --- NỘI DUNG CHÍNH ---

# ================= TRANG CHỦ =================
if st.session_state['page'] == 'TRANG CHỦ':
    
    # MỤC 1: VỀ SILVERSHIELD & HƯỚNG DẪN (Chia cột 2:1)
    st.markdown('<div class="section-title">TỔNG QUAN</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1], gap="medium")
    
    with c1:
        st.markdown("""
        <div class="info-card">
            <h3 style="color:#D32F2F; margin-top:0;">🛡️ Về SilverShield</h3>
            <p style="text-align: justify;">
                <b>SilverShield</b> là giải pháp công nghệ tiên phong dành riêng cho người cao tuổi, 
                đóng vai trò như một "lớp khiên bạc" bảo vệ ông bà, cha mẹ trước làn sóng lừa đảo trực tuyến.
                Sử dụng trí tuệ nhân tạo (AI) thế hệ mới, chúng tôi giúp phân tích tin nhắn, hình ảnh để đưa ra cảnh báo tức thì.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Grid nhỏ bên trong cho 2 mục con
        sub1, sub2 = st.columns(2)
        with sub1:
             st.markdown("""<div class="info-card" style="margin-top:15px; background:#e8eaf6;">
                <b>🎯 Sứ mệnh</b><br>Xóa bỏ khoảng cách số, mang lại sự an tâm.
             </div>""", unsafe_allow_html=True)
        with sub2:
             st.markdown("""<div class="info-card" style="margin-top:15px; background:#e8eaf6;">
                <b>🚀 Tầm nhìn</b><br>Trở thành ứng dụng quốc dân cho người cao tuổi.
             </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <h3 style="color:#002147; margin-top:0;">📖 Hướng dẫn nhanh</h3>
            <ul style="padding-left: 20px;">
                <li><b>B1:</b> Chọn Tab "Vệ sĩ Silver".</li>
                <li><b>B2:</b> Dán tin nhắn hoặc chụp ảnh màn hình.</li>
                <li><b>B3:</b> Bấm "Kiểm tra".</li>
                <li><b>B4:</b> Nghe lời khuyên từ AI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # MỤC 2: TIN TỨC & QUY TẮC (Chia cột 1:1:1)
    st.markdown('<div class="section-title">THÔNG TIN & QUY TẮC AN TOÀN</div>', unsafe_allow_html=True)
    n1, n2, n3 = st.columns(3, gap="medium")
    
    with n1:
        st.markdown("""
        <div class="info-card">
            <h4 style="color:#002147">📰 Tin tức nổi bật</h4>
            <hr>
            <p>🔥 Cảnh báo thủ đoạn giả danh công an gọi video...</p>
            <p>🔥 Lừa đảo "con cấp cứu" tái xuất hiện...</p>
        </div>
        """, unsafe_allow_html=True)
    
    with n2:
        st.markdown("""
        <div class="info-card">
            <h4 style="color:#002147">⛔ 5 KHÔNG</h4>
            <hr>
            1. Không chuyển tiền cho người lạ.<br>
            2. Không bấm link lạ.<br>
            3. Không cung cấp mã OTP.<br>
            4. Không cài app lạ.<br>
            5. Không sợ hãi trước lời đe dọa.
        </div>
        """, unsafe_allow_html=True)
        
    with n3:
        st.markdown("""
        <div class="info-card">
            <h4 style="color:#002147">✅ 3 NÊN</h4>
            <hr>
            1. Nên gọi điện xác thực.<br>
            2. Nên hỏi ý kiến con cháu.<br>
            3. Nên báo cơ quan chức năng (156).
        </div>
        """, unsafe_allow_html=True)


# ================= TRANG GIỚI THIỆU =================
elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="section-title">👥 ĐỘI NGŨ DVT - EMPIRE CBZ X</div>', unsafe_allow_html=True)
    st.info("Học sinh Trường THPT Dương Văn Thì - TP. Thủ Đức")
    
    col1, col2, col3 = st.columns(3)
    
    # Bạn thay tên và thông tin thật vào đây nhé
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)
        st.markdown("### Thành viên 1\n*Trưởng nhóm & Lập trình*")
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140047.png", width=120)
        st.markdown("### Thành viên 2\n*Nội dung & Dữ liệu AI*")

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140037.png", width=120)
        st.markdown("### Thành viên 3\n*Thiết kế & Truyền thông*")


# ================= TRANG TIN TỨC =================
elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="section-title">📰 ĐIỂM TIN AN NINH MẠNG</div>', unsafe_allow_html=True)
    
    # Bài 1
    st.markdown("""
    <div class="info-card" style="margin-bottom: 20px;">
        <h3 style="color:#D32F2F;">Cảnh báo: 24 hình thức lừa đảo trực tuyến phổ biến</h3>
        <p>Theo Cục An toàn thông tin (Bộ TT&TT), các hình thức lừa đảo ngày càng tinh vi...</p>
        <a href="https://tinnhiemmang.vn" target="_blank" style="color:#002147; font-weight:bold;">Xem chi tiết tại Tín Nhiệm Mạng >></a>
    </div>
    """, unsafe_allow_html=True)
    
    # Bài 2
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#D32F2F;">Cổng cảnh báo an toàn thông tin Việt Nam</h3>
        <p>Người dân có thể phản ánh các cuộc gọi rác, tin nhắn lừa đảo qua đầu số 156.</p>
        <a href="https://khonggianmang.vn" target="_blank" style="color:#002147; font-weight:bold;">Truy cập Cổng Không Gian Mạng >></a>
    </div>
    """, unsafe_allow_html=True)


# ================= TRANG VỆ SĨ SILVER =================
elif st.session_state['page'] == 'VỆ SĨ SILVER':
    st.markdown('<div class="section-title">🛡️ VỆ SĨ AI PHÂN TÍCH</div>', unsafe_allow_html=True)
    
    c_input, c_result = st.columns([1, 1], gap="large")
    
    with c_input:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.subheader("1. Nhập thông tin nghi ngờ")
        user_text = st.text_area("Dán nội dung tin nhắn vào đây:", height=150)
        uploaded_file = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        
        # Nút bấm kiểm tra đẹp
        if st.button("🔍 KIỂM TRA NGAY", type="primary", use_container_width=True):
            if user_text or uploaded_file:
                with st.spinner("Vệ sĩ Silver đang phân tích dữ liệu..."):
                    try:
                        img = Image.open(uploaded_file) if uploaded_file else None
                        st.session_state['result'] = logic.analyze_content(model, user_text, img)
                    except Exception as e:
                        st.error(f"Có lỗi xảy ra: {e}")
            else:
                st.warning("Bạn chưa nhập nội dung nào cả!")
        st.markdown('</div>', unsafe_allow_html=True)

    with c_result:
        st.markdown('<div class="info-card" style="background:#f1f8e9; border-color:#81c784;">', unsafe_allow_html=True)
        st.subheader("2. Kết quả từ SilverShield")
        
        if 'result' in st.session_state:
            st.success("Đã hoàn tất phân tích!")
            st.markdown(f"<div style='font-size:18px;'>{st.session_state['result']}</div>", unsafe_allow_html=True)
            # Giọng nói
            try:
                audio_bytes = logic.text_to_speech(st.session_state['result'])
                st.audio(audio_bytes, format='audio/mp3')
            except:
                st.warning("Không thể tạo giọng nói lúc này.")
        else:
            st.info("👈 Hãy nhập thông tin bên trái để Vệ sĩ bảo vệ bạn.")
            st.image("https://cdn-icons-png.flaticon.com/512/1161/1161388.png", width=100)
        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
styles.render_footer()
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



