import streamlit as st
from PIL import Image
import styles
import logic

# --- 1. KHỞI TẠO & ÉP FOOTER SÁT ĐÁY DỨT ĐIỂM + TỐI ƯU CỠ CHỮ ---
styles.apply_styles()
styles.render_header_structure() 

st.markdown("""
    <style>
        /* Khóa chặt Footer xuống đáy tuyệt đối */
        .main .block-container {
            padding-top: 2rem !important;
            padding-bottom: 0rem !important; /* Triệt tiêu khoảng hở dưới cùng */
            max-width: 100% !important;
        }
        
        .stApp {
            display: flex;
            flex-direction: column;
            min-height: 100vh; /* Ép app chiếm toàn bộ chiều cao màn hình */
        }

        /* Ẩn rác của hệ thống */
        footer {visibility: hidden !important; height: 0;}
        header {visibility: hidden !important;}

        /* TĂNG CỠ CHỮ TO RÕ CHO NGƯỜI GIÀ */
        html, body, [class*="st-"] {
            font-size: 20px !important; 
        }
        .banner-header { font-size: 28px !important; font-weight: 900 !important; }
        .rule-header { font-size: 24px !important; }
        p, li { font-size: 20px !important; line-height: 1.6 !important; }
        
        /* Xóa khoảng cách thừa của dòng cuối */
        div[data-testid="stVerticalBlock"] > div:last-child {
            margin-bottom: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    model = logic.init_ai()
except:
    pass 

if 'page' not in st.session_state:
    st.session_state['page'] = 'TRANG CHỦ'

# --- 2. NAVBAR CHUẨN (CĂN CHỈNH KÍCH THƯỚC NÚT) ---
st.markdown('<div class="olympic-navbar"><div class="navbar-container" style="width:1200px; margin:0 auto; display:flex; align-items:center;">', unsafe_allow_html=True)
c_logo, m1, m2, m3, m4 = st.columns([1.5, 2, 2, 2, 2])

with c_logo:
    st.markdown('<img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:60px; margin-left:15px;">', unsafe_allow_html=True)

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
# Dùng container để bọc nội dung, giúp CSS flex-grow hoạt động
content_container = st.container()

with content_container:
    if st.session_state['page'] == 'TRANG CHỦ':
        # MẪU MỚI: BANNER TO Ở GIỮA, BỎ KHUNG ĐEN QUÊ MÙA
        banner_html = """
        <div style="width: 100%; display: flex; justify-content: center; padding: 20px 0;">
            <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png" 
                 style="width: 1100px; height: auto; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.4);">
        </div>
        """
        st.markdown(banner_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # CÁC KHUNG CHỮ TO RÕ
        c_intro, c_guide = st.columns(2, gap="large")
        with c_intro:
            st.markdown('<div class="banner-strip"><div class="banner-header">VỀ ỨNG DỤNG</div><p style="text-align:justify; color:#333; padding:15px;">SilverShield là "vệ sĩ ảo" giúp ông bà, cha mẹ tránh xa các cạm bẫy lừa đảo trên mạng bằng trí tuệ nhân tạo.</p></div>', unsafe_allow_html=True)
        with c_guide:
            st.markdown('<div class="banner-strip"><div class="banner-header">CÁCH DÙNG</div><ul style="text-align:left; color:#333; padding:15px;"><li><b>BƯỚC 1:</b> Nhấn nút "VỆ SĨ AI"</li><li><b>BƯỚC 2:</b> Nhập tin nhắn nghi ngờ</li><li><b>BƯỚC 3:</b> Xem kết quả từ máy tính</li></ul></div>', unsafe_allow_html=True)

        st.markdown('<div class="rules-main-header" style="font-size:26px !important;">🛡️ QUY TẮC VÀNG CHO NGƯỜI CAO TUỔI</div>', unsafe_allow_html=True)
        r1, r2, r3 = st.columns(3, gap="medium")
        with r1:
            st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div style="padding:15px; font-weight:bold;">1. Không chuyển tiền<br>2. Không bấm link lạ<br>3. Không đưa OTP<br>4. Không cài app lạ<br>5. Không sợ đe dọa</div></div>', unsafe_allow_html=True)
        with r2:
            st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div style="padding:15px; font-weight:bold;">1. Nên gọi xác thực<br>2. Nên hỏi con cháu<br>3. Nên báo công an</div></div>', unsafe_allow_html=True)
        with r3:
            st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý</div><div style="padding:15px; font-weight:bold;">1. Luôn bình tĩnh<br>2. Đọc tin an ninh<br>3. Dùng SilverShield</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:15px; margin-top:30px; font-weight:bold; font-size:24px;">📰 TIN TỨC CẦN BIẾT</div>', unsafe_allow_html=True)
        news_data = [
            {"title": "Lừa đảo qua mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://vtv.vn"},
            {"title": "Giả giọng nói người thân", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn"},
            {"title": "Bẫy việc làm lương cao", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net"}
        ]
        cols = st.columns(3)
        for idx, item in enumerate(news_data):
            with cols[idx]:
                st.markdown(f'<div class="news-card" style="background:white; border:1px solid #ddd;"><img src="{item["img"]}" style="width:100%; height:200px; object-fit:cover;"><div style="padding:15px; font-weight:bold; font-size:18px;">{item["title"]}</div></div>', unsafe_allow_html=True)
                st.link_button("XEM CHI TIẾT", item['url'], use_container_width=True)

    elif st.session_state['page'] == 'GIỚI THIỆU':
        st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN</div>', unsafe_allow_html=True)
        # Giữ nguyên code logic của bạn...
        st.write("Thông tin đội ngũ...")

    elif st.session_state['page'] == 'TIN TỨC':
        st.markdown('<div class="rules-main-header">📰 BẢN TIN AN NINH</div>', unsafe_allow_html=True)
        # Giữ nguyên code logic của bạn...
        st.write("Nội dung tin tức...")

    elif st.session_state['page'] == 'VỆ SĨ AI':
        st.markdown('<div class="rules-main-header">🛡️ TRUNG TÂM PHÂN TÍCH AI</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1], gap="large")
        with c1:
            txt = st.text_area("Nhập nội dung cần kiểm tra:", height=200)
            img = st.file_uploader("Tải ảnh chụp màn hình:", type=['png','jpg','jpeg'])
            if st.button("PHÂN TÍCH NGAY", type="primary", use_container_width=True):
                if txt or img:
                    with st.spinner("Đang kiểm tra..."):
                        i = Image.open(img) if img else None
                        st.session_state['res'] = logic.analyze_content(model, txt, i)
        with c2:
            if 'res' in st.session_state:
                st.success("KẾT QUẢ PHÂN TÍCH")
                st.write(st.session_state['res'])
                st.audio(logic.text_to_speech(st.session_state['res']))

# --- 4. FOOTER (KHÓA CHẶT Ở ĐÁY) ---
# Thêm div giãn cách để đẩy footer xuống nếu nội dung trang quá ngắn
st.markdown('<div style="flex-grow: 1;"></div>', unsafe_allow_html=True)
styles.render_footer_structure()
