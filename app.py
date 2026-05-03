import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="YardMasters Ltd. | London Landscaping",
    page_icon="🌿",
    layout="wide"
)

# --- 2. CUSTOM GREEN THEME (CSS) ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #fcfdfc;
    }
    h1, h2, h3 {
        color: #1b3022 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Customizing the Button */
    .stButton>button {
        background-color: #2e4a31 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.6rem 2rem !important;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3e6342 !important;
        border: none !important;
    }

    /* Testimonial Boxes */
    .stAlert {
        background-color: #e8f5e9 !important;
        border: 1px solid #c8e6c9 !important;
        color: #1b5e20 !important;
        border-radius: 10px;
    }
    
    /* Sidebar/Menu styling */
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & HERO SECTION ---
col_title, col_cta = st.columns([2, 1])

with col_title:
    st.title("YardMasters Ltd.")
    st.subheader("Bespoke Landscaping & Expert Garden Care")
    st.write("📍 **Serving London & Surrounding Areas**")

with col_cta:
    st.write(" ") # Spacing
    st.link_button("View Our 5-Star Reviews", "https://maps.app.goo.gl/FxYksuPrLMZ24pr67")

# Large Hero Image
st.image("https://images.unsplash.com/photo-1558904541-efa8c1965f1e?q=80&w=1200", use_container_width=True)

st.write("---")

# --- 4. SERVICES SECTION ---
st.header("Professional Services")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌿 Gardening")
    st.write("From seasonal tidy-ups to precision hedge trimming and planting.")

with col2:
    st.markdown("### 🏗️ Landscaping")
    st.write("High-quality patios, decking, fencing, and complete garden redesigns.")

with col3:
    st.markdown("### 🏠 Indoor Help")
    st.write("Aamir and the team also assist with indoor assembly and handiwork.")

st.write("---")

# --- 5. TESTIMONIALS (From Google Maps) ---
st.header("What Our Clients Say")
t_col1, t_col2 = st.columns(2)

with t_col1:
    st.info("""
    **"Aamir did a great job... very hard-working, effective, and efficient. 
    Got everything done to a good standard. Highly recommend."**
    """)
    st.info("""
    **"Excellent work by Aamir and his team. Professional and efficient."**
    """)

with t_col2:
    st.info("""
    **"The quote was very competitive... the team arrived on time and did a 
    great job clearing all debris. Excellent service."**
    """)
    st.info("""
    **"Great knowledge. Used YardMasters for removal and landscaping jobs. 
    Always professional."**
    """)

st.write("---")

# --- 6. INTERACTIVE QUOTE & CONTACT ---
st.header("Get an Estimate")
contact_left, contact_right = st.columns(2)

with contact_left:
    st.write("Ready to transform your space? Fill out the form or contact directly.")
    st.markdown("### 📞 Contact Info")
    st.write("**Phone:** 07XXX XXXXXX *(Ask Aamir for his number)*")
    st.write("**Email:** info@yardmasters.ltd")
    st.write("**Hours:** Mon-Sat, 8:00 AM - 6:00 PM")

with contact_right:
    name = st.text_input("Name")
    service_type = st.selectbox("Service Needed", ["Garden Tidy-up", "Landscaping", "Tree Trimming", "Handyman/Assembly"])
    details = st.text_area("Tell us about the project...")
    
    if st.button("Send Request to Aamir"):
        if name:
            st.success(f"Thank you, {name}! Your request for a {service_type} has been prepared. (Demo Only)")
        else:
            st.error("Please enter your name.")

# --- 7. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.caption("© 2026 YardMasters Ltd. | Built with ❤️ for Aamir")
