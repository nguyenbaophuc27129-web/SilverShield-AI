import streamlit as st
import google.generativeai as genai
from PIL import Image
from gtts import gTTS
import io

# --- 1. CẤU HÌNH TRANG WEB ---
st.set_page_config(
    page_title="SilverShield - Lá Chắn Bảo Vệ",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS TỐI ƯU CHO NGƯỜI GIÀ (CHỮ TO, RÕ RÀNG) ---
st.markdown("""
    <style>
    /* Chỉnh phông chữ to toàn bộ web */
    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
    }
    h1 { color: #2E7D32; font-size: 40px !important; font-weight: bold; }
    h2 { color: #1565C0; font-size: 30px !important; }
    h3 { color: #D84315; font-size: 26px !important; }
    p, div, label, span { font-size: 20px !important; line-height: 1.6; }
    
    /* Nút bấm to đùng */
    .stButton button {
        background-color: #d32f2f;
        color: white;
        font-size: 24px !important;
        padding: 15px 30px;
        border-radius: 15px;
        width: 100%;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .stButton button:hover {
        background-color: #b71c1c;
        color: white;
    }
    
    /* Khung chat */
    .stTextArea textarea {
        font-size: 20px !important;
        background-color: #f1f8e9;
        border: 2px solid #81c784;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CẤU HÌNH AI GEMINI ---
# Lấy API Key từ Secrets của Streamlit (Sẽ cài đặt sau trên web)
# --- 3. CẤU HÌNH AI GEMINI (ĐOẠN ĐÃ SỬA) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Tìm kiếm model khả dụng để không bị lỗi NotFound
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # Ưu tiên chọn gemini-1.5-flash, nếu không có thì lấy cái đầu tiên
    target_model = 'models/gemini-1.5-flash'
    if target_model not in available_models:
        target_model = available_models[0]
        
    model = genai.GenerativeModel(target_model)
    st.sidebar.success(f"✅ Đang dùng: {target_model}")
except Exception as e:
    st.error(f"⚠️ Lỗi cấu hình API: {e}")

# --- 4. HÀM XỬ LÝ ---
def text_to_speech(text):
    """Chuyển văn bản thành giọng nói tiếng Việt"""
    try:
        tts = gTTS(text=text, lang='vi')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp
    except Exception as e:
        st.error(f"Lỗi giọng nói: {e}")
        return None

def analyze_content(text, image):
    """Gửi nội dung cho Gemini phân tích"""
    system_prompt = """
    Bạn là SilverShield, vệ sĩ ảo bảo vệ người cao tuổi Việt Nam.
    Nhiệm vụ: Phân tích xem nội dung có lừa đảo không.
    Phong cách: Lễ phép, nhẹ nhàng như con cháu, gọi người dùng là "Ông/Bà/Bác", xưng "Cháu".
    
    Quy tắc trả lời:
    1. Kết luận ngay: [AN TOÀN] hay [CẢNH BÁO LỪA ĐẢO].
    2. Giải thích đơn giản: Tại sao lại thế (VD: Họ dọa nạt, họ đòi tiền trước...).
    3. Lời khuyên: Cần làm gì ngay (VD: Xóa tin nhắn, gọi con cháu).
    4. Trích dẫn 1 quy tắc an toàn (Giữ an toàn, Không gặp gỡ, Đừng chấp nhận, Kiểm tra, Hãy nói ra).
    """
    
    prompt_parts = [system_prompt]
    if text:
        prompt_parts.append(f"Nội dung văn bản: {text}")
    if image:
        prompt_parts.append(image)
        prompt_parts.append("Hãy xem kỹ ảnh này có dấu hiệu lừa đảo không (logo giả, tin nhắn giả...).")
        
    response = model.generate_content(prompt_parts)
    return response.text

# --- 5. GIAO DIỆN CHÍNH (SIDEBAR NAVIGATION) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9664/9664268.png", width=150) # Logo mẫu
    st.title("MENU ĐIỀU KHIỂN")
    page = st.radio("Chọn mục:", ["🏠 Trang Chủ", "📰 Tin Tức Cảnh Báo", "🛡️ Vệ Sĩ AI (Kiểm Tra)"])
    st.markdown("---")
    st.info("**Đường dây nóng:** 156 (Báo lừa đảo)")

# --- TRANG 1: TRANG CHỦ ---
if page == "🏠 Trang Chủ":
    st.title("🛡️ CHÀO MỪNG ĐẾN VỚI SILVERSHIELD")
    st.subheader("Lá chắn AI bảo vệ người cao tuổi trên không gian mạng")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/grandma-concept-illustration_114360-16147.jpg", caption="Người bạn của người cao tuổi")
    with col2:
        st.markdown("""
        **Ông Bà, Cô Bác có bao giờ gặp tình huống này?**
        - 📞 Có người lạ gọi điện đòi chuyển tiền gấp?
        - 🎁 Nhận tin nhắn trúng thưởng xe máy, tivi?
        - 💑 Có "người yêu nước ngoài" hứa gửi quà về?
        
        👉 **Đừng lo! Đã có SilverShield ở đây.**
        Cháu là một vệ sĩ ảo, giúp Ông Bà kiểm tra mọi tin nhắn, hình ảnh xem có phải lừa đảo không.
        """)
        if st.button("BẤM VÀO ĐÂY ĐỂ KIỂM TRA NGAY"):
            st.toast("Ông/Bà hãy chọn mục 'Vệ Sĩ AI' ở bên trái nhé!", icon="👈")

# --- TRANG 2: TIN TỨC CẢNH BÁO ---
elif page == "📰 Tin Tức Cảnh Báo":
    st.title("📰 BẢN TIN AN NINH MẠNG")
    st.markdown("*Nguồn tin tổng hợp từ Cục An toàn thông tin & Báo Chính Phủ*")
    
    # Tin 1
    with st.expander("🔴 CẢNH BÁO: Lừa đảo 'Con đang cấp cứu' (Mới nhất)", expanded=True):
        st.image("https://baochinhphu.vn/Uploaded/tranducmanh/2023_03_14/lua-dao-con-cap-cuu-2.jpg", width=400)
        st.warning("Chiêu trò: Kẻ gian gọi điện báo con cháu bị tai nạn, cần chuyển tiền mổ gấp.")
        st.success("✅ Cách xử lý: Tuyệt đối bình tĩnh. Gọi điện thoại trực tiếp cho con hoặc giáo viên chủ nhiệm để xác minh.")

    # Tin 2
    with st.expander("🔴 CẢNH BÁO: Giả danh Công an gọi video (Deepfake)"):
        st.write("Kẻ gian dùng AI ghép mặt công an, gọi video yêu cầu cài ứng dụng lạ để chiếm đoạt tài sản.")
        st.info("💡 Ghi nhớ: Công an KHÔNG làm việc qua điện thoại, KHÔNG yêu cầu chuyển tiền.")

# --- TRANG 3: VỆ SĨ AI (TÍNH NĂNG CHÍNH) ---
elif page == "🛡️ Vệ Sĩ AI (Kiểm Tra)":
    st.title("🛡️ KIỂM TRA TIN NHẮN LỪA ĐẢO")
    st.markdown("---")
    
    col_input, col_result = st.columns([1, 1])
    
    with col_input:
        st.markdown("### 1. Nhập thông tin cần kiểm tra:")
        user_input = st.text_area("Ông/Bà dán tin nhắn vào đây:", height=150, placeholder="Ví dụ: Cháu ơi chuyển tiền gấp...")
        
        uploaded_file = st.file_uploader("Hoặc tải ảnh chụp màn hình:", type=["jpg", "png", "jpeg"])
        img_data = None
        if uploaded_file:
            img_data = Image.open(uploaded_file)
            st.image(img_data, caption="Ảnh ông bà vừa tải lên", width=200)

        check_btn = st.button("🔍 KIỂM TRA NGAY GIÚP TÔI")

    with col_result:
        st.markdown("### 2. Kết quả phân tích:")
        
        if check_btn:
            if not user_input and not img_data:
                st.warning("⚠️ Ông/Bà chưa nhập gì cả ạ. Hãy dán tin nhắn hoặc gửi ảnh nhé!")
            else:
                with st.spinner("⏳ Cháu đang đọc kỹ, Ông/Bà đợi một chút nhé..."):
                    # Gọi AI xử lý
                    result_text = analyze_content(user_input, img_data)
                    
                    # Hiển thị text
                    st.success("💌 Lời nhắn từ SilverShield:")
                    st.write(result_text)
                    
                    # Phát âm thanh
                    audio_file = text_to_speech(result_text)
                    if audio_file:
                        st.audio(audio_file, format='audio/mp3', start_time=0)
                        st.caption("🔊 Bấm nút Play ở trên để nghe cháu đọc ạ.")

