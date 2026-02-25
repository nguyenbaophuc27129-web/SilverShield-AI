import streamlit as st
from PIL import Image
import styles
import logic
import time  # Thêm thư viện để xử lý thời gian chờ

# --- 1. KHỞI TẠO & ÉP FOOTER SÁT ĐÁY TUYỆT ĐỐI ---
styles.apply_styles()
styles.render_header_structure() 

# Đoạn CSS này được bổ sung thêm các quy tắc về FONT CHỮ TO RÕ
st.markdown("""
    <style>
        /* --- PHẦN THÊM MỚI: TỐI ƯU FONT CHO NGƯỜI LỚN TUỔI --- */
        html, body, [class*="st-"] {
            font-family: 'Segoe UI', Arial, sans-serif !important;
            font-size: 18px !important; /* Tăng size nền toàn trang */
        }
        
        /* Làm cho các đoạn văn bản mô tả to và dễ đọc hơn */
        p, li {
            font-size: 20px !important; 
            line-height: 1.6 !important;
            color: black !important; /* Độ tương phản cao */
            font-weight: 450 !important;
        }

        /* Tăng kích thước nút bấm để dễ nhấn */
        .stButton>button {
            font-size: 20px !important;
            font-weight: bold !important;
            padding: 10px !important;
        }

        /* Tiêu đề các mục phải cực kỳ nổi bật */
        .banner-header, .rules-main-header, .news-header-bar {
            font-size: 28px !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
        }

        /* Thẻ quy tắc (Rule Cards) chữ to hơn */
        .rule-header {
            font-size: 24px !important;
            font-weight: bold !important;
        }

        /* ======================================================= */
        /* CHỖ ĐỂ BẠN CHỈNH MÀU CHỮ FOOTER                         */
        /* ======================================================= */
        .footer-container, .footer-container p, .footer-container div, .footer-container span {
            color: #FFFF00 !important; /* Đã sửa lỗi chữ 'w' dư thừa cho bạn */
            opacity: 1 !important;
        }
        /* ======================================================= */

        /* --- GIỮ NGUYÊN CÁC CSS CŨ CỦA BẠN --- */
        .loading-overlay {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 99999;
            flex-direction: column;
        }
        .loading-text {
            font-size: 80px;
            font-weight: bold;
            color: #FF6600;
            font-family: Arial, sans-serif;
            letter-spacing: -2px;
            overflow: hidden; 
            white-space: nowrap;
            margin: 0 auto;
            border-right: .15em solid #FF6600;
            animation: typing 0.8s steps(12, end), blink-caret .75s step-end infinite;
        }

        @keyframes typing { from { width: 0 } to { width: 600px } }
        @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #FF6600; } }

        .main .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; max-width: 100% !important; }
        footer {visibility: hidden !important; height: 0;}
        header {visibility: hidden !important;}

        .stApp { display: flex; flex-direction: column; }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section { display: flex; flex-direction: column; }
        .stVerticalBlock { flex-grow: 1; }
        div[data-testid="stVerticalBlock"] > div:last-child { margin-bottom: 0px !important; padding-bottom: 0px !important; }
    </style>
""", unsafe_allow_html=True)

