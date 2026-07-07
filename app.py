import streamlit as st

# Set up the page title and clean layout
st.set_page_config(page_title="Hydraulic Pressure Calculator", layout="centered")

# Main Header
st.title("Target Load to Pressure Converter")
st.write("Enter your parameters below to instantly calculate the required gauge pressure.")

st.markdown("---")

# Two-column layout for inputs
col1, col2 = st.columns(2)

with col1:
    # Initialize with your exact spreadsheet value
    area = st.number_input("Cylinder Area (cm²):", value=25.10, format="%.2f")

with col2:
    # Initialize with your exact spreadsheet target force
    force = st.number_input("Target Force (kN):", value=30.00, format="%.2f")

st.markdown("---")

# Calculation Logic
if area > 0:
    pressure = force / (area * 0.01)
    
    # Large, professional result display
    st.subheader("REQUIRED PRESSURE:")
    st.metric(label="", value=f"{pressure:.2f} bar")
else:
    st.error("Cylinder Area must be greater than zero.")

# Floating space to push footer down
st.write("")
st.write("")

# Your professional signature footer
st.markdown(
    "<p style='text-align: center; color: gray; font-style: italic; font-size: 0.85em;'>"
    "Prepared by Mohamed Abozaid | Senior Technical Engineer, Fischer Kuwait"
    "</p>", 
    unsafe_allow_html=True
)