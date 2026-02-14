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

# --- 2. NAVBAR CHUẨN (FIX LOGO) ---

st.markdown('<div class="olympic-navbar"><div class="navbar-container" style="width:1200px; margin:0 auto; display:flex; align-items:center;">', unsafe_allow_html=True)

c_logo, m1, m2, m3, m4 = st.columns([1.5, 2, 2, 2, 2])



with c_logo:

    # Đã sửa link RAW để logo hiện lên

    st.markdown('<img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/t%E1%BA%A3i%20xu%E1%BB%91ng%20(1).png" style="height:50px; margin-left:15px;">', unsafe_allow_html=True)



with m1:

    if st.button("🏠 TRANG CHỦ", use_container_width=True): st.session_state['page'] = 'TRANG CHỦ'; st.rerun()

with m2:

    if st.button("👥 GIỚI THIỆU", use_container_width=True): pass

with m3:

    if st.button("📰 TIN TỨC", use_container_width=True): pass

with m4:

    if st.button("🛡️ VỆ SĨ AI", use_container_width=True): st.session_state['page'] = 'VỆ SĨ AI'; st.rerun()

st.markdown('</div></div>', unsafe_allow_html=True)


  # --- 3. ĐIỀU HƯỚNG TRANG CHỦ (BANNER FULL NỀN - DÍNH SÁT - VUÔNG GÓC) ---
if st.session_state['page'] == 'TRANG CHỦ':
    st.markdown("""
        <div style="background: #001529; width: 100%; padding: 50px 0; display: flex; justify-content: center; align-items: center;">
            <div style="display: flex; width: 1100px; height: 380px; box-shadow: 0 25px 50px rgba(0,0,0,0.5); border: none;">
                
                <div style="flex: 1; height: 100%; overflow: hidden;">
                    <img src="https://raw.githubusercontent.com/nguyenbaophuc27129-web/SilverShield-AI/main/%E1%BA%A8M%20TH%E1%BB%B0C%20A4%20(1).png" 
                         style="width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0;">
                </div>

                <div style="flex: 1; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); 
                            display: flex; flex-direction: column; align-items: center; justify-content: center; 
                            text-align: center; border-radius: 0; border-left: 1px solid rgba(255,255,255,0.1);">
                    
                    <h2 style="font-family: 'Roboto', sans-serif; color:#FFB300; margin:0; font-size: 42px; font-weight: 900; text-transform: uppercase; line-height: 1.1;">VỆ SĨ<br>SILVER</h2>
                    <div style="height: 5px; background: #d32f2f; width: 80px; margin: 20px auto;"></div>
                    <p style="font-family: 'Roboto', sans-serif; font-size: 18px; color: white; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Hệ thống AI bảo vệ người già</p>
                    
                    <div style="height: 40px;"></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # NÚT BẤM (CĂN GIỮA VÀO KHỐI BÊN PHẢI)
    st.markdown('<div style="margin-top: -100px; position: relative; z-index: 1000; display: flex; justify-content: center; width: 100%; padding-left: 370px;">', unsafe_allow_html=True)
    if st.button("KIỂM TRA NGAY", key="hero_btn"):
        st.session_state['page'] = 'VỆ SĨ AI'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    # --- KHỐI: VỀ ỨNG DỤNG & HƯỚNG DẪN ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_intro, c_guide = st.columns(2, gap="large")
    with c_intro:
        st.markdown('<div class="banner-strip"><div class="banner-header">VỀ ỨNG DỤNG</div><p style="text-align:justify; color:#555; font-size:14px;">SilverShield là giải pháp công nghệ tiên phong, sử dụng trí tuệ nhân tạo để phân tích và cảnh báo lừa đảo trực tuyến cho người cao tuổi.</p></div>', unsafe_allow_html=True)
    with c_guide:
        st.markdown('<div class="banner-strip"><div class="banner-header">HƯỚNG DẪN</div><ul style="text-align:left; color:#555; font-size:14px;"><li>Bước 1: Chọn "Vệ sĩ AI"</li><li>Bước 2: Nhập nội dung nghi ngờ</li><li>Bước 3: Xem kết quả cảnh báo</li></ul></div>', unsafe_allow_html=True)

    # --- KHỐI: QUY TẮC AN TOÀN ---
    st.markdown('<div class="rules-main-header">🛡️ QUY TẮC AN TOÀN KHÔNG GIAN MẠNG</div>', unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3, gap="medium")
    with r1:
        st.markdown('<div class="rule-card"><div class="rule-header bg-red">5 KHÔNG</div><div style="padding:15px; font-size:13px;">1. Không chuyển tiền<br>2. Không bấm link lạ<br>3. Không đưa OTP<br>4. Không cài app lạ<br>5. Không sợ đe dọa</div></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="rule-card"><div class="rule-header bg-green">3 NÊN</div><div style="padding:15px; font-size:13px;">1. Nên gọi xác thực<br>2. Nên hỏi con cháu<br>3. Nên báo công an</div></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="rule-card"><div class="rule-header bg-teal">LƯU Ý</div><div style="padding:15px; font-size:13px;">1. Luôn bình tĩnh<br>2. Đọc tin an ninh<br>3. Dùng SilverShield</div></div>', unsafe_allow_html=True)

    # --- KHỐI TIN TỨC ---
    st.markdown('<div class="news-header-bar" style="background:#0044cc; color:white; padding:10px; margin-top:30px; font-weight:bold;">📰 TIN TỨC AN NINH MẠNG</div>', unsafe_allow_html=True)
    news_data = [
        {"title": "Cảnh báo lừa đảo mã QR", "img": "https://vnn-imgs-f.vgcloud.vn/2023/08/15/11/qr-code-lua-dao.jpg", "url": "https://chinhphu.vn/"},
        {"title": "Deepfake giả giọng nói", "img": "https://vnn-imgs-f.vgcloud.vn/2023/03/27/10/deepfake-lua-dao.jpg", "url": "https://tuoitre.vn/"},
        {"title": "Bẫy việc làm trên mạng", "img": "https://vnn-imgs-f.vgcloud.vn/2022/06/20/16/lua-dao-viec-lam.jpg", "url": "https://vnexpress.net/"}
    ]
    cols = st.columns(3)
    for idx, item in enumerate(news_data):
        with cols[idx]:
            st.markdown(f'<div class="news-card" style="background:white; border:1px solid #eee;"><img src="{item["img"]}" style="width:100%; height:150px; object-fit:cover;"><div style="padding:10px; font-weight:bold; font-size:13px;">{item["title"]}</div></div>', unsafe_allow_html=True)
            st.link_button("CHI TIẾT", item['url'], use_container_width=True)

# --- GIỮ NGUYÊN PHẦN LOGIC VỆ SĨ AI ---
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

elif st.session_state['page'] == 'GIỚI THIỆU':
    st.markdown('<div class="rules-main-header">ĐỘI NGŨ PHÁT TRIỂN</div>', unsafe_allow_html=True)

styles.render_footer_structure()































