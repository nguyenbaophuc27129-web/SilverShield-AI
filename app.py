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

# --- 2. NAVBAR ---
st.markdown('<div class="olympic-navbar"><div style="width:1200px; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, c_menu = st.columns([1.5, 8.5])

with c_logo:
    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/9664/9664268.png" style="height:60px; margin-top:-10px;">', unsafe_allow_html=True)

with c_menu:
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        if st.button("🏠 TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'
    with m2:
        if st.button("👥 GIỚI THIỆU", use_container_width=True): st.session_state['page'] = 'GIỚI THIỆU'
    with m3:
        if st.button("📰 TIN TỨC", use_container_width=True): st.session_state['page'] = 'TIN TỨC'
    with m4:
        if st.button("🛡️ VỆ SĨ AI", use_container_width=True): st.session_state['page'] = 'VỆ SĨ AI'
st.markdown('</div></div>', unsafe_allow_html=True)

# ==================== TRANG CHỦ (CHÍNH) ====================
if st.session_state['page'] == 'TRANG CHỦ':
    # --- PHẦN 1, 2, 3: BANNER CHÍNH (XẾP LỚP) ---
    st.markdown('<div class="hero-container"><div class="hero-bg-overlay"></div><div class="hero-content-wrapper">', unsafe_allow_html=True)
    
    col_hero_1, col_hero_2 = st.columns([2.5, 1])
    
    with col_hero_1:
        st.image("https://olympicenglish.vn/upload/banner-olympic-2025.png", use_container_width=True)
        
    with col_hero_2:
        st.markdown("""
        <div class="glass-box">
            <h2 style="color:#FFB300; margin-top:0;">VỆ SĨ SILVER</h2>
            <p style="font-size:14px; margin-bottom:20px;">Hệ thống AI bảo vệ người cao tuổi</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="btn-check-now">', unsafe_allow_html=True)
        if st.button("KIỂM TRA NGAY", use_container_width=True):
            st.session_state['page'] = 'VỆ SĨ AI'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True) 

    # --- KHỐI: VỀ ỨNG DỤNG & HƯỚNG DẪN ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_intro, c_guide = st.columns(2, gap="large")
    with c_intro:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">VỀ ỨNG DỤNG SILVERSHIELDAI</div>
            <div class="banner-divider"></div>
            <p style="text-align:justify; color:#555;">
                SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến, 
                được thiết kế chuyên biệt cho người cao tuổi với giao diện đơn giản, dễ sử dụng.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c_guide:
        st.markdown("""
        <div class="banner-strip">
            <div class="banner-header">HƯỚNG DẪN SỬ DỤNG SILVERSHIELDAI</div>
            <div class="banner-divider"></div>
            <ul style="text-align:left; color:#555; padding-left:20px;">
                <li>Bước 1: Truy cập mục "Vệ sĩ AI".</li>
                <li>Bước 2: Nhập văn bản hoặc tải ảnh cần kiểm tra.</li>
                <li>Bước 3: Nhận kết quả và lời khuyên từ AI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # --- KHỐI: QUY TẮC AN TOÀN ---
    st.markdown('<div class="rules-main-header">🛡️ CÁC QUY TẮC AN TOÀN TRÊN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3, gap="medium")
    with r1:
        st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div class="rule-body"><div class="rule-item">1. KHÔNG chuyển tiền cho người lạ</div><div class="rule-item">2. KHÔNG bấm link lạ</div><div class="rule-item">3. KHÔNG cung cấp mã OTP</div><div class="rule-item">4. KHÔNG cài app lạ</div><div class="rule-item">5. KHÔNG sợ hãi lời đe dọa</div></div></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div class="rule-body"><div class="rule-item">1. NÊN gọi điện xác thực lại</div><div class="rule-item">2. NÊN hỏi ý kiến con cháu</div><div class="rule-item">3. NÊN báo cơ quan chức năng (156)</div></div></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý QUAN TRỌNG</div><div class="rule-body"><div class="rule-item">1. Bình tĩnh trước mọi tình huống</div><div class="rule-item">2. Cập nhật tin tức thường xuyên</div><div class="rule-item">3. Sử dụng SilverShield để kiểm tra</div></div></div>', unsafe_allow_html=True)

    # --- KHỐI TIN TỨC ---
    st.markdown('<div class="news-header-bar">📰 Tin tức an ninh mạng</div>', unsafe_allow_html=True)
    news_data = [
        {"title": "Cảnh báo thủ đoạn lừa đảo chiếm đoạt tài khoản qua mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://chinhphu.vn/canh-bao-thu-doan-lua-dao-moi-qua-ma-qr-103230815"},
        {"title": "Deepfake giả danh người thân gọi video call vay tiền", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/canh-bao-lua-dao-bang-video-call-deepfake-20230327101530456.htm"},
        {"title": "Cảnh giác bẫy 'việc làm nhẹ lương cao' trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/cac-bay-lua-dao-truc-tuyen-pho-bien-tai-viet-nam-4621535.html"},
        {"title": "Cách nhận biết các trang web giả mạo cơ quan chức năng", "img": "https://ict-imgs.vnncdn.net/files/2023/05/22/gia-mao-website-1.jpg", "url": "https://xaydungchinhphu.vn/bo-cong-an-huong-dan-ky-nang-phong-chong-lua-dao-truc-tuyen-119230522"},
        {"title": "Rủi ro mất tài khoản ngân hàng từ việc cài app lạ (.apk)", "img": "https://vnn-imgs-f.vgcloud.vn/2023/07/05/09/app-gia-mao-thue.jpg", "url": "https://thanhnien.vn/canh-bao-mat-tien-vi-cai-app-la-gia-danh-co-quan-thue-185230705091530.htm"},
        {"title": "Chiến dịch nhận diện và phòng chống lừa đảo trực tuyến", "img": "https://vnn-imgs-f.vgcloud.vn/2023/06/23/14/chien-dich-lua-dao.jpg", "url": "https://mic.gov.vn/chien-dich-tuyen-truyen-ky-nang-nhan-dien-va-phong-chong-lua-dao-truc-tuyen-172230623143050.htm"}
    ]
    for i in range(0, 6, 3):
        cols = st.columns(3, gap="medium")
        for j in range(3):
            idx = i + j
            if idx < len(news_data):
                item = news_data[idx]
                with cols[j]:
                    st.markdown(f'<div class="news-card"><img src="{item["img"]}" style="width:100%; height:160px; object-fit:cover;"><div style="padding:15px;"><p style="font-weight:700; color:#002147; font-size:14px; height:60px; overflow:hidden;">{item["title"]}</p></div></div>', unsafe_allow_html=True)
                    st.link_button("ĐỌC CHI TIẾT", item['url'], use_container_width=True)

# --- CÁC TRANG KHÁC GIỮ NGUYÊN ---
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
        else: st.info("Kết quả sẽ hiển thị tại đây.")

elif st.session_state['page'] == 'TIN TỨC':
    st.markdown('<div class="news-header-bar">TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN</div>', unsafe_allow_html=True)

styles.render_footer_structure()
