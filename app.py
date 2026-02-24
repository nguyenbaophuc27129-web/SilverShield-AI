import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO & CẤU HÌNH GIAO DIỆN ---
styles.apply_styles()
styles.render_header_structure() 

# NÂNG CẤP CSS ĐỂ GIỐNG MẪU "FOCUSON" VÀ FIX FOOTER
st.markdown("""
    <style>
        /* Reset Layout */
        .main .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        footer {visibility: hidden !important;}
        header {visibility: hidden !important;}

        /* Navbar Gọn Đẹp */
        .stButton > button {
            border: none !important;
            background: transparent !important;
            color: #555 !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            text-transform: uppercase;
            transition: 0.3s;
        }
        .stButton > button:hover {
            color: #8bc34a !important; /* Màu xanh lá Focuson */
        }

        /* Banner Hero Section (Giống mẫu Focuson) */
        .hero-container {
            background-color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 80px 10%;
            min-height: 500px;
        }
        .hero-text {
            flex: 1;
            padding-right: 50px;
        }
        .hero-text h4 {
            color: #8bc34a;
            font-weight: 600;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }
        .hero-text h1 {
            font-size: 45px;
            font-weight: 800;
            line-height: 1.2;
            color: #222;
        }
        .hero-image {
            flex: 1;
            position: relative;
        }
        .hero-image img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 20px 20px 60px rgba(0,0,0,0.1);
        }

        /* Footer Cam (Giống mẫu Tuyệt Kỹ Powerpoint) */
        .custom-footer {
            background-color: #e65100;
            color: white;
            padding: 40px 10%;
            margin-top: 50px;
        }
        .footer-grid {
            display: grid;
            grid-template-columns: 1.5fr 1fr 1fr 1fr;
            gap: 30px;
        }
        .footer-col h5 { font-weight: bold; margin-bottom: 20px; }
        .footer-col p, .footer-col li { font-size: 14px !important; list-style: none; padding: 0; }
    </style>
""", unsafe_allow_html=True)

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR CHUẨN (GỌN VÀ ĐẸP) ---
st.markdown('<div style="background: white; border-bottom: 1px solid #eee; padding: 10px 0;">', unsafe_allow_html=True)
nav_col_logo, nav_col_menu = st.columns([1, 4])

with nav_col_logo:
    st.image("https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png", width=150)

with nav_col_menu:
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("HOME", use_container_width=True): 
            st.session_state['page'] = 'TRANG CHỦ'
            st.rerun()
    with m2:
        if st.button("ABOUT", use_container_width=True): 
            st.session_state['page'] = 'GIỚI THIỆU'
            st.rerun()
    with m3:
        if st.button("NEWS", use_container_width=True): 
            st.session_state['page'] = 'TIN TỨC'
            st.rerun()
    with m4:
        if st.button("AI SHIELD", use_container_width=True): 
            st.session_state['page'] = 'VỆ SĨ AI'
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. ĐIỀU HƯỚNG NỘI DUNG ---
main_body = st.container()

with main_body:
    if st.session_state['page'] == 'TRANG CHỦ':
        # --- NEW BANNER: CƠ CHẾ Y CHANG MẪU FOCUSON ---
        st.markdown(f"""
            <div class="hero-container">
                <div class="hero-text">
                    <h4>SILVERSHIELD PROTECT</h4>
                    <h1>POWERFUL & SMART <br><span style="color:#8bc34a">AI GUARDIAN</span> FOR ELDERS</h1>
                    <p style="color:#666; margin: 20px 0;">Hệ thống trí tuệ nhân tạo hàng đầu giúp nhận diện lừa đảo, bảo vệ người cao tuổi an tâm sử dụng mạng internet mỗi ngày.</p>
                </div>
                <div class="hero-image">
                    <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png">
                </div>
            </div>
        """, unsafe_allow_html=True)

        # PHẦN QUY TẮC AN TOÀN (GIỮ NGUYÊN NHƯNG TINH CHỈNH CSS)
        st.markdown('<div class="rules-main-header" style="text-align:center; padding: 30px 0;">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
        r1, r2, r3 = st.columns(3, gap="medium")
        with r1:
            st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div style="padding:15px; font-weight:bold;">1. Không chuyển tiền<br>2. Không bấm link lạ<br>3. Không đưa OTP<br>4. Không cài app lạ<br>5. Không sợ đe dọa</div></div>', unsafe_allow_html=True)
        with r2:
            st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div style="padding:15px; font-weight:bold;">1. Nên gọi xác thực<br>2. Nên hỏi con cháu<br>3. Nên báo công an</div></div>', unsafe_allow_html=True)
        with r3:
            st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý</div><div style="padding:15px; font-weight:bold;">1. Luôn bình tĩnh<br>2. Đọc tin an ninh<br>3. Dùng SilverShield</div></div>', unsafe_allow_html=True)

        # TIN TỨC (FIX LỖI LINK_BUTTON)
        st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:15px; margin-top:30px; font-weight:bold; border-radius:5px;">📰 TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
        news_data = [
            {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
            {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/canh-bao-thu-doan-lua-dao-bang-cong-nghe-deepfake-2023032711054321.htm"},
            {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/bay-viec-nhe-luong-cao-tren-mang-4478144.html"}
        ]
        cols = st.columns(3)
        for idx, item in enumerate(news_data):
            with cols[idx]:
                st.markdown(f'<div class="news-card" style="background:white; border:1px solid #eee; border-radius:8px; overflow:hidden;"><img src="{item["img"]}" style="width:100%; height:180px; object-fit:cover;"><div style="padding:10px; font-weight:bold; height:60px;">{item["title"]}</div></div>', unsafe_allow_html=True)
                # FIX: Bỏ tham số 'key' vì link_button không hỗ trợ key trong phiên bản của bạn
                st.link_button("CHI TIẾT", item['url'], use_container_width=True)

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
                # FIX: Bỏ tham số key
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

# --- 4. NEW FOOTER: MÀU CAM HOÀN CHỈNH ---
st.markdown("""
    <div class="custom-footer">
        <div class="footer-grid">
            <div class="footer-col">
                <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" width="120" style="filter: brightness(0) invert(1);">
                <p style="margin-top:20px;">SilverShield - Lá chắn thép bảo vệ người cao tuổi trên không gian mạng.</p>
            </div>
            <div class="footer-col">
                <h5>CHĂM SÓC KHÁCH HÀNG</h5>
                <li>Hướng dẫn sử dụng</li>
                <li>Câu hỏi thường gặp</li>
                <li>Liên hệ hỗ trợ</li>
            </div>
            <div class="footer-col">
                <h5>VỀ SILVERSHIELD</h5>
                <li>Điều khoản dịch vụ</li>
                <li>Chính sách bảo mật</li>
                <li>Đội ngũ phát triển</li>
            </div>
            <div class="footer-col">
                <h5>LIÊN HỆ</h5>
                <p>📍 THPT Dương Văn Thì</p>
                <p>📧 support@silvershield.vn</p>
                <p>📞 1900 xxxx</p>
            </div>
        </div>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 30px 0;">
        <p style="text-align:center; font-size: 12px !important;">© 2026 Bản quyền thuộc về Đội ngũ DVT - Empire CBZ X</p>
    </div>
""", unsafe_allow_html=True)
