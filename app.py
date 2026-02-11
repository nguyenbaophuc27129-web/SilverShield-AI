import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
styles.apply_styles()
styles.render_top_bar() # Hàm này giờ đã có trong styles.py, yên tâm không lỗi nữa
try:
    model = logic.init_ai()
except:
    pass

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. BANNER LỚN (Đầu trang) ---
# Bạn thay link banner của bạn vào đây
st.image("https://github.com/nguyenbaophuc27129-web/SilverShield-AI/blob/5befa8d1b793de0b6934f56af0f4458a8967457b/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png", use_container_width=True)

# --- 3. MENU NGANG (Thẳng hàng) ---
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
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

# --- 4. NỘI DUNG CHÍNH ---

if st.session_state['page'] == 'TRANG CHỦ':
    
    # HÀNG 1: VỀ SILVERSHIELD (Bên trái) & HƯỚNG DẪN (Bên phải)
    c1, c2 = st.columns([1.5, 1], gap="medium")
    
    with c1:
        styles.section_header("VỀ DỰ ÁN SILVERSHIELD")
        styles.open_box()
        st.markdown("""
        <h3 style="color:#002147; margin-top:0;">🛡️ Sứ mệnh bảo vệ</h3>
        <p style="text-align:justify; font-size: 15px;">
            Trong bối cảnh lừa đảo công nghệ cao ngày càng tinh vi, <b>SilverShield</b> ra đời như một lá chắn vững chắc dành riêng cho người cao tuổi. 
            Chúng tôi sử dụng <b>AI (Trí tuệ nhân tạo)</b> để phân tích tin nhắn và hình ảnh, giúp Ông Bà, Cha Mẹ nhận diện rủi ro ngay lập tức.
        </p>
        <p><b>Được phát triển bởi:</b> Nhóm DVT - Empire CBZ X (THPT Dương Văn Thì).</p>
        """, unsafe_allow_html=True)
        styles.close_box()

    with c2:
        styles.section_header("HƯỚNG DẪN SỬ DỤNG")
        styles.open_box()
        st.markdown("""
        <ul style="padding-left:15px; font-size: 15px;">
            <li>👉 <b>B1:</b> Chọn mục <b>'Vệ Sĩ Silver'</b>.</li>
            <li>👉 <b>B2:</b> Nhập tin nhắn hoặc tải ảnh.</li>
            <li>👉 <b>B3:</b> Bấm nút <b>'Kiểm tra ngay'</b>.</li>
            <li>👉 <b>B4:</b> Nhận cảnh báo từ AI.</li>
        </ul>
        """, unsafe_allow_html=True)
        styles.close_box()

    # HÀNG 2: THÔNG TIN QUY TẮC MẠNG
    styles.section_header("THÔNG TIN VỀ QUY TẮC TRÊN KHÔNG GIAN MẠNG")
    styles.open_box()
    k1, k2, k3 = st.columns(3)
    with k1:
        st.info("🚫 **5 KHÔNG:**\n1. Không chuyển tiền\n2. Không bấm link lạ\n3. Không nhập mật khẩu\n4. Không cài app lạ\n5. Không sợ hãi")
    with k2:
        st.success("✅ **3 NÊN:**\n1. Nên gọi xác thực\n2. Nên hỏi con cháu\n3. Nên báo công an (156)")
    with k3:
        st.warning("⚠️ **CẢNH BÁO:**\nTuyệt đối cảnh giác với các cuộc gọi video Deepfake giả mạo người thân.")
    styles.close_box()

    # HÀNG 3: ĐƠN VỊ ĐỒNG HÀNH (Layout Logo giống Olympic)
    styles.section_header("ĐƠN VỊ CHỨC NĂNG & ĐỒNG HÀNH")
    styles.open_box()
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="partner-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Logo_bo_cong_an.png/120px-Logo_bo_cong_an.png" width="60"><div class="partner-label">BỘ CÔNG AN</div></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="partner-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg/120px-Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg.png" width="60"><div class="partner-label">BỘ GD & ĐT</div></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="partner-img"><img src="https://tinnhiemmang.vn/handle_cert/images/logo.png" width="100"><div class="partner-label">TÍN NHIỆM MẠNG</div></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="partner-img"><img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" width="60"><div class="partner-label">SILVERSHIELD</div></div>', unsafe_allow_html=True)
    styles.close_box()


elif st.session_state['page'] == 'GIỚI THIỆU':
    styles.section_header("THÀNH VIÊN ĐỘI DVT - EMPIRE CBZ X")
    styles.open_box()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)
        st.markdown("**Thành viên 1**\n\n*Trưởng nhóm*")
    with c2:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140047.png", width=120)
        st.markdown("**Thành viên 2**\n\n*Nội dung*")
    with c3:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140037.png", width=120)
        st.markdown("**Thành viên 3**\n\n*Kỹ thuật*")
    styles.close_box()


elif st.session_state['page'] == 'TIN TỨC':
    styles.section_header("TIN TỨC AN NINH MẠNG")
    styles.open_box()
    st.markdown("""
    #### 📰 Bộ Công an cảnh báo 24 hình thức lừa đảo
    <small>Nguồn: Báo Chính Phủ</small>
    <p>Các đối tượng sử dụng công nghệ cao để chiếm đoạt tài sản...</p>
    <hr>
    #### 📰 Cẩm nang nhận diện Deepfake
    <small>Nguồn: Cục An toàn thông tin</small>
    <p>Dấu hiệu nhận biết: Khuôn mặt đơ cứng, giọng nói không tự nhiên...</p>
    """, unsafe_allow_html=True)
    styles.close_box()


elif st.session_state['page'] == 'VỆ SĨ SILVER':
    styles.section_header("TRUNG TÂM PHÂN TÍCH VỆ SĨ AI")
    
    col_in, col_out = st.columns([1, 1], gap="large")
    with col_in:
        styles.open_box()
        st.subheader("1. Nhập liệu")
        txt = st.text_area("Dán tin nhắn nghi ngờ:", height=150)
        img = st.file_uploader("Tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        
        if st.button("🔍 PHÂN TÍCH NGAY", type="primary", use_container_width=True):
            if txt or img:
                with st.spinner("Đang xử lý..."):
                    img_data = Image.open(img) if img else None
                    st.session_state['res'] = logic.analyze_content(model, txt, img_data)
        styles.close_box()
        
    with col_out:
        styles.open_box()
        st.subheader("2. Kết quả")
        if 'res' in st.session_state:
            st.success("Đã có kết quả!")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("Vui lòng nhập dữ liệu để kiểm tra.")
        styles.close_box()

# --- 5. FOOTER (CHÂN TRANG) ---
st.markdown("""
    <div class="footer-container">
        <h2>SILVERSHIELD</h2>
        <p>"Vì một không gian mạng an toàn"</p>
        <br>
        <p style="font-size:12px;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
    </div>
""", unsafe_allow_html=True)
