import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. PAGE CONFIG & FORCED THEME ---
st.set_page_config(page_title="YardMasters Ltd.", page_icon="🌳", layout="wide")

st.markdown("""
    <style>
    /* Forced Background Color */
    .stApp, .stAppViewContainer, .stMain {
        background-color: #f2f5f1 !important;
    }
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }
    h1, h2, h3, p, span, label {
        color: #2c3e2d !important;
    }
    .stButton>button {
        background-color: #3a5a40 !important;
        color: white !important;
        border-radius: 5px !important;
    }
    /* Simple styling for the data table */
    .stDataFrame {
        background-color: white !important;
        border-radius: 10px;
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
        "Status": "New"
    }])
    if not os.path.isfile(DB_FILE):
        new_data.to_csv(DB_FILE, index=False)
    else:
        new_data.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- 3. PUBLIC WEBSITE CONTENT ---
st.title("YardMasters Ltd.")
st.subheader("Professional Landscaping & Garden Care")

col_img1, col_img2 = st.columns(2)
with col_img1:
    st.image("mowing.png", caption="Maintenance", use_container_width=True)
with col_img2:
    st.image("planting.png", caption="Design", use_container_width=True)

st.write("---")

# --- 4. QUOTE FORM ---
st.header("Request a Free Site Survey")
f_col1, f_col2 = st.columns(2)

with f_col1:
    name = st.text_input("Name")
    contact = st.text_input("Phone Number or Email")
    service = st.selectbox("Service", ["Garden Tidy-up", "Landscaping", "Tree Work", "Other"])
    details = st.text_area("Details")
    
    if st.button("Submit Request"):
        if name and contact:
            save_data(name, contact, service, details)
            st.success("Thank you! Your request has been logged.")
        else:
            st.error("Please fill in your name and contact info.")

with f_col2:
    st.markdown("### 📞 Contact")
    st.write("**Area:** London & Surrounding")
    st.write("**Hours:** Mon - Sat, 08:00 - 18:00")

# --- 5. PRIVATE ADMIN PANEL ---
st.write("---")
with st.expander("🔐 Admin Login"):
    password = st.text_input("Enter Password", type="password")
    # You can change 'admin123' to whatever you want
    if password == "yardmasters2026":
        st.subheader("Current Quote Requests")
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            st.dataframe(df, use_container_width=True)
            
            # Option to download the list as Excel/CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Leads as CSV", data=csv, file_name="yardmasters_leads.csv")
        else:
            st.info("No requests received yet.")
    elif password:
        st.error("Incorrect password")

st.markdown("<br><center>© 2026 YardMasters Ltd.</center>", unsafe_allow_html=True)
