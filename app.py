import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
styles.apply_styles()
styles.render_top_bar() # Thanh xanh lá trên cùng

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR (MENU TRẮNG - LOGO XANH) ---
st.markdown('<div class="focuson-navbar"><div style="width:1200px; margin:0 auto; padding:0 15px; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, c_menu = st.columns([2, 8])

with c_logo:
    # Logo chữ màu xanh lá giống mẫu Focuson
    st.markdown('<h2 style="color:#82b440; margin:0; font-family:Raleway; font-weight:800;">SILVERSHIELD</h2>', unsafe_allow_html=True)

with c_menu:
    m1, m2, m3, m4, m5 = st.columns([1.5, 1.5, 1.5, 2, 2.5])
    with m1:
        if st.button("TRANG CHỦ"): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("GIỚI THIỆU"): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("TIN TỨC"): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("VỆ SĨ AI"): st.session_state['page'] = 'VỆ SĨ AI'
    with m5:
        # Nút xanh lá nổi bật
        st.markdown('<div class="btn-quote">', unsafe_allow_html=True)
        if st.button("KIỂM TRA NGAY", use_container_width=True):
            st.session_state['page'] = 'VỆ SĨ AI'
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)


# --- 3. NỘI DUNG CHÍNH ---

if st.session_state['page'] == 'TRANG CHỦ':
    # === HERO SECTION (GIỐNG MẪU FOCUSON) ===
    # Text nằm bên trái, Nền trắng đè lên ảnh
    st.markdown("""
    <div class="focuson-hero">
        <div class="hero-overlay-gradient"></div>
        <div class="hero-text-box">
            <div class="green-script">We Are SilverShield AI</div>
            <div class="big-title">POWERFUL & CLEAN<br>AI GUARDIAN</div>
            <p class="hero-desc">
                Hệ thống trí tuệ nhân tạo hàng đầu giúp nhận diện lừa đảo, bảo vệ người cao tuổi an tâm sử dụng mạng internet mỗi ngày.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Nút bấm trong Banner (Dùng columns để canh vị trí cho nút Streamlit)
    # Hack vị trí để nút nằm đè lên banner
    st.markdown('<div style="max-width:1200px; margin:-200px auto 0 auto; padding-left:20px; position:relative; z-index:5;">', unsafe_allow_html=True)
    col_cta, col_empty = st.columns([2, 8])
    with col_cta:
        st.markdown('<div class="btn-quote">', unsafe_allow_html=True)
        if st.button("BẮT ĐẦU NGAY"):
            st.session_state['page'] = 'VỆ SĨ AI'
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div><div style="height:150px;"></div>', unsafe_allow_html=True)


    # === CÁC KHỐI THÔNG TIN (VUÔNG VỨC) ===
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    
    # Tiêu đề section
    st.markdown('<h3 style="text-align:center; color:#333; font-weight:800; text-transform:uppercase;">VỀ CHÚNG TÔI</h3><div style="width:50px; height:3px; background:#82b440; margin:15px auto 40px auto;"></div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.markdown("""
        <div class="info-box">
            <h4 style="color:#333; font-weight:700;">THÔNG MINH</h4>
            <p style="color:#777; font-size:14px;">Phân tích tin nhắn lừa đảo chính xác bằng AI Google Gemini.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="info-box">
            <h4 style="color:#333; font-weight:700;">ĐƠN GIẢN</h4>
            <p style="color:#777; font-size:14px;">Giao diện tối giản, dễ sử dụng cho người lớn tuổi.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="info-box">
            <h4 style="color:#333; font-weight:700;">TỐC ĐỘ</h4>
            <p style="color:#777; font-size:14px;">Trả kết quả cảnh báo và giọng nói ngay lập tức.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)


