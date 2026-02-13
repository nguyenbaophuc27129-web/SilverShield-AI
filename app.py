import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. SETUP HỆ THỐNG ---
st.set_page_config(layout="wide", page_title="SilverShield - Vệ sĩ AI", page_icon="🛡️")
styles.apply_styles()
styles.render_top_bar()

# Init AI (Bỏ qua lỗi nếu chưa config key để demo giao diện)
try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR (MENU CHÍNH) ---
# Sử dụng container để tạo nền trắng
with st.container():
    # Grid: Logo (2) | Menu (8) | Button (2)
    c_logo, c_menu, c_cta = st.columns([2, 7, 3])
    
    with c_logo:
        # Logo + Tên thương hiệu
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px;">
            <img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" width="50">
            <span style="font-weight: 800; font-size: 22px; color: #0c3c78; letter-spacing: -0.5px;">SILVERSHIELD</span>
        </div>
        """, unsafe_allow_html=True)
        
    with c_menu:
        # Menu canh giữa
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            if st.button("TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
        with m2:
            if st.button("GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
        with m3:
            if st.button("TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
        with m4:
            if st.button("VỆ SĨ SILVER", use_container_width=True): st.session_state['page'] = 'VỆ SĨ SILVER'
            
    with c_cta:
        # Nút CTA nổi bật
        st.markdown('<div class="btn-cta">', unsafe_allow_html=True)
        if st.button("KIỂM TRA NGAY", use_container_width=True):
            st.session_state['page'] = 'VỆ SĨ SILVER'
        st.markdown('</div>', unsafe_allow_html=True)

# Đường kẻ phân cách menu
st.markdown("<div style='height: 1px; background: #eee; margin-bottom: 20px;'></div>", unsafe_allow_html=True)


# --- 3. NỘI DUNG CHÍNH ---

# ==================== TRANG CHỦ ====================
if st.session_state['page'] == 'TRANG CHỦ':
    
    # HERO SECTION (Gradient Blue)
    st.markdown("""
        <div class="hero-bg">
            <div style="display: flex; align-items: center;">
                <div style="flex: 1;">
                    <div class="hero-title">TRUNG TÂM PHÂN TÍCH AI<br>BẢO VỆ KHÔNG GIAN MẠNG</div>
                    <div class="hero-desc">SilverShield sử dụng trí tuệ nhân tạo để phân tích tin nhắn, phát hiện lừa đảo và bảo vệ người cao tuổi khỏi các mối đe dọa số.</div>
                </div>
                <div style="flex: 0.5; display: flex; justify-content: center;">
                    <img src="https://cdn-icons-png.flaticon.com/512/2040/2040504.png" width="200" style="opacity: 0.9;">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # WHY CHOOSE US
    st.markdown('<div class="section-title">TẠI SAO CHỌN SILVERSHIELD?</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Giải pháp toàn diện được tin dùng bởi cộng đồng</div>', unsafe_allow_html=True)
    
    w1, w2, w3 = st.columns(3, gap="medium")
    with w1:
        st.markdown("""
        <div class="clean-card">
            <img src="https://cdn-icons-png.flaticon.com/512/8655/8655268.png" width="50">
            <h3 style="color:#0c3c78; margin-top: 15px;">Phân tích AI 24/7</h3>
            <p style="color:#666;">Hệ thống hoạt động liên tục, phân tích ngôn ngữ tự nhiên để phát hiện dấu hiệu lừa đảo trong tích tắc.</p>
        </div>
        """, unsafe_allow_html=True)
    with w2:
        st.markdown("""
        <div class="clean-card">
            <img src="https://cdn-icons-png.flaticon.com/512/11502/11502421.png" width="50">
            <h3 style="color:#0c3c78; margin-top: 15px;">Dễ sử dụng</h3>
            <p style="color:#666;">Giao diện tối giản, cỡ chữ lớn, thao tác một chạm được thiết kế riêng cho người cao tuổi.</p>
        </div>
        """, unsafe_allow_html=True)
    with w3:
        st.markdown("""
        <div class="clean-card">
            <img src="https://cdn-icons-png.flaticon.com/512/9402/9402280.png" width="50">
            <h3 style="color:#0c3c78; margin-top: 15px;">Cảnh báo giọng nói</h3>
            <p style="color:#666;">Tích hợp trợ lý ảo đọc kết quả cảnh báo, giúp người dùng không cần đọc văn bản dài.</p>
        </div>
        """, unsafe_allow_html=True)

    # ĐỐI TÁC
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">ĐƠN VỊ ĐỒNG HÀNH</div>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    with p1: st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Logo_bo_cong_an.png/120px-Logo_bo_cong_an.png", width=80)
    with p2: st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg/120px-Logo_Bo_Giao_duc_va_Dao_tao_%28Viet_Nam%29.svg.png", width=80)
    with p3: st.image("https://tinnhiemmang.vn/handle_cert/images/logo.png", width=120)
    with p4: st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=80)


