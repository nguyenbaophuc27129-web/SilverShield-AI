import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. SETUP ---
st.set_page_config(layout="wide", page_title="SilverShield Olympic", page_icon="🛡️")
styles.apply_styles()

# --- 2. HEADER COMPLEX (Top Bar + Navbar + Logo Treo) ---
styles.render_top_bar()

# Navbar Container (Chứa menu bên phải)
st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
# Sử dụng columns để đặt menu lệch phải
# Cột 1: Spacer (để chừa chỗ cho logo), Cột 2: Menu
c_spacer, c_menu = st.columns([2, 8]) 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

with c_menu:
    # Menu ngang
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("🏠 TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("VỆ SĨ AI", use_container_width=True): st.session_state['page'] = 'VỆ SĨ AI'
st.markdown('</div>', unsafe_allow_html=True)

# Logo treo (Render sau navbar để đè lên trên)
styles.render_hanging_logo()

# Dòng chữ chạy (Marquee)
styles.render_marquee()


# --- 3. NỘI DUNG CHÍNH ---

# ==================== TRANG CHỦ ====================
if st.session_state['page'] == 'TRANG CHỦ':
    
    # --- A. BANNER HERO SECTION (Quan trọng) ---
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    # Chữ STEM chìm nền
    st.markdown('<div class="bg-text-stem">STEM</div>', unsafe_allow_html=True)
    
    # Grid 70% - 30%
    h_left, h_right = st.columns([7, 3])
    
    with h_left:
        # Phần này để trống hoặc chèn ảnh minh họa trong suốt nếu muốn
        # st.image("link_anh_minh_hoa_trong_suot.png")
        st.write("") # Placeholder
        
    with h_right:
        # Khối Vệ sĩ SILVER (Glassmorphism)
        st.markdown("""
        <div class="glass-box">
            <h2 style="margin:0 0 15px 0; font-weight:400; letter-spacing:1px;">Vệ sĩ SILVER</h2>
            <div style="font-size:40px; margin-bottom:20px;">🛡️</div>
        </div>
        """, unsafe_allow_html=True)
        # Nút bấm (dùng st.button để bắt sự kiện)
        st.markdown('<div class="btn-check-now">', unsafe_allow_html=True)
        if st.button("🌐 KIỂM TRA NGAY"):
            st.session_state['page'] = 'VỆ SĨ AI'
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # End hero-section


    # --- B. INTRO & HƯỚNG DẪN (2 Cột) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    intro_col, guide_col = st.columns(2, gap="large")
    
    with intro_col:
        # Header đỏ
        st.markdown("""
            <div style="text-align:center; height: 20px; border-bottom: 1px solid #e0e0e0; margin-bottom: 30px;">
                <span style="background:white; padding:0 15px; color:#D32F2F; font-weight:bold; font-size:18px;">VỀ ỨNG DỤNG SILVERSHIELD</span>
            </div>
            <div style="text-align:justify; color:#555; line-height:1.6;">
                SilverShield là ứng dụng AI tiên phong giúp người cao tuổi phát hiện tin nhắn lừa đảo. 
                Với công nghệ xử lý ngôn ngữ tự nhiên, chúng tôi tạo ra lá chắn số vững chắc bảo vệ tài sản và tinh thần cho ông bà, cha mẹ.
            </div>
        """, unsafe_allow_html=True)
        
    with guide_col:
        # Header đỏ
        st.markdown("""
            <div style="text-align:center; height: 20px; border-bottom: 1px solid #e0e0e0; margin-bottom: 30px;">
                <span style="background:white; padding:0 15px; color:#D32F2F; font-weight:bold; font-size:18px;">HƯỚNG DẪN SỬ DỤNG</span>
            </div>
            <div style="background:#f9f9f9; padding:15px; border-radius:5px;">
                1. Chọn mục <b>"Vệ sĩ AI"</b> trên thanh menu.<br>
                2. Nhập văn bản hoặc tải ảnh cần kiểm tra.<br>
                3. Nhấn nút <b>"Phân tích"</b> và đợi kết quả.<br>
            </div>
        """, unsafe_allow_html=True)


    # --- C. QUY TẮC AN TOÀN (3 Cột) ---
    st.markdown("""
        <div class="rules-header">
            <span>💻</span> CÁC QUY TẮC AN TOÀN TRÊN KHÔNG GIAN MẠNG
        </div>
    """, unsafe_allow_html=True)
    
    r1, r2, r3 = st.columns(3, gap="medium")
    
    # Hàm tạo thẻ quy tắc
    def rule_card(title, color_class, items):
        html_items = "".join([f"<div class='rule-item'>{idx+1}. {item}</div>" for idx, item in enumerate(items)])
        st.markdown(f"""
            <div style="margin-top:20px;">
                <div class="rule-card-header {color_class}">{title}</div>
                <div class="rule-card-body">{html_items}</div>
            </div>
        """, unsafe_allow_html=True)

    with r1: rule_card("5 KHÔNG", "bg-red", ["Không chuyển tiền lạ", "Không bấm link lạ", "Không cung cấp OTP", "Không cài app lạ", "Không sợ hãi"])
    with r2: rule_card("3 NÊN", "bg-green", ["Nên gọi xác thực", "Nên hỏi con cháu", "Nên báo cơ quan (156)"])
    with r3: rule_card("LƯU Ý", "bg-teal", ["Cập nhật kiến thức", "Bảo mật mật khẩu", "Kiểm tra tài khoản"])


    # --- D. TIN TỨC (Lưới 3x2) ---
    st.markdown("""
        <div class="news-header-bar">
            <div class="news-header-text">TIN TỨC</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Hàm tạo thẻ tin tức
    def news_card_item(img_link, title):
        st.markdown(f"""
        <div class="news-card">
            <div class="news-thumb" style="background-image: url('{img_link}');"></div>
            <div class="news-content">
                <div class="news-title">🚀 {title}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Hàng 1
    n1, n2, n3 = st.columns(3)
    with n1: news_card_item("https://img.freepik.com/free-vector/hacker-activity-concept_23-2148532952.jpg", "Cảnh báo thủ đoạn giả danh công an")
    with n2: news_card_item("https://img.freepik.com/free-vector/phishing-account-concept_23-2148532258.jpg", "Lừa đảo 'Con cấp cứu' quay trở lại")
    with n3: news_card_item("https://img.freepik.com/free-vector/internet-security-concept_23-2148532259.jpg", "Cách bảo vệ tài khoản ngân hàng")
    
    # Hàng 2
    n4, n5, n6 = st.columns(3)
    with n4: news_card_item("https://img.freepik.com/free-vector/cyber-security-concept_23-2148532255.jpg", "Chiêu trò tuyển CTV online")
    with n5: news_card_item("https://img.freepik.com/free-vector/global-data-security-personal-data-security-cyber-data-security-online-concept-illustration_1150-37336.jpg", "Cẩm nang an toàn số 2026")
    with n6: news_card_item("https://img.freepik.com/free-vector/secure-data-concept-illustration_114360-483.jpg", "Đường dây nóng hỗ trợ 156")


# ==================== CÁC TRANG KHÁC (GIỮ NGUYÊN LOGIC) ====================
elif st.session_state['page'] == 'VỆ SĨ AI':
    # Copy logic trang Vệ sĩ AI vào đây (giữ nguyên code cũ hoặc bọc vào container)
    st.markdown('<div class="rules-header">TRUNG TÂM PHÂN TÍCH</div>', unsafe_allow_html=True)
    c_in, c_res = st.columns(2, gap="large")
    with c_in:
        txt = st.text_area("Nhập tin nhắn:", height=150)
        img = st.file_uploader("Tải ảnh:", type=['jpg','png'])
        if st.button("PHÂN TÍCH", type="primary"):
            # Gọi logic AI
            pass
    with c_res:
        st.info("Kết quả hiển thị tại đây")

# (Các trang Giới thiệu, Tin tức bạn copy logic tương tự)

# --- 4. FOOTER ---
styles.render_footer()