# HÀM XỬ LÝ HIỆU ỨNG CHỜ KHI CHUYỂN TRANG
def trigger_loading(target_page):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""
            <div class="loading-overlay">
                <div class="loading-text">SILVERSHIELD</div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.2)
    st.session_state['page'] = target_page
    placeholder.empty()
    st.rerun()

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR CHUẨN (GIỮ NGUYÊN NỘI DUNG) ---
st.markdown('<div class="olympic-navbar"><div class="navbar-container" style="width:1200px; margin:0 auto; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, m1, m2, m3, m4 = st.columns([1.5, 2, 2, 2, 2])

with c_logo:
    st.markdown('<img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:50px; margin-left:15px;">', unsafe_allow_html=True)

with m1:
    if st.button("TRANG CHỦ", use_container_width=True): trigger_loading('TRANG CHỦ')
with m2:
    if st.button("GIỚI THIỆU", use_container_width=True): trigger_loading('GIỚI THIỆU')
with m3:
    if st.button("TIN TỨC", use_container_width=True): trigger_loading('TIN TỨC')
with m4:
    if st.button("VỆ SĨ SILVER", use_container_width=True): trigger_loading('VỆ SĨ SILVER')

st.markdown('</div></div>', unsafe_allow_html=True)

# --- 3. ĐIỀU HƯỚNG NỘI DUNG ---
main_body = st.container()

with main_body:
    if st.session_state['page'] == 'TRANG CHỦ':
        # --- THÊM CSS ĐỂ ĐỒNG BỘ HÌNH KHỐI (KHÔNG CHẠM VÀO LOGIC) ---
        st.markdown("""
            <style>
                .home-info-card {
                    background: white; border-radius: 20px; padding: 25px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease; height: 100%;
                    border-top: 6px solid #0044cc;
                }
                .home-info-card:hover { transform: translateY(-5px); }
                .rule-card-modern {
                    background: white; border-radius: 20px; overflow: hidden;
                    box-shadow: 0 10px 20px rgba(0,0,0,0.08); height: 100%;
                }
                .rule-header-modern {
                    padding: 15px; color: white; font-weight: bold;
                    font-size: 22px; text-align: center; text-transform: uppercase;
                }
            </style>
        """, unsafe_allow_html=True)

        banner_html = """
        <div class="hero-container" style="position: relative; overflow: hidden; border-radius: 20px;">
                <div class="hero-bg-overlay"></div>
                <div style="display: flex; align-items: center; justify-content: center; gap: 50px; width: 1200px; margin: 0 auto; height: 100%; position: relative; z-index: 10;">
            <div style="display: flex; width: 1100px; height: 350px; box-shadow: 0 20px 50px rgba(0,0,0,0.5);">
                <div style="flex: 3; height: 100%;">
                    <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png" 
                         style="width: 100%; height: 100%; object-fit: cover; border-radius: 0;">
                </div>
        """
        st.markdown(banner_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        c_intro, c_guide = st.columns(2, gap="large")
        with c_intro:
            st.markdown("""
                <div class="home-info-card">
                    <div class="banner-header" style="color:#0044cc; border-bottom: 2px solid #eee; padding-bottom:10px;">🛡️ VỀ ỨNG DỤNG</div>
                    <p style="text-align:justify; margin-top:15px;">SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến cho người cao tuổi.</p>
                </div>
            """, unsafe_allow_html=True)
        with c_guide:
            st.markdown("""
                <div class="home-info-card" style="border-top-color: #FF6600;">
                    <div class="banner-header" style="color:#FF6600; border-bottom: 2px solid #eee; padding-bottom:10px;">📖 HƯỚNG DẪN</div>
                    <ul style="text-align:left; margin-top:15px;">
                        <li><b>Bước 1:</b> Chọn MỤC "VỆ SĨ SILVER" để được hỗ trợ nhanh nhất</li>
                        <li><b>Bước 2:</b> Nhập nội dung nghi ngờ vào khung tin nhắn hoặc nhấn gửi hình ảnh</li>
                        <li><b>Bước 3:</b> Hết sức bình tĩnh và làm theo chỉ dẫn </li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

        # --- KHỐI QUY TẮC AN TOÀN (ĐÃ ĐỒNG BỘ CẤU HÌNH Y CHANG 2 Ô TRÊN) ---
        # --- PHẦN 3 Ô QUY TẮC AN TOÀN HOÀN CHỈNH ---
        st.markdown('<div class="rules-main-header">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
        
        r1, r2, r3 = st.columns(3, gap="medium")
        
        with r1:
            st.markdown("""
                <div class="home-info-card" style="border-top-color: #d32f2f; border-radius: 0px !important;">
                    <div class="banner-header" style="color:#d32f2f; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 15px;">
                        🚫 5 "KHÔNG"
                    </div>
                    <div style="font-size:18px; line-height:1.8; color: #222;">
                        1. <b>Không</b> chia sẻ dữ liệu cá nhân<br>
                        2. <b>Không</b> tiết lộ mã OTP cá nhân<br>
                        3. <b>Không</b> bấm vào đường link, quảng cáo lạ<br>
                        4. <b>Không</b> mở tệp tin lạ gửi qua email và tin nhắn<br>
                        5. <b>Không</b> làm theo yêu cầu chuyển tiền của người lạ
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        with r2:
            st.markdown("""
                <div class="home-info-card" style="border-top-color: #2e7d32; border-radius: 0px !important;">
                    <div class="banner-header" style="color:#2e7d32; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 15px;">
                        ✅ 5 "LUÔN"
                    </div>
                    <div style="font-size:18px; line-height:1.8; color: #222;">
                        1. <b>Luôn</b> ý thức bảo mật thông tin cá nhân<br>
                        2. <b>Luôn</b> đặt mật khẩu mạnh và thay đổi thường xuyên<br>
                        3. <b>Luôn</b> dùng phần mềm uy tín có nguồn gốc rõ ràng<br>
                        4. <b>Luôn</b> cập nhật kiến thức an toàn mạng qua các kênh chính thống<br>
                        5. <b>Luôn</b> cảnh giác khi có yêu cầu chuyển tiền lạ
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        with r3:
            st.markdown("""
                <div class="home-info-card" style="border-top-color: #008080; border-radius: 0px !important;">
                    <div class="banner-header" style="color:#008080; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 15px;">
                        💡 LƯU Ý
                    </div>
                    <div style="font-size:18px; line-height:1.8; color: #222;">
                        1. <b>Luôn luôn</b> giữ bình tĩnh tuyệt đối, không hoảng loạn<br>
                        2. <b>Thường xuyên</b> đọc tin tức an ninh<br>
                        3. <b>Kiểm tra</b> kỹ danh tính người yêu cầu hành động<br>
                        4. <b>Chia sẻ</b> kiến thức an toàn mạng cho mọi người<br>
                        5. <b>Lặp tức</b> tắt máy đối với các đối tượng giả danh chính quyền hành động ONLINE
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:10px; margin-top:30px; font-weight:bold; border-radius:10px;">📰 TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
        news_data = [
            {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
            {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/canh-bao-thu-doan-lua-dao-bang-cong-nghe-deepfake-2023032711054321.htm"},
            {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/bay-viec-nhe-luong-cao-tren-mang-4478144.html"}
        ]
        cols = st.columns(3)
        for idx, item in enumerate(news_data):
            with cols[idx]:
                st.markdown(f'<div class="news-card" style="background:white; border:1px solid #eee; border-radius:15px; overflow:hidden;"><img src="{item["img"]}" style="width:100%; height:150px; object-fit:cover;"><div style="padding:10px; font-weight:bold;">{item["title"]}</div></div>', unsafe_allow_html=True)
                st.link_button("CHI TIẾT", item['url'], use_container_width=True)

    elif st.session_state['page'] == 'GIỚI THIỆU':
        st.markdown("""
            <style>
                .team-card {
                    background: white; border-radius: 20px; padding: 25px;
                    text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease; height: 100%; border-bottom: 5px solid #FF6600;
                }
                .team-card:hover { transform: translateY(-10px); }
                .team-img { width: 140px; height: 140px; border-radius: 50%; object-fit: cover; margin-bottom: 15px; border: 4px solid #f0f2f6; }
                .team-name { color: #0044cc; font-weight: bold; font-size: 22px; margin-bottom: 5px; }
                .team-role { color: #FF6600; font-weight: 600; font-size: 16px; margin-bottom: 15px; text-transform: uppercase; }
                .info-box { background: #ffffff; border-top: 5px solid #0044cc; padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); height: 100%; }
                .info-title { color: #0044cc; font-size: 26px; font-weight: 800; margin-bottom: 15px; }
                .info-text { color: #333; line-height: 1.8; text-align: justify; font-size: 18px; }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="rules-main-header">🌟 GƯƠNG MẶT PHÁT TRIỂN SILVERSHIELD</div>', unsafe_allow_html=True)
        col_t1, col_t2, col_t3 = st.columns(3, gap="large")
        with col_t1:
            st.markdown('<div class="team-card"><img src="https://via.placeholder.com/150" class="team-img"><div class="team-name">Nguyễn Bảo Phúc</div><div class="team-role">Trưởng nhóm & Kỹ thuật AI</div><p style="font-size:16px; color:#444;">Phụ trách kiến trúc hệ thống và huấn luyện mô hình ngôn ngữ cho Vệ sĩ Silver.</p></div>', unsafe_allow_html=True)
        with col_t2:
            st.markdown('<div class="team-card"><img src="https://via.placeholder.com/150" class="team-img"><div class="team-name">Empire CBZ X</div><div class="team-role">Phát triển Nội dung</div><p style="font-size:16px; color:#444;">Xây dựng cơ sở dữ liệu các kịch bản lừa đảo và tối ưu trải nghiệm người dùng.</p></div>', unsafe_allow_html=True)
        with col_t3:
            st.markdown('<div class="team-card"><img src="https://via.placeholder.com/150" class="team-img"><div class="team-name">DVT Team</div><div class="team-role">Thiết kế & Truyền thông</div><p style="font-size:16px; color:#444;">Đảm bảo giao diện trực quan, dễ tiếp cận nhất cho người cao tuổi Việt Nam.</p></div>', unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        col_left, col_right = st.columns(2, gap="large")
        with col_left:
            st.markdown('<div class="info-box"><div class="info-title">📜 CÂU CHUYỆN CỦA CHÚNG TÔI</div><div class="info-text">Xuất phát từ thực trạng nhức nhối khi người cao tuổi thường xuyên bị kẻ xấu lợi dụng trên không gian mạng, chúng tôi - những học sinh từ trường <b>THPT Dương Văn Thì</b> - đã quyết tâm tạo ra một giải pháp bảo vệ. SilverShield ra đời như một người bạn đồng hành.</div></div>', unsafe_allow_html=True)
        with col_right:
            st.markdown('<div class="info-box" style="border-top-color: #FF6600;"><div class="info-title" style="color: #FF6600;">🚀 SỨ MỆNH SILVERSHIELD</div><div class="info-text">Sứ mệnh của SilverShield là phổ cập AI để làm "lá chắn thép" cho người dân, giảm thiểu thiệt hại do lừa đảo trực tuyến và xây dựng một cộng đồng số an toàn, văn minh cho mọi lứa tuổi.</div></div>', unsafe_allow_html=True)

    elif st.session_state['page'] == 'TIN TỨC':
        st.markdown('<div class="rules-main-header">📰 BẢN TIN AN NINH TOÀN CẢNH</div>', unsafe_allow_html=True)
        full_news = [
            {"title": "Lừa đảo qua video call Deepfake", "desc": "Đối tượng dùng AI giả khuôn mặt người thân để vay tiền gấp.", "tag": "CẢNH BÁO", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://vnexpress.net/thu-doan-lua-dao-video-call-deepfake-4586231.html"},
            {"title": "Tin nhắn giả danh ngân hàng", "desc": "Yêu cầu cập nhật thông tin qua link lạ để chiếm đoạt mã OTP.", "tag": "NGUY HIỂM", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
            {"title": "Cẩm nang phòng chống tội phạm", "desc": "Sổ tay hướng dẫn của Bộ Công An dành cho người dân và người cao tuổi.", "tag": "KIẾN THỨC", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://chinhphu.vn/canh-bao-24-hinh-thuc-lua-dao-tren-khong-gian-mang-103230713145455645.htm"}
        ]
        for idx, n in enumerate(full_news):
            c_img, c_txt = st.columns([1, 2.5])
            with c_img: st.image(n["img"], use_container_width=True)
            with c_txt:
                st.markdown(f'<div style="background:white; padding:15px; border-left:8px solid #d32f2f; margin-bottom:5px;"><span style="background:#d32f2f; color:white; padding:4px 12px; font-size:14px; font-weight:bold;">{n["tag"]}</span><h3 style="margin:15px 0;">{n["title"]}</h3><p style="color:#222;">{n["desc"]}</p></div>', unsafe_allow_html=True)
                st.link_button("XEM BÁO CHÍNH THỐNG", n['url'])
            st.markdown("<hr>", unsafe_allow_html=True)

    elif st.session_state['page'] == 'VỆ SĨ SILVER':
        st.markdown('<div class="rules-main-header">🛡️ TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1], gap="large")
        with c1:
            txt = st.text_area("Nhập nội dung cần kiểm tra:", height=250)
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

# --- 4. FOOTER (SÁT ĐÁY TUYỆT ĐỐI) ---
styles.render_footer_structure()






