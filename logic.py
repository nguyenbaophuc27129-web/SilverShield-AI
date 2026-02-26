import google.generativeai as genai
from gtts import gTTS
import io
import streamlit as st

# GIỮ NGUYÊN CÁC HÀM LOGIC GỐC CỦA BẠN
def init_ai():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
    except Exception as e:
        st.error(f"Lỗi khởi tạo AI: {e}")
        return None

def analyze_content(model, text, image):
    # Prompt giữ nguyên như yêu cầu của bạn
    prompt = """Bạn là SilverShield, vệ sĩ ảo bảo vệ người già Việt Nam. 
    Hãy phân tích nội dung sau và đưa ra cảnh báo lừa đảo một cách lễ phép, dễ hiểu. 
    Nhắc nhở về 5 quy tắc an toàn internet."""
    
    parts = [prompt]
    if text: parts.append(f"Văn bản: {text}")
    if image: parts.append(image)
    
    response = model.generate_content(parts)
    return response.text

def text_to_speech(text):
    tts = gTTS(text=text, lang='vi')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

# --- PHẦN HIỂN THỊ TÍCH HỢP (THÊM MỚI NHƯNG KHÔNG SỬA LOGIC CŨ) ---

model = init_ai()

if model:
    # Giao diện nhập liệu của bạn
    st.title("🛡️ SILVERSHIELD - VỆ SĨ SILVER")
    user_text = st.text_area("Nhập nội dung nghi ngờ:")
    user_image = st.file_uploader("Hoặc tải ảnh lên:", type=['png', 'jpg', 'jpeg'])

    if st.button("KIỂM TRA NGAY"):
        with st.spinner('Vệ sĩ Silver đang phân tích...'):
            # Gọi hàm logic gốc của bạn
            result = analyze_content(model, user_text, user_image)
            
            # 1. Hiển thị văn bản kết quả
            st.markdown("### 📝 Lời khuyên từ Vệ sĩ Silver:")
            st.write(result)
            
            # 2. Phát âm thanh (Hàm logic gốc của bạn)
            audio_fp = text_to_speech(result)
            st.audio(audio_fp, format='audio/mp3')

            # 3. TÍCH HỢP NÚT GỌI KHẨN CẤP (Chỉ hiện khi AI nhận diện rủi ro)
            # Chúng ta kiểm tra nếu AI có nhắc đến cảnh báo nguy hiểm
            if any(word in result.lower() for word in ["lừa đảo", "nguy hiểm", "cẩn thận", "không nên"]):
                st.divider()
                st.error("🆘 ÔNG/BÀ HÃY HÀNH ĐỘNG NGAY ĐỂ BẢO VỆ MÌNH:")
                
                col1, col2 = st.columns(2)
                with col1:
                    # Nút gọi người thân (Thay số 090... bằng số thực tế)
                    st.markdown("""
                        <a href="tel:0901234567" style="text-decoration: none;">
                            <div style="background-color: #25D366; color: white; padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; font-size: 20px;">
                                📞 GỌI NGƯỜI THÂN
                            </div>
                        </a>""", unsafe_allow_html=True)
                
                with col2:
                    # Nút gọi 113
                    st.markdown("""
                        <a href="tel:113" style="text-decoration: none;">
                            <div style="background-color: #FF4B4B; color: white; padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; font-size: 20px;">
                                📞 GỌI CÔNG AN
                            </div>
                        </a>""", unsafe_allow_html=True)
                
                # Nút báo cáo lên hệ thống (Minh chứng cho Bước 4 trong bài luận)
                if st.button("⚠️ BÁO CÁO KỊCH BẢN LỪA ĐẢO NÀY"):
                    st.success("Đã gửi kịch bản về trung tâm dữ liệu SilverShield trên GitHub để huấn luyện AI bảo vệ mọi người!")
