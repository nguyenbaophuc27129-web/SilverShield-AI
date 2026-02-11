import streamlit as st
from PIL import Image
import styles
import logic

# 1. Khởi tạo
styles.apply_styles()
styles.header_component()
model = logic.init_ai()

# 2. Sidebar Navigation
with st.sidebar:
    # Sau này bạn thay link ảnh logo của bạn vào đây
    st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=120)
    st.markdown("<h2 style='text-align: center;'>SILVERSHIELD</h2>", unsafe_allow_html=True)
    page = st.radio("CHỌN CHỨC NĂNG", ["🏠 Trang Chủ", "🛡️ Vệ Sĩ AI", "📰 Tin Tức Cảnh Báo"])

# --- TRANG CHỦ ---
if page == "🏠 Trang Chủ":
    st.markdown("<h1 style='color:#002147;'>🛡️ SILVERSHIELD</h1>", unsafe_allow_html=True)
    # Banner chính (Sau này bạn thay link ảnh banner xịn vào)
    st.image("https://baochinhphu.vn/Uploaded/tranducmanh/2023_03_14/lua-dao-con-cap-cuu-2.jpg", use_container_width=True)
    
    st.markdown("""
    <div class="content-card">
        <h3>Chào mừng Ông Bà đến với Hệ thống Bảo vệ!</h3>
        <p style='font-size:20px;'>SilverShield sử dụng trí tuệ nhân tạo (AI) để giúp người cao tuổi 
        phát hiện các hành vi lừa đảo qua tin nhắn và hình ảnh.</p>
    </div>
    """, unsafe_allow_html=True)

# --- TRANG VỆ SĨ AI ---
elif page == "🛡️ Vệ Sĩ AI":
    st.markdown("<h1 style='color:#002147;'>🛡️ TRUNG TÂM PHÂN TÍCH AI</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.subheader("📥 Gửi thông tin")
        user_text = st.text_area("Dán tin nhắn nghi ngờ vào đây:", height=150)
        u_file = st.file_uploader("Hoặc gửi ảnh chụp màn hình:", type=['jpg','png','jpeg'])
        
        if st.button("🔍 KIỂM TRA NGAY"):
            if user_text or u_file:
                with st.spinner("Đang xử lý..."):
                    img = Image.open(u_file) if u_file else None
                    res = logic.analyze_content(model, user_text, img)
                    st.session_state['result'] = res
            else: st.warning("Bà ơi, hãy nhập thông tin nhé!")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.subheader("📤 Kết quả từ cháu SilverShield")
        if 'result' in st.session_state:
            res = st.session_state['result']
            st.write(res)
            audio = logic.text_to_speech(res)
            st.audio(audio, format='audio/mp3')
        else:
            st.info("Cháu đang đợi tin nhắn từ bà ạ...")
        st.markdown("</div>", unsafe_allow_html=True)

# --- TRANG TIN TỨC (Dẫn link ra ngoài) ---
elif page == "📰 Tin Tức Cảnh Báo":
    st.markdown("<h1 style='color:#002147;'>📰 TIN TỨC & CẢNH BÁO</h1>", unsafe_allow_html=True)
    
    def news_item(title, summary, link):
        st.markdown(f"""
            <div class="news-card">
                <a class="news-link" href="{link}" target="_blank">{title}</a>
                <p style='margin-top:10px;'>{summary}</p>
                <a href="{link}" target="_blank" style='color:#D32F2F;'>Xem chi tiết trên Báo Chính Phủ →</a>
            </div>
        """, unsafe_allow_html=True)

    # Các bài báo link trực tiếp ra ngoài
    news_item(
        "Cảnh báo lừa đảo chiếm đoạt tài sản qua mạng",
        "Bộ Công an cảnh báo các thủ đoạn giả danh cơ quan tư pháp gọi điện đe dọa người dân...",
        "https://baochinhphu.vn/canh-bao-cac-thu-doan-lua-dao-truc-tuyen-moi-10223032415254247.htm"
    )
    
    news_item(
        "Nhận diện 24 hình thức lừa đảo trên không gian mạng",
        "Cục An toàn thông tin cung cấp cẩm nang giúp người dân phòng tránh bẫy lừa đảo...",
        "https://tinnhiemmang.vn/canh-bao"
    )

    st.info("💡 Ông bà hãy bấm vào tiêu đề để đọc báo chi tiết ạ!")
