import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* --- 1. IMPORT FONT & GLOBAL SETUP --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Reset & Base */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #f7fafc; /* Nền xám nhạt */
            color: #2d3748;
        }
        .block-container {
            max-width: 1200px !important;
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
            margin: 0 auto !important;
        }
        [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

        /* --- 2. HEADER SYSTEM (Giống Olympic) --- */

        /* Tầng 1: Top Bar */
        .top-bar {
            background-color: #1a365d; /* Dark Blue */
            color: white;
            padding: 10px 0;
            font-size: 13px;
            font-weight: 500;
        }
        .top-bar-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 1rem;
        }
        .top-bar-btn {
            padding: 6px 15px;
            border-radius: 4px;
            color: white !important;
            font-weight: 600;
            text-decoration: none;
            margin-left: 10px;
        }
        .btn-red { background-color: #c53030; } /* Accent Red */
        .btn-gold { background-color: #f6ad55; } /* Accent Gold */

        /* Tầng 2: Navbar */
        .nav-container {
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            padding: 15px 0;
            position: sticky; top: 0; z-index: 1000;
        }
        .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }

        /* Nút menu text */
        div.stButton > button {
            background: transparent !important;
            color: #1a365d !important;
            border: none !important;
            font-weight: 600 !important;
            font-size: 15px !important;
            text-transform: uppercase !important;
            padding-bottom: 5px !important;
            border-bottom: 3px solid transparent !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            border-bottom: 3px solid #f6ad55 !important; /* Gạch chân vàng khi hover */
        }
        
        /* --- 3. HERO SECTION (BANNER) --- */
        .hero-section {
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://img.freepik.com/free-vector/digital-technology-background-with-abstract-wave-border_53876-117508.jpg');
            background-size: cover;
            background-position: center;
            padding: 50px 0;
            border-radius: 12px;
            overflow: hidden;
        }
        .hero-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }

        /* --- 4. CARDS & SECTIONS --- */
        .section-header {
            text-align: center;
            margin: 50px 0 30px 0;
        }
        .section-title {
            color: #1a365d;
            font-size: 28px;
            font-weight: 700;
            text-transform: uppercase;
        }
        .section-subtitle { color: #718096; }

        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
            height: 100%;
            transition: all 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
            border-color: #f6ad55;
        }
        .card-title {
            color: #1a365d;
            font-weight: 600;
            font-size: 18px;
            margin-bottom: 10px;
        }
        .card p { color: #4a5568; font-size: 15px; }

        /* --- 5. FOOTER --- */
        .footer {
            background: #1a365d;
            color: white;
            padding: 50px 0;
            margin-top: 60px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
