import google.generativeai as genai
from gtts import gTTS
import io
import streamlit as st

def init_ai():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        # Tự động chọn model
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
    except Exception as e:
        st.error(f"Lỗi khởi tạo AI: {e}")
        return None

def analyze_content(model, text, image):
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
