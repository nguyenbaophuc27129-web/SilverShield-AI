import streamlit as st
from PIL import Image
import styles
import logic

# --- KHỞI TẠO ---
styles.apply_styles()
styles.render_top_bar()
try:
    model = logic.init_ai()
except:
    pass

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# ==================== PHẦN HEADER & MENU ====================
# Tạo container trắng cho Menu
st.markdown('<div class="nav-wrapper"><div class="nav-content">', unsafe_allow_html=True)
c_logo, c_menu = st.columns([1.5, 8.5])

with c_logo:
    # Logo tròn bên trái (Thay link logo của bạn vào đây)
    st.markdown('<div style="display:flex; align-items:center; height:100%;"><img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" width="60"></div>', unsafe_allow_html=True)

with c_menu:
    # Menu ngang thẳng hàng
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("VỆ SĨ SILVER", use_container_width=True): st.session_state['page'] = 'VỆ SĨ SILVER'

st.markdown('</div></div>', unsafe_allow_html=True) # Đóng thẻ nav


# ==================== PHẦN HERO SECTION (BANNER + NỀN) ====================
# Chỉ hiện ở Trang chủ
if st.session_state['page'] == 'TRANG CHỦ':
    st.markdown('<div class="hero-section"><div class="hero-overlay"></div><div class="hero-content">', unsafe_allow_html=True)
    
    # Chia 2 cột: Banner Lớn bên trái - Hộp chức năng bên phải
    h1, h2 = st.columns([2.5, 1])
    
    with h1:
        # Ảnh Banner Lớn (Thay link banner thiết kế của bạn vào)
        st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True)
        
    with h2:
        # Khối đen mờ bên phải (Giống khối 'Bắt đầu thi' của Olympic)
        st.markdown("""
        <div class="glass-box">
            <h3 style="margin:0; color:white;">BẮT ĐẦU NGAY</h3>
            <p style="font-size:14px; opacity:0.9;">Kiểm tra độ an toàn của tin nhắn</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 KIỂM TRA", type="primary", use_container_width=True):
             st.session_state['page'] = 'VỆ SĨ SILVER'

    st.markdown('</div></div>', unsafe_allow_html=True) # Đóng thẻ hero


# ==================== NỘI DUNG CHÍNH (BODY) ====================
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# --- TRANG CHỦ ---
if st.session_state['page'] == 'TRANG CHỦ':
    
    # Mục 1: Về SilverShield
    st.markdown('<div class="section-header">VỀ DỰ ÁN SILVERSHIELD</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1], gap="medium")
    with c1:
        st.markdown("""
        <div style="background:white; padding:20px; border:1px solid #ddd; border-radius:5px;">
            <p style="font-size:16px; line-height:1.6; color:#333;">
                <b>SilverShield</b> là giải pháp công nghệ tiên phong dành riêng cho người cao tuổi. 
                Chúng tôi sử dụng AI để tạo ra một lá chắn bảo vệ ông bà, cha mẹ trước các thủ đoạn lừa đảo tinh vi.
            </p>
            <ul style="color:#003366; font-weight:500;">
                <li>✅ Phân tích tin nhắn lừa đảo bằng AI</li>
                <li>✅ Cảnh báo bằng giọng nói dễ hiểu</li>
                <li>✅ Giao diện đơn giản, chữ to, rõ ràng</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.info("💡 **HƯỚNG DẪN SỬ DỤNG**\n\n1. Chọn 'Vệ sĩ Silver'\n2. Dán tin nhắn/ảnh\n3. Bấm Kiểm tra")

    # Mục 2: Tin tức & Quy tắc
    st.markdown('<br><div class="section-header">TIN TỨC & QUY TẮC AN TOÀN</div>', unsafe_allow_html=True)
    n1, n2, n3 = st.columns(3, gap="medium")
    
    with n1:
        st.markdown("""<div class="news-card">
            <h4 style="color:#d32f2f; margin:0;">🔥 CẢNH BÁO MỚI</h4><hr>
            <p>Thủ đoạn giả danh công an gọi video call...</p>
        </div>""", unsafe_allow_html=True)
    with n2:
        st.markdown("""<div class="news-card">
            <h4 style="color:#003366; margin:0;">⛔ 5 KHÔNG</h4><hr>
            <p>1. Không chuyển tiền<br>2. Không bấm link lạ...</p>
        </div>""", unsafe_allow_html=True)
    with n3:
        st.markdown("""<div class="news-card">
            <h4 style="color:#003366; margin:0;">✅ 3 NÊN</h4><hr>
            <p>1. Gọi xác thực<br>2. Hỏi con cháu<br>3. Báo công an (156)</p>
        </div>""", unsafe_allow_html=True)


# --- TRANG VỆ SĨ SILVER ---
elif st.session_state['page'] == 'VỆ SĨ SILVER':
    st.markdown('<div class="section-header">TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
    
    col_input, col_res = st.columns([1, 1], gap="large")
    with col_input:
        st.markdown('<div style="background:white; padding:20px; border-radius:8px; border:1px solid #ddd;">', unsafe_allow_html=True)
        st.subheader("1. Nhập thông tin")
        txt = st.text_area("Dán tin nhắn vào đây:", height=150)
        img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
        if st.button("🔍 PHÂN TÍCH NGAY", type="primary", use_container_width=True):
            if txt or img:
                with st.spinner("AI đang quét dữ liệu..."):
                    i = Image.open(img) if img else None
                    st.session_state['res'] = logic.analyze_content(model, txt, i)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_res:
        st.markdown('<div style="background:#f1f8e9; padding:20px; border-radius:8px; border:1px solid #81c784; height:100%;">', unsafe_allow_html=True)
        st.subheader("2. Kết quả")
        if 'res' in st.session_state:
            st.success("Đã có kết quả!")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("👈 Hãy nhập dữ liệu bên trái.")
        st.markdown('</div>', unsafe_allow_html=True)


# --- TRANG GIỚI THIỆU ---
elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="section-header">ĐỘI NGŨ DVT - EMPIRE CBZ X</div>', unsafe_allow_html=True)
    t1, t2, t3 = st.columns(3)
    # Thay link ảnh của 3 bạn vào đây
    with t1: st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=150, caption="Thành viên 1")
    with t2: st.image("https://cdn-icons-png.flaticon.com/512/4140/4140047.png", width=150, caption="Thành viên 2")
    with t3: st.image("https://cdn-icons-png.flaticon.com/512/4140/4140037.png", width=150, caption="Thành viên 3")


# --- TRANG TIN TỨC ---
elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="section-header">TIN TỨC CHÍNH THỐNG</div>', unsafe_allow_html=True)
    st.info("Đang cập nhật dữ liệu từ Cục An toàn thông tin...")

st.markdown('</div>', unsafe_allow_html=True) # Đóng content-wrapper

# --- FOOTER ---
st.markdown("""
    <div style="background:#003366; color:white; padding:40px 0; text-align:center; margin-top:50px; border-top:5px solid #d32f2f;">
        <h2 style="margin:0;">SILVERSHIELD</h2>
        <p>Vì một không gian mạng an toàn</p>
        <p style="font-size:13px; margin-top:20px; opacity:0.7;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
    </div>
""", unsafe_allow_html=True)