# --- TRANG VỆ SĨ AI (GIỮ NGUYÊN LOGIC - CHỈNH LẠI BOX) ---
elif st.session_state['page'] == 'VỆ SĨ AI':
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#333; font-weight:800;">TRUNG TÂM PHÂN TÍCH</h3><div style="width:50px; height:3px; background:#82b440; margin:10px 0 30px 0;"></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown('<div style="background:#f9f9f9; padding:20px; border:1px solid #eee;">', unsafe_allow_html=True)
        st.markdown("#### 1. NHẬP THÔNG TIN")
        txt = st.text_area("Nội dung tin nhắn:", height=150)
        img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg'])
        
        st.markdown('<div class="btn-quote" style="margin-top:10px;">', unsafe_allow_html=True)
        if st.button("PHÂN TÍCH", use_container_width=True):
            if txt or img:
                with st.spinner("AI đang xử lý..."):
                    i = Image.open(img) if img else None
                    st.session_state['res'] = logic.analyze_content(model, txt, i)
        st.markdown('</div></div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div style="background:#fff; padding:20px; border:1px solid #eee; height:100%;">', unsafe_allow_html=True)
        st.markdown("#### 2. KẾT QUẢ")
        if 'res' in st.session_state:
            st.success("ĐÃ CÓ KẾT QUẢ")
            st.write(st.session_state['res'])
            st.audio(logic.text_to_speech(st.session_state['res']))
        else:
            st.info("Kết quả sẽ hiện ở đây.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with c_intro:
            st.markdown('<div class="banner-strip"><div class="banner-header">VỀ ỨNG DỤNG</div><p style="text-align:justify; color:#333; padding:15px;">SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến cho người cao tuổi.</p></div>', unsafe_allow_html=True)
        with c_guide:
            st.markdown('<div class="banner-strip"><div class="banner-header">HƯỚNG DẪN</div><ul style="text-align:left; color:#333; padding:15px;"><li>Bước 1: Chọn "Vệ sĩ AI"</li><li>Bước 2: Nhập nội dung nghi ngờ</li><li>Bước 3: Xem kết quả cảnh báo</li></ul></div>', unsafe_allow_html=True)

        st.markdown('<div class="rules-main-header">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
        r1, r2, r3 = st.columns(3, gap="medium")
        with r1:
            st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div style="padding:15px; font-weight:bold;">1. Không chuyển tiền<br>2. Không bấm link lạ<br>3. Không đưa OTP<br>4. Không cài app lạ<br>5. Không sợ đe dọa</div></div>', unsafe_allow_html=True)
        with r2:
            st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div style="padding:15px; font-weight:bold;">1. Nên gọi xác thực<br>2. Nên hỏi con cháu<br>3. Nên báo công an</div></div>', unsafe_allow_html=True)
        with r3:
            st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý</div><div style="padding:15px; font-weight:bold;">1. Luôn bình tĩnh<br>2. Đọc tin an ninh<br>3. Dùng SilverShield</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:15px; margin-top:30px; font-weight:bold;">📰 TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
        news_data = [
            {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
            {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/canh-bao-thu-doan-lua-dao-bang-cong-nghe-deepfake-2023032711054321.htm"},
            {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/bay-viec-nhe-luong-cao-tren-mang-4478144.html"}
        ]
        cols = st.columns(3)
        for idx, item in enumerate(news_data):
            with cols[idx]:
                st.markdown(f'<div class="news-card" style="background:white; border:1px solid #eee;"><img src="{item["img"]}" style="width:100%; height:180px; object-fit:cover;"><div style="padding:10px; font-weight:bold;">{item["title"]}</div></div>', unsafe_allow_html=True)
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


# --- FOOTER ---
st.markdown("""
    <div class="footer">
        <h3 style="color:white; margin:0;">SILVERSHIELD</h3>
        <p>Thành viên của DVT - Empire CBZ X</p>
        <div style="margin-top:20px; font-size:12px;">© 2026 All Rights Reserved.</div>
    </div>
""", unsafe_allow_html=True)
