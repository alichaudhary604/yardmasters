import streamlit as st
import requests

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="YardMasters Ltd.", page_icon="🌳", layout="wide")

# --- 2. THEME & STYLING (Sage Green & Charcoal) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f2f5f1 !important;
    }
    h1, h2, h3 {
        color: #2c3e2d !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #3a5a40 !important;
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
        padding: 0.7rem 2rem !important;
    }
    .stAlert {
        background-color: #ffffff !important;
        border-left: 5px solid #a3b18a !important;
        color: #344e41 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HERO SECTION ---
st.title("YardMasters Ltd.")
st.subheader("Professional Landscaping & Garden Care Specialists")
st.write("---")

# --- 4. IMAGE GALLERY (Using your filenames) ---
col_img1, col_img2 = st.columns(2)
with col_img1:
    # Make sure mowing.png is uploaded to your GitHub repo
    st.image("mowing.png", caption="Precision Maintenance", use_container_width=True)
with col_img2:
    # Make sure planting.png is uploaded to your GitHub repo
    st.image("planting.png", caption="Expert Planting & Design", use_container_width=True)

st.write("---")

# --- 5. SERVICES ---
st.header("Our Professional Services")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### 🌿 Garden Tidy-Ups")
    st.write("Full seasonal clearances and garden rejuvenation.")
with c2:
    st.markdown("### 🏗️ Hard Landscaping")
    st.write("Quality paving, decking, and fencing.")
with c3:
    st.markdown("### 🌳 Maintenance")
    st.write("Expert hedge trimming and lawn care programs.")

st.write("---")

# --- 6. QUOTE REQUEST (The "Showroom" Form) ---
st.header("Request a Site Survey")
st.write("Provide your details below and our team will contact you within 24 hours.")

f_col1, f_col2 = st.columns(2)

with f_col1:
    name = st.text_input("Name")
    contact = st.text_input("Phone Number or Email")
    service = st.selectbox("Required Service", ["Garden Tidy-up", "Landscaping", "Tree Work", "Fencing", "Other"])
    details = st.text_area("Project Details")
    
    if st.button("Submit Quote Request"):
        if name and contact:
            # --- EMAILJS CONFIG ---
            # Paste your keys here from your EmailJS account
            service_id = "YOUR_SERVICE_ID"
            template_id = "YOUR_TEMPLATE_ID"
            public_key = "YOUR_PUBLIC_KEY"

            data = {
                "service_id": service_id,
                "template_id": template_id,
                "user_id": public_key,
                "template_params": {
                    "client_name": name,
                    "client_contact": contact,
                    "service_needed": service,
                    "details": details
                }
            }

            try:
                response = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=data)
                if response.status_code == 200:
                    st.success("Request sent! We will be in touch shortly.")
                else:
                    st.error("Submission failed. (Check your EmailJS Keys!)")
            except:
                st.error("System error. Check your connection.")
        else:
            st.warning("Please provide both your name and contact info.")

with f_col2:
    st.markdown("### 📞 Contact Information")
    st.write("**Service Area:** London & Surrounding Areas")
    st.write("**Business Hours:** Monday - Saturday, 08:00 - 18:00")
    st.write("**Direct Line:** [Add Phone Number Here]")
    st.info("Fully insured professionals providing competitive, transparent pricing.")

st.markdown("<br><hr><center>© 2026 YardMasters Ltd.</center>", unsafe_allow_html=True)
