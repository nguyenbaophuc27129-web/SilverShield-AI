import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO ---
styles.apply_styles()
styles.render_header_structure() 

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR CHUẨN (FIX LỆNH CHUYỂN TRANG) ---
st.markdown('<div class="olympic-navbar"><div class="navbar-container" style="width:1200px; margin:0 auto; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, m1, m2, m3, m4 = st.columns([1.5, 2, 2, 2, 2])

with c_logo:
    st.markdown('<img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:50px; margin-left:15px;">', unsafe_allow_html=True)

with m1:
    if st.button("🏠 TRANG CHỦ", use_container_width=True): 
        st.session_state['page'] = 'TRANG CHỦ'; st.rerun()

with m2:
    # Đã sửa: Thêm lệnh chuyển trang cho GIỚI THIỆU
    if st.button("👥 GIỚI THIỆU", use_container_width=True): 
        st.session_state['page'] = 'GIỚI THIỆU'; st.rerun()

with m3:
    # Đã sửa: Thêm lệnh chuyển trang cho TIN TỨC
    if st.button("📰 TIN TỨC", use_container_width=True): 
        st.session_state['page'] = 'TIN TỨC'; st.rerun()

with m4:
    if st.button("🛡️ VỆ SĨ AI", use_container_width=True): 
        st.session_state['page'] = 'VỆ SĨ AI'; st.rerun()
st.markdown('</div></div>', unsafe_allow_html=True)


# --- 3. ĐIỀU HƯỚNG NỘI DUNG ---

# --- TRANG CHỦ ---
if st.session_state['page'] == 'TRANG CHỦ':
    banner_html = """
    <div class="hero-container" style="position: relative; overflow: hidden; background: #001529; padding: 20px 0;">
        <div style="display: flex; width: 1100px; height: 350px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); margin: 0 auto;">
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
    
    # Nút KIỂM TRA NGAY đè lên banner
    st.markdown('<div style="margin-top: -105px; position: relative; z-index: 1000; display: flex; justify-content: center; width: 100%; padding-left: 450px;">', unsafe_allow_html=True)
    if st.button("KIỂM TRA NGAY", key="hero_btn"):
        st.session_state['page'] = 'VỆ SĨ AI'; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c_intro, c_guide = st.columns(2, gap="large")
    with c_intro:
        st.markdown('<div class="banner-strip"><div class="banner-header">VỀ ỨNG DỤNG</div><p style="text-align:justify; color:#555; font-size:14px; padding:15px;">SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến cho người cao tuổi.</p></div>', unsafe_allow_html=True)
    with c_guide:
        st.markdown('<div class="banner-strip"><div class="banner-header">HƯỚNG DẪN</div><ul style="text-align:left; color:#555; font-size:14px; padding:15px;"><li>Bước 1: Chọn "Vệ sĩ AI"</li><li>Bước 2: Nhập nội dung nghi ngờ</li><li>Bước 3: Xem kết quả cảnh báo</li></ul></div>', unsafe_allow_html=True)

# --- TRANG GIỚI THIỆU (ĐÃ THÊM NỘI DUNG) ---
elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="rules-main-header">GIỚI THIỆU HỆ THỐNG SILVERSHIELD AI</div>', unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 1], gap="medium")
    with col_l:
        st.markdown("""
            <div class="rule-card">
                <div class="rule-header bg-teal">SỨ MỆNH</div>
                <div style="padding:20px; text-align:justify;">
                    SilverShield ra đời với sứ mệnh bảo vệ thế hệ người cao tuổi Việt Nam trước làn sóng tội phạm công nghệ cao đang ngày càng tinh vi. Chúng tôi xây dựng một lá chắn số an toàn, dễ sử dụng và tin cậy.
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_r:
        st.markdown("""
            <div class="rule-card">
                <div class="rule-header bg-green">ĐỘI NGŨ PHÁT TRIỂN</div>
                <div style="padding:20px;">
                    <b>Đội ngũ DVT - Empire CBZ X</b><br>
                    - Nhóm chuyên gia về AI & An ninh mạng.<br>
                    - Đơn vị tiên phong trong các giải pháp công nghệ vì cộng đồng.<br>
                    - Địa điểm: THPT Dương Văn Thì.
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TRANG TIN TỨC (ĐÃ THÊM NỘI DUNG) ---
elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="rules-main-header">BẢN TIN AN NINH MẠNG MỚI NHẤT</div>', unsafe_allow_html=True)
    
    news_list = [
        {"title": "Cảnh báo lừa đảo mã QR tại các nhà hàng", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "desc": "Tội phạm dán đè mã QR lạ lên mã của cửa hàng để chiếm đoạt tài khoản..."},
        {"title": "Deepfake: Cuộc gọi giả danh con cháu", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "desc": "Công nghệ AI tạo hình ảnh và giọng nói giả người thân để vay tiền gấp..."},
        {"title": "Bẫy 'Việc nhẹ lương cao' trên Facebook", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "desc": "Cảnh báo các sàn thương mại điện tử giả mạo tuyển cộng tác viên chốt đơn..."},
        {"title": "Giả danh cán bộ Công an, Viện kiểm sát", "img": "https://vnn-imgs-f.vgcloud.vn/2021/04/14/11/gia-danh-cong-an.jpg", "desc": "Người dân cần cảnh giác với các yêu cầu cài đặt phần mềm 'Dịch vụ công' lạ..."}
    ]

    for item in news_list:
        c1, c2 = st.columns([1, 3])
        with c1:
            st.image(item['img'], use_container_width=True)
        with c2:
            st.subheader(item['title'])
            st.write(item['desc'])
            st.button("Xem thêm", key=item['title'])
        st.markdown("---")

# --- TRANG VỆ SĨ AI ---
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

# Luôn gọi footer ở cuối trang
styles.render_footer_structure()