# ==================== VỆ SĨ SILVER (Trang quan trọng nhất) ====================
elif st.session_state['page'] == 'VỆ SĨ SILVER':
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">TRUNG TÂM PHÂN TÍCH</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">Dán tin nhắn hoặc tải ảnh để AI kiểm tra ngay lập tức</p>', unsafe_allow_html=True)
    
    # Giao diện AI đặt trong 1 khối thống nhất (Container)
    st.markdown('<div class="ai-container">', unsafe_allow_html=True)
    
    ai_col1, ai_col2 = st.columns([1.2, 1], gap="large")
    
    with ai_col1:
        st.subheader("1. Nhập thông tin")
        user_text = st.text_area("Dán nội dung tin nhắn:", height=200, placeholder="Ví dụ: Chúc mừng bạn đã trúng thưởng SH...")
        uploaded_file = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Nút phân tích Gradient
        st.markdown('<div class="btn-cta">', unsafe_allow_html=True)
        if st.button("🔍 PHÂN TÍCH NGAY", key="analyze_btn", use_container_width=True):
            if user_text or uploaded_file:
                with st.spinner("AI đang quét dữ liệu..."):
                    try:
                        img = Image.open(uploaded_file) if uploaded_file else None
                        st.session_state['result'] = logic.analyze_content(model, user_text, img)
                    except Exception as e:
                        st.error("Lỗi hệ thống AI.")
            else:
                st.warning("Vui lòng nhập thông tin!")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with ai_col2:
        st.subheader("2. Kết quả phân tích")
        if 'result' in st.session_state:
            # Hiển thị kết quả trong box đẹp
            st.markdown(f"""
            <div class="result-box">
                <h4 style="color:#0c3c78; margin-top:0;">💡 Đánh giá của SilverShield:</h4>
                <p style="font-size:16px;">{st.session_state['result']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.caption("🔊 Nghe trợ lý ảo đọc:")
            try:
                st.audio(logic.text_to_speech(st.session_state['result']))
            except:
                pass
        else:
            # Placeholder khi chưa có kết quả
            st.info("👈 Kết quả sẽ hiển thị tại đây sau khi bạn bấm phân tích.")
            st.image("https://cdn-icons-png.flaticon.com/512/10606/10606037.png", width=150)

    st.markdown('</div>', unsafe_allow_html=True) # End AI Container
    st.markdown('</div>', unsafe_allow_html=True)


# ==================== GIỚI THIỆU ====================
elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="section-title">ĐỘI NGŨ PHÁT TRIỂN</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">DVT - Empire CBZ X | THPT Dương Văn Thì</div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns(3, gap="medium")
    
    # Team Card Template
    def team_card(img, name, role):
        st.markdown(f"""
        <div class="clean-card" style="text-align:center;">
            <img src="{img}" style="width:100px; height:100px; border-radius:50%; object-fit:cover; border: 3px solid #0c3c78;">
            <h3 style="color:#0c3c78; margin: 15px 0 5px 0;">{name}</h3>
            <span style="background:#e3f2fd; color:#0c3c78; padding: 4px 12px; border-radius:20px; font-size:12px; font-weight:600;">{role}</span>
        </div>
        """, unsafe_allow_html=True)

    with t1: team_card("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", "Thành viên 1", "Trưởng nhóm")
    with t2: team_card("https://cdn-icons-png.flaticon.com/512/4140/4140047.png", "Thành viên 2", "Nội dung AI")
    with t3: team_card("https://cdn-icons-png.flaticon.com/512/4140/4140037.png", "Thành viên 3", "Thiết kế")


# ==================== TIN TỨC ====================
elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="section-title">TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("""
        <div class="clean-card">
            <span style="color:#d32f2f; font-weight:bold;">🔥 MỚI NHẤT</span>
            <h3>Cảnh báo hình thức lừa đảo "Con đang cấp cứu"</h3>
            <p style="color:#666;">Các đối tượng sử dụng AI để giả mạo giọng nói, gọi điện cho phụ huynh yêu cầu chuyển tiền gấp...</p>
            <a href="#" style="color:#0c3c78; font-weight:bold;">Đọc tiếp &rarr;</a>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="clean-card">
            <span style="color:#0c3c78; font-weight:bold;">🛡️ KIẾN THỨC</span>
            <h3>Cẩm nang nhận diện 24 hình thức lừa đảo</h3>
            <p style="color:#666;">Bộ Thông tin và Truyền thông phát hành bộ cẩm nang giúp người dân phòng tránh các bẫy lừa đảo...</p>
            <a href="#" style="color:#0c3c78; font-weight:bold;">Đọc tiếp &rarr;</a>
        </div>
        """, unsafe_allow_html=True)


# --- 4. FOOTER ---
styles.render_footer()
