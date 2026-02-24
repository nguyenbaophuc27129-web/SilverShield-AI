import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO (GIỮ NGUYÊN) ---
styles.apply_styles()
styles.render_header_structure() 

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR (GIỮ NGUYÊN) ---
st.markdown('<div class="olympic-navbar"><div class="navbar-container" style="width:1200px; margin:0 auto; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, m1, m2, m3, m4 = st.columns([1.5, 2, 2, 2, 2])

with c_logo:
    st.markdown('<img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:50px; margin-left:15px;">', unsafe_allow_html=True)

with m1:
    if st.button("🏠 TRANG CHỦ", use_container_width=True): 
        st.session_state['page'] = 'TRANG CHỦ'; st.rerun()
with m2:
    if st.button("👥 GIỚI THIỆU", use_container_width=True): 
        st.session_state['page'] = 'GIỚI THIỆU'; st.rerun()
with m3:
    if st.button("📰 TIN TỨC", use_container_width=True): 
        st.session_state['page'] = 'TIN TỨC'; st.rerun()
with m4:
    if st.button("🛡️ VỆ SĨ AI", use_container_width=True): 
        st.session_state['page'] = 'VỆ SĨ AI'; st.rerun()

st.markdown('</div></div>', unsafe_allow_html=True)

# --- 3. ĐIỀU HƯỚNG NỘI DUNG ---

if st.session_state['page'] == 'TRANG CHỦ':
    # --- GIỮ NGUYÊN BANNER ---
    banner_html = """
    <div class="hero-container" style="position: relative; overflow: hidden;">
            <div class="hero-bg-overlay"></div>
            <div style="display: flex; align-items: center; justify-content: center; gap: 50px; width: 1200px; margin: 0 auto; height: 100%; position: relative; z-index: 10;">
        <div style="display: flex; width: 1100px; height: 350px; box-shadow: 0 20px 50px rgba(0,0,0,0.5);">
            <div style="flex: 3; height: 100%;">
                <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png" 
                     style="width: 100%; height: 100%; object-fit: cover; border-radius: 0;">
            </div>
            <div style="flex: 1; background: rgba(255,255,255,0.1); backdrop-filter: blur(15px); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border-radius: 0; padding: 20px;">
                <h2 style="font-family: 'Roboto', sans-serif; color:#FFB300; margin:0; font-size: 40px; font-weight: 900; text-transform: uppercase;">VỆ SĨ SILVER</h2>
                <div style="height: 4px; background: #d32f2f; width: 80px; margin: 15px auto;"></div>
                <p style="font-size:18px; color: white; font-weight: 700; text-transform: uppercase;">Hệ thống AI bảo vệ người già</p>
                <div style="height: 50px;"></div>
            </div>
        </div>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    c_intro, c_guide = st.columns(2, gap="large")
    with c_intro:
        st.markdown('<div class="banner-strip"><div class="banner-header">VỀ ỨNG DỤNG</div><p style="text-align:justify; color:#555; font-size:14px; padding:15px;">SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến cho người cao tuổi.</p></div>', unsafe_allow_html=True)
    with c_guide:
        st.markdown('<div class="banner-strip"><div class="banner-header">HƯỚNG DẪN</div><ul style="text-align:left; color:#555; font-size:14px; padding:15px;"><li>Bước 1: Chọn "Vệ sĩ AI"</li><li>Bước 2: Nhập nội dung nghi ngờ</li><li>Bước 3: Xem kết quả cảnh báo</li></ul></div>', unsafe_allow_html=True)

    st.markdown('<div class="rules-main-header">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3, gap="medium")
    with r1:
        st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div style="padding:15px; font-size:13px;">1. Không chuyển tiền<br>2. Không bấm link lạ<br>3. Không đưa OTP<br>4. Không cài app lạ<br>5. Không sợ đe dọa</div></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div style="padding:15px; font-size:13px;">1. Nên gọi xác thực<br>2. Nên hỏi con cháu<br>3. Nên báo công an</div></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý</div><div style="padding:15px; font-size:13px;">1. Luôn bình tĩnh<br>2. Đọc tin an ninh<br>3. Dùng SilverShield</div></div>', unsafe_allow_html=True)

    # Tin tức ở trang chủ (Đã bỏ tham số key để tránh lỗi)
    st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:10px; margin-top:30px; font-weight:bold;">📰 TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
    news_data = [
        {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn"},
        {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn"},
        {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net"}
    ]
    cols = st.columns(3)
    for idx, item in enumerate(news_data):
        with cols[idx]:
            st.markdown(f'<div class="news-card" style="background:white; border:1px solid #eee;"><img src="{item["img"]}" style="width:100%; height:150px; object-fit:cover;"><div style="padding:10px; font-weight:bold; font-size:13px;">{item["title"]}</div></div>', unsafe_allow_html=True)
            # FIX: Bỏ tham số key tại đây
            st.link_button("CHI TIẾT", item['url'], use_container_width=True)

elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN & SỨ MỆNH</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown('<div class="banner-strip"><div class="banner-header">SỨ MỆNH</div><p style="padding:20px; text-align:justify; color:#555;">SilverShield ra đời để bảo vệ người cao tuổi Việt Nam trước vấn nạn lừa đảo mạng ngày càng tinh vi. Chúng tôi cam kết sử dụng AI để tạo ra "lá chắn thép" cho mọi gia đình.</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="banner-strip"><div class="banner-header">ĐỘI NGŨ DVT</div><p style="padding:20px; text-align:justify; color:#555;">Đội ngũ Empire CBZ X hội tụ các cá nhân đam mê công nghệ tại THPT Dương Văn Thì, hướng tới những giải pháp vì cộng đồng.</p></div>', unsafe_allow_html=True)

elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="rules-main-header">📰 BẢN TIN AN NINH TOÀN CẢNH</div>', unsafe_allow_html=True)
    
    full_news = [
        {"title": "Lừa đảo qua video call Deepfake", "desc": "Đối tượng dùng AI giả khuôn mặt người thân để vay tiền gấp.", "tag": "CẢNH BÁO", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://vnexpress.net/thu-doan-lua-dao-video-call-deepfake-4586231.html"},
        {"title": "Tin nhắn giả danh ngân hàng", "desc": "Yêu cầu cập nhật thông tin qua link lạ để chiếm đoạt mã OTP.", "tag": "NGUY HIỂM", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn/cong-nghe/canh-bao-hinh-thuc-lua-dao-moi-qua-ma-qr-20230814154506307.htm"},
        {"title": "Cẩm nang phòng chống tội phạm", "desc": "Sổ tay hướng dẫn của Bộ Công An dành cho người dân.", "tag": "KIẾN THỨC", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://chinhphu.vn/canh-bao-24-hinh-thuc-lua-dao-tren-khong-gian-mang-103230713145455645.htm"}
    ]

    for idx, n in enumerate(full_news):
        col_img, col_txt = st.columns([1, 2.5])
        with col_img:
            st.image(n['img'], use_container_width=True)
        with col_txt:
            st.markdown(f"""
                <div style="background:white; padding:15px; border-left:5px solid #d32f2f; margin-bottom:10px;">
                    <span style="background:#d32f2f; color:white; padding:2px 8px; font-size:10px; font-weight:bold;">{n['tag']}</span>
                    <h3 style="margin:10px 0;">{n['title']}</h3>
                    <p style="color:#666;">{n['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            # SỬA LỖI TRIỆT ĐỂ: Bỏ hoàn toàn tham số 'key' trong link_button
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

styles.render_footer_structure()
