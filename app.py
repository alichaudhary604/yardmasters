import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. PAGE CONFIG & THEME OVERRIDE ---
st.set_page_config(page_title="YardMasters Ltd.", page_icon="🌳", layout="wide")

# This CSS targets the specific containers seen in your screenshot to kill the white background
st.markdown("""
    <style>
    /* Targets the main background and the specific block container in your screenshot */
    .stApp, 
    .stAppViewContainer, 
    .stMain, 
    .stAppViewBlockContainer, 
    [data-testid="stAppViewBlockContainer"],
    [data-testid="stVerticalBlock"] {
        background-color: #f2f5f1 !important;
    }
    
    /* Makes the top header transparent */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* Force all text to Charcoal Green for readability */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #2c3e2d !important;
    }

    /* Professional Button Styling */
    .stButton>button {
        background-color: #3a5a40 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        font-weight: bold;
    }

    /* Styling for the Admin Login and form fields */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #ffffff !important;
        color: #2c3e2d !important;
    }
    
    .stExpander {
        background-color: #ffffff !important;
        border: 1px solid #d1ead5 !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA STORAGE LOGIC ---
DB_FILE = "leads.csv"

def save_data(name, contact, service, details):
    new_data = pd.DataFrame([{
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Name": name,
        "Contact": contact,
        "Service": service,
        "Details": details,
    }])
    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- 3. PUBLIC WEBSITE CONTENT ---
st.title("YardMasters Ltd.")
st.subheader("Bespoke Landscaping & Garden Maintenance")
st.write("---")

# Portfolio Images
col_img1, col_img2 = st.columns(2)
with col_img1:
    st.image("planting.png", caption="Professional Garden Design", use_container_width=True)
with col_img2:
    st.image("mowing.png", caption="Expert Maintenance & Care", use_container_width=True)

st.write("---")

# --- 4. SERVICES SECTION ---
st.header("Our Services")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### 🌿 Maintenance")
    st.write("Hedge trimming, lawn care, and seasonal clearances.")
with c2:
    st.markdown("### 🏗️ Landscaping")
    st.write("Fencing, decking, and paving solutions.")
with c3:
    st.markdown("### 🍂 Cleanups")
    st.write("Full garden rejuvenation and waste removal.")

st.write("---")

# --- 5. THE QUOTE FORM ---
st.header("Request a Quote")
st.write("Submit your details and our team will contact you within 24 hours.")

form_left, form_right = st.columns(2)

with form_left:
    name = st.text_input("Full Name")
    contact = st.text_input("Phone Number / Email")
    service = st.selectbox("Service Required", ["Maintenance", "Landscaping", "Clearance", "Other"])
    details = st.text_area("Tell us about your project...")
    
    if st.button("Submit Request"):
        if name and contact:
            save_data(name, contact, service, details)
            st.success("Success! Your request has been recorded.")
        else:
            st.error("Please provide both your name and contact info.")

with form_right:
    st.markdown("### 📞 Contact Details")
    st.write("**07415792101**")
    st.write("**Area:** London & Surrounding Areas")
    st.write("**Hours:** Monday - Saturday, 08:00 - 18:00")
    st.info("Fully insured and highly recommended professionals.")

# --- 6. ADMIN PANEL ---
st.write("<br><br>", unsafe_allow_html=True)
st.write("---")
with st.expander("🔐 Business Owner Login"):
    st.write("Enter credentials to view current leads.")
    password = st.text_input("Password", type="password")
    
    if password == "yardmasters2026":
        st.subheader("Client Inquiries")
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.dataframe(df, use_container_width=True)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Export Leads to CSV", data=csv, file_name="yardmasters_leads.csv")
        else:
            st.info("No leads recorded yet.")
    elif password:
        st.error("Incorrect Password.")

st.markdown("<br><center>© 2026 YardMasters Ltd.</center>", unsafe_allow_html=True)
