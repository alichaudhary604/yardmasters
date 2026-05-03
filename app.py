import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="YardMasters Ltd. | Premium Landscaping", page_icon="🌿", layout="wide")

# --- CUSTOM GREEN THEME CSS ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #fcfdfc;
    }
    /* Headers */
    h1, h2, h3 {
        color: #1b3022 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Buttons */
    .stButton>button {
        background-color: #2e4a31 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        font-weight: bold;
    }
    /* Sidebar / Info boxes */
    .stAlert {
        background-color: #e8f5e9 !important;
        border: 1px solid #c8e6c9 !important;
        color: #1b5e20 !important;
    }
    </style>
    """, unsafe_base64=True)

# --- HEADER SECTION ---
col_logo, col_title = st.columns([1, 4])
with col_title:
    st.title("YardMasters Ltd.")
    st.subheader("Bespoke Landscaping & Garden Maintenance")

# --- HERO IMAGE ---
st.image("https://images.unsplash.com/photo-1558904541-efa8c1965f1e?q=80&w=1200", use_container_width=True)

st.write("---")

# --- ABOUT & SERVICES ---
col1, col2 = st.columns(2)

with col1:
    st.header("Why Choose YardMasters?")
    st.write("""
    Based in London, **YardMasters Ltd.** is led by Aamir and a team of dedicated professionals. 
    We pride ourselves on being:
    - **Reliable:** We arrive on time, every time.
    - **Efficient:** Quick turnarounds without sacrificing quality.
    - **Versatile:** From heavy landscaping to indoor 'bits and bobs'.
    """)

with col2:
    st.header("Our Services")
    tab1, tab2, tab3 = st.tabs(["Gardening", "Landscaping", "Maintenance"])
    with tab1:
        st.write("Full garden tidy-ups, weeding, and planting.")
    with tab2:
        st.write("Patios, decking, fencing, and turfing.")
    with tab3:
        st.write("Regular lawn care and seasonal clearances.")

st.write("---")

# --- TESTIMONIALS ---
st.header("What Our Clients Say")
t_col1, t_col2 = st.columns(2)

with t_col1:
    st.info("**'Aamir did a great job... very hard-working and efficient. Got everything done to a good standard.'**")
with t_col2:
    st.info("**'The quote was very competitive... the team did a great job clearing all debris.'**")

st.write("---")

# --- CONTACT & FOOTER ---
st.header("Get Your Free Quote")
contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown("### 📞 Contact Details")
    st.write("**Phone:** [Click to call Aamir]") # Replace with real phone
    st.write("**Area:** Serving London & Surrounding Areas")
    st.write("**Rating:** ⭐⭐⭐⭐⭐ (5.0 on Google Maps)")
    
    # Button to link to their actual Google Maps listing
    st.link_button("View Our Reviews on Google", "https://maps.app.goo.gl/FxYksuPrLMZ24pr67")

with contact_col2:
    st.markdown("### ✉️ Send a Message")
    name = st.text_input("Your Name")
    msg = st.text_area("How can we help?")
    if st.button("Send Request"):
        st.success(f"Thanks {name}! Aamir will be in touch shortly.")

st.markdown("<br><hr><center>© 2026 YardMasters Ltd. | Built by YourAgency</center>", unsafe_base64=True)
