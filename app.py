import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
styles.apply_styles()
styles.render_top_bar() # Gọi hàm hiển thị thanh trên cùng
try:
    model = logic.init_ai()
except:
    pass

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. HERO BANNER (Full width) ---
# Thay ảnh banner của bạn vào đây
st.image("https://github.com/nguyenbaophuc27129-web/SilverShield-AI/blob/5befa8d1b793de0b6934f56af0f4458a8967457b/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png", use_container_width=True)

# --- 3. MENU NAVIGATION (Thanh trắng nằm dưới Banner) ---
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
# Chia cột: Logo (1) | Menu (5) | Kiểm tra (2)
c_logo, c_menu, c_btn = st.columns([1, 5, 2])

with c_logo:
    # Logo tròn
    st.image("https://github.com/nguyenbaophuc27129-web/SilverShield-AI/blob/5befa8d1b793de0b6934f56af0f4458a8967457b/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png", width=60)

with c_menu:
    # Menu ngang
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("VỆ SĨ SILVER", use_container_width=True): st.session_state['page'] = 'VỆ SĨ SILVER'

with c_btn:
    # Nút nổi bật
    if st.button("🚀 KIỂM TRA NGAY", type="primary", use_container_width=True):
        st.session_state['page'] = 'VỆ SĨ SILVER'
st.markdown('</div>', unsafe_allow_html=True)


# --- 4. NỘI DUNG CHÍNH (BODY) ---

# ============ TRANG CHỦ ============
if st.session_state['page'] == 'TRANG CHỦ':
    
    # ROW 1: TỔNG QUAN (Về dự án + Hướng dẫn)
    st.markdown('<div class="section-header">TỔNG QUAN DỰ ÁN</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1.6, 1], gap="medium")
    
    with c1:
        st.markdown("""
        <div class="olympic-card">
            <div class="card-title-blue">🛡️ Về SilverShield</div>
            <p style="text-align: justify; color: #555; font-size: 15px;">
                <b>SilverShield</b> là giải pháp công nghệ tiên phong dành riêng cho người cao tuổi, 
                đóng vai trò như một "lớp khiên bạc" bảo vệ ông bà, cha mẹ trước làn sóng lừa đảo trực tuyến.
                <br><br>
                Sử dụng trí tuệ nhân tạo (AI) thế hệ mới, chúng tôi giúp phân tích tin nhắn, hình ảnh để đưa ra cảnh báo tức thì.
            </p>
            <div style="display:flex; gap:10px; margin-top:15px;">
                <div style="background:#e3f2fd; padding:10px; border-radius:5px; flex:1;">
                    <b>🎯 Sứ mệnh</b><br><small>Xóa bỏ khoảng cách số</small>
                </div>
                <div style="background:#e3f2fd; padding:10px; border-radius:5px; flex:1;">
                    <b>🚀 Tầm nhìn</b><br><small>Ứng dụng quốc dân 2026</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="olympic-card">
            <div class="card-title-blue">📖 Hướng dẫn nhanh</div>
            <ul class="custom-list">
                <li>1️⃣ Chọn Tab <b>"Vệ sĩ Silver"</b>.</li>
                <li>2️⃣ Dán tin nhắn hoặc chụp ảnh màn hình.</li>
                <li>3️⃣ Bấm nút <b>"Kiểm tra"</b> màu đỏ.</li>
                <li>4️⃣ Nghe lời khuyên từ AI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # ROW 2: THÔNG TIN & QUY TẮC (Tin tức + 5 Không + 3 Nên)
    st.markdown('<div class="section-header">THÔNG TIN & QUY TẮC AN TOÀN</div>', unsafe_allow_html=True)
    n1, n2, n3 = st.columns(3, gap="medium")
    
    with n1: # Cột Tin Tức
        st.markdown("""
        <div class="olympic-card">
            <div class="card-title-blue">📰 Tin tức nổi bật</div>
            <ul class="custom-list">
                <li>🔥 Cảnh báo thủ đoạn giả danh công an gọi video...</li>
                <li>🔥 Lừa đảo "con cấp cứu" tái xuất hiện...</li>
                <li>🔥 Chiêu trò tuyển CTV việc nhẹ lương cao...</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with n2: # Cột 5 Không
        st.markdown("""
        <div class="olympic-card">
            <div class="card-title-red">⛔ 5 KHÔNG</div>
            <ul class="custom-list">
                <li>❌ Không chuyển tiền cho người lạ.</li>
                <li>❌ Không bấm vào link lạ.</li>
                <li>❌ Không cung cấp mã OTP.</li>
                <li>❌ Không cài app không rõ nguồn.</li>
                <li>❌ Không sợ hãi trước lời đe dọa.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with n3: # Cột 3 Nên
        st.markdown("""
        <div class="olympic-card">
            <div class="card-title-cyan">✅ 3 NÊN</div>
            <ul class="custom-list">
                <li>📞 Nên gọi điện xác thực lại.</li>
                <li>👨‍👩‍👧‍👦 Nên hỏi ý kiến con cháu.</li>
                <li>👮 Nên báo cơ quan chức năng (156).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ============ TRANG VỆ SĨ SILVER ============
elif st.session_state['page'] == 'VỆ SĨ SILVER':
    st.markdown('<div class="section-header">TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
    
    c_in, c_out = st.columns([1, 1], gap="large")
    with c_in:
        st.markdown('<div class="olympic-card">', unsafe_allow_html=True)
        st.subheader("1. Nhập thông tin")
        txt = st.text_area("Dán tin nhắn vào đây:", height=150)
        img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
        if st.button("🔍 PHÂN TÍCH NGAY", type="primary", use_container_width=True):
            if txt or img:
                with st.spinner("AI đang xử lý..."):
                    i = Image.open(img) if img else None
                    st.session_state['res'] = logic.analyze_content(model, txt, i)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c_out:
        st.markdown('<div class="olympic-card" style="background:#f1f8e9; border-color:#81c784;">', unsafe_allow_html=True)
        st.subheader("2. Kết quả")
        if 'res' in st.session_state:
            st.success("Đã có kết quả!")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("👈 Hãy nhập liệu để kiểm tra.")
        st.markdown('</div>', unsafe_allow_html=True)


# ============ TRANG GIỚI THIỆU ============
elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="section-header">ĐỘI NGŨ PHÁT TRIỂN</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="olympic-card" style="text-align:center;"><h3>Thành viên 1</h3><p>Trưởng nhóm</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="olympic-card" style="text-align:center;"><h3>Thành viên 2</h3><p>Nội dung</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="olympic-card" style="text-align:center;"><h3>Thành viên 3</h3><p>Thiết kế</p></div>', unsafe_allow_html=True)


# ============ TRANG TIN TỨC ============
elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="section-header">TIN TỨC CHÍNH THỐNG</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="olympic-card">
        <h3>🚨 Cảnh báo Lừa đảo trực tuyến 2026</h3>
        <p>Cập nhật các hình thức lừa đảo mới nhất từ Bộ Công An...</p>
    </div>
    """, unsafe_allow_html=True)


# --- 5. FOOTER ---
st.markdown("""
    <div class="footer-container">
        <h2 style="margin:0;">SILVERSHIELD</h2>
        <p><i>"Vì một không gian mạng an toàn"</i></p>
        <p style="font-size: 13px; margin-top: 20px;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
    </div>
""", unsafe_allow_html=True)
