import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO & ÉP FOOTER SÁT ĐÁY TUYỆT ĐỐI ---
styles.apply_styles()
styles.render_header_structure() 

# ĐOẠN CSS NÂNG CẤP GIAO DIỆN CHUYÊN NGHIỆP (GIỮ LẠI CƠ CHẾ CŨ)
st.markdown("""
    <style>
        /* Reset & Layout */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }
        footer {visibility: hidden !important; height: 0;}
        header {visibility: hidden !important;}

        .stApp {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background-color: #ffffff;
        }

        /* Typography */
        p, li, div { font-size: 16px; color: #444; }
        
        /* Hiệu ứng Card chuyên nghiệp */
        .pro-card {
            background: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
            border: 1px solid #f0f0f0;
            height: 100%;
        }
        .pro-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        /* Hero Section Styling */
        .hero-text-side {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 40px;
        }

        /* Xóa khoảng hở cuối trang */
        div[data-testid="stVerticalBlock"] > div:last-child {
            margin-bottom: 0px !important;
            padding-bottom: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR CHUẨN ---
st.markdown('<div class="olympic-navbar"><div class="navbar-container" style="width:1200px; margin:0 auto; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, m1, m2, m3, m4 = st.columns([1.5, 2, 2, 2, 2])

with c_logo:
    st.markdown('<img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:50px; margin-left:15px;">', unsafe_allow_html=True)

with m1:
    if st.button("🏠 TRANG CHỦ", use_container_width=True): 
        st.session_state['page'] = 'TRANG CHỦ'
        st.rerun()
with m2:
    if st.button("👥 GIỚI THIỆU", use_container_width=True): 
        st.session_state['page'] = 'GIỚI THIỆU'
        st.rerun()
with m3:
    if st.button("📰 TIN TỨC", use_container_width=True): 
        st.session_state['page'] = 'TIN TỨC'
        st.rerun()
with m4:
    if st.button("🛡️ VỆ SĨ AI", use_container_width=True): 
        st.session_state['page'] = 'VỆ SĨ AI'
        st.rerun()

st.markdown('</div></div>', unsafe_allow_html=True)

# --- 3. ĐIỀU HƯỚNG NỘI DUNG ---
main_body = st.container()

with main_body:
    if st.session_state['page'] == 'TRANG CHỦ':
        # --- HERO SECTION PHONG CÁCH "FOCUSON" ---
        hero_html = """
        <div style="width: 100%; background: #ffffff; padding: 60px 0; border-bottom: 1px solid #eee;">
            <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; gap: 40px;">
                <div style="flex: 1.2;" class="hero-text-side">
                    <h4 style="color: #8bc34a; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;">SILVERSHIELD AI</h4>
                    <h1 style="font-size: 48px; font-weight: 800; color: #222; line-height: 1.2; margin-bottom: 20px;">
                        HỆ THỐNG BẢO VỆ <br><span style="color: #8bc34a;">NGƯỜI CAO TUỔI</span>
                    </h1>
                    <p style="font-size: 18px; color: #666; line-height: 1.6; margin-bottom: 30px;">
                        Sử dụng trí tuệ nhân tạo tiên phong để phân tích, phát hiện và ngăn chặn các hành vi lừa đảo trực tuyến, bảo vệ sự an toàn cho cha mẹ và người thân của bạn.
                    </p>
                </div>
                <div style="flex: 1;">
                    <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png" 
                         style="width: 100%; border-radius: 15px; box-shadow: 20px 20px 60px #d9d9d9;">
                </div>
            </div>
        </div>
        """
        st.markdown(hero_html, unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # --- FEATURE SECTION ---
        st.markdown('<div style="max-width:1200px; margin:0 auto;">', unsafe_allow_html=True)
        c_intro, c_guide = st.columns(2, gap="large")
        with c_intro:
            st.markdown("""
                <div class="pro-card">
                    <h3 style="color: #222; border-bottom: 3px solid #8bc34a; display: inline-block; padding-bottom: 5px;">VỀ ỨNG DỤNG</h3>
                    <p style="margin-top: 15px; text-align: justify;">SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến cho người cao tuổi.</p>
                </div>
            """, unsafe_allow_html=True)
        with c_guide:
            st.markdown("""
                <div class="pro-card">
                    <h3 style="color: #222; border-bottom: 3px solid #0044cc; display: inline-block; padding-bottom: 5px;">HƯỚNG DẪN</h3>
                    <ul style="margin-top: 15px; list-style-type: none; padding-left: 0;">
                        <li style="margin-bottom: 10px;">🛡️ <b>Bước 1:</b> Chọn mục "Vệ sĩ AI"</li>
                        <li style="margin-bottom: 10px;">🔍 <b>Bước 2:</b> Nhập nội dung nghi ngờ</li>
                        <li>✅ <b>Bước 3:</b> Nhận kết quả từ AI</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # --- RULES SECTION ---
        st.markdown('<br><br><div style="max-width:1200px; margin:0 auto;">', unsafe_allow_html=True)
        st.markdown('<div class="rules-main-header" style="background: #222; color: white; padding: 15px; text-align: center; border-radius: 5px;">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
        r1, r2, r3 = st.columns(3, gap="medium")
        with r1:
            st.markdown('<div class="pro-card" style="border-top: 5px solid #d32f2f;"><h4 style="color:#d32f2f; text-align:center;">5 KHÔNG</h4><p style="font-weight:bold; line-height:1.8;">1. Không chuyển tiền<br>2. Không bấm link lạ<br>3. Không đưa OTP<br>4. Không cài app lạ<br>5. Không sợ đe dọa</p></div>', unsafe_allow_html=True)
        with r2:
            st.markdown('<div class="pro-card" style="border-top: 5px solid #2e7d32;"><h4 style="color:#2e7d32; text-align:center;">3 NÊN</h4><p style="font-weight:bold; line-height:1.8;">1. Nên gọi xác thực<br>2. Nên hỏi con cháu<br>3. Nên báo công an</p></div>', unsafe_allow_html=True)
        with r3:
            st.markdown('<div class="pro-card" style="border-top: 5px solid #0097a7;"><h4 style="color:#0097a7; text-align:center;">LƯU Ý</h4><p style="font-weight:bold; line-height:1.8;">1. Luôn bình tĩnh<br>2. Đọc tin an ninh<br>3. Dùng SilverShield</p></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # --- NEWS SECTION ---
        st.markdown('<br><br><div style="max-width:1200px; margin:0 auto;">', unsafe_allow_html=True)
        st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:15px; font-weight:bold; border-radius: 5px;">📰 TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
        news_data = [
            {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
            {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/canh-bao-thu-doan-lua-dao-bang-cong-nghe-deepfake-2023032711054321.htm"},
            {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/bay-viec-nhe-luong-cao-tren-mang-4478144.html"}
        ]
        cols = st.columns(3)
        for idx, item in enumerate(news_data):
            with cols[idx]:
                st.markdown(f'<div class="pro-card" style="padding:0; overflow:hidden;"><img src="{item["img"]}" style="width:100%; height:200px; object-fit:cover;"><div style="padding:15px;"><h5 style="font-weight:bold; min-height:50px;">{item["title"]}</h5></div></div>', unsafe_allow_html=True)
                st.link_button("CHI TIẾT", item['url'], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state['page'] == 'GIỚI THIỆU':
        st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN & SỨ MỆNH</div>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2, gap="large")
        with col_a:
            st.markdown('<div class="banner-strip"><div class="banner-header">SỨ MỆNH</div><p style="padding:20px; text-align:justify; color:#333;">SilverShield ra đời để bảo vệ người cao tuổi Việt Nam trước vấn nạn lừa đảo mạng ngày càng tinh vi. Chúng tôi cam kết sử dụng AI để tạo ra "lá chắn thép" cho mọi gia đình.</p></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="banner-strip"><div class="banner-header">ĐỘI NGŨ DVT</div><p style="padding:20px; text-align:justify; color:#333;">Đội ngũ Empire CBZ X hội tụ các cá nhân đam mê công nghệ tại THPT Dương Văn Thì, hướng tới những giải pháp vì cộng đồng.</p></div>', unsafe_allow_html=True)

    elif st.session_state['page'] == 'TIN TỨC':
        st.markdown('<div class="rules-main-header">📰 BẢN TIN AN NINH TOÀN CẢNH</div>', unsafe_allow_html=True)
        full_news = [
            {"title": "Lừa đảo qua video call Deepfake", "desc": "Đối tượng dùng AI giả khuôn mặt người thân để vay tiền gấp.", "tag": "CẢNH BÁO", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://vnexpress.net/thu-doan-lua-dao-video-call-deepfake-4586231.html"},
            {"title": "Tin nhắn giả danh ngân hàng", "desc": "Yêu cầu cập nhật thông tin qua link lạ để chiếm đoạt mã OTP.", "tag": "NGUY HIỂM", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
            {"title": "Cẩm nang phòng chống tội phạm", "desc": "Sổ tay hướng dẫn của Bộ Công An dành cho người dân và người cao tuổi.", "tag": "KIẾN THỨC", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://chinhphu.vn/canh-bao-24-hinh-thuc-lua-dao-tren-khong-gian-mang-103230713145455645.htm"}
        ]
        for idx, n in enumerate(full_news):
            c_img, c_txt = st.columns([1, 2.5])
            with c_img:
                st.image(n["img"], use_container_width=True)
            with c_txt:
                st.markdown(f"""
                    <div style="background:white; padding:15px; border-left:5px solid #d32f2f; margin-bottom:5px;">
                        <span style="background:#d32f2f; color:white; padding:2px 8px; font-size:12px; font-weight:bold;">{n['tag']}</span>
                        <h3 style="margin:10px 0;">{n['title']}</h3>
                        <p style="color:#333;">{n['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button("XEM BÁO CHÍNH THỐNG", n['url'])
            st.markdown("<hr>", unsafe_allow_html=True)

    elif st.session_state['page'] == 'VỆ SĨ AI':
        st.markdown('<div class="rules-main-header">🛡️ TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1], gap="large")
        with c1:
            txt = st.text_area("Nhập nội dung cần kiểm tra:", height=200)
            img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
            if st.button("PHÂN TÍCH NGAY", type="primary", use_container_width=True):
                if txt or img:
                    with st.spinner("AI đang quét dữ liệu..."):
                        i = Image.open(img) if img else None
                        st.session_state['res'] = logic.analyze_content(model, txt, i)
        with c2:
            if 'res' in st.session_state:
                st.success("KẾT QUẢ PHÂN TÍCH")
                st.write(st.session_state['res'])
                st.audio(logic.text_to_speech(st.session_state['res']))
            else: st.info("Kết quả hiển thị tại đây.")

# --- 4. FOOTER KHÓA CHẶT ĐÁY ---
styles.render_footer_structure()
