import streamlit as st

# Set up the page title and clean layout
st.set_page_config(page_title="Hydraulic Pressure Calculator", layout="centered")

# --- Corporate Header ---
# Using the exact image name uploaded to GitHub
logo_path = "logo.png"

# Center the logo using HTML
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.image(logo_path, width=200)
st.markdown('</div>', unsafe_allow_html=True)

# Centered main title
st.markdown('<h1 style="text-align: center;">Target Load to Pressure Converter</h1>', unsafe_allow_html=True)
st.write("")

st.markdown("---")

# Define the static Cylinder Area
STATIC_AREA = 25.10

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    # Display the Area as static text (not editable)
    st.write("") 
    st.markdown(f"<p style='font-size: 1.1em; color: black; margin-top: 5px;'><b>Cylinder Area (cm²):</b> {STATIC_AREA:.2f}</p>", unsafe_allow_html=True)

with col2:
    # The ONLY editable input field
    force = st.number_input("Target Force (kN):", value=30.00, format="%.2f")

st.markdown("---")

# Calculation Logic
if STATIC_AREA > 0:
    pressure = force / (STATIC_AREA * 0.01)
    
    # Large, professional result display
    st.subheader("REQUIRED PRESSURE:")
    st.metric(label="", value=f"{pressure:.2f} bar")

# Floating space to push footer down
st.write("")
st.write("")

# Professional signature footer
st.markdown(
    "<p style='text-align: center; color: gray; font-style: italic; font-size: 0.85em;'>"
    "Prepared by Mohamed Abozaid | Senior Technical Engineer, Fischer Kuwait"
    "</p>", 
    unsafe_allow_html=True
)
