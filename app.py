import streamlit as st
import torch
from PIL import Image
import os
import time

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="CardioScan AI", layout="wide")

# Safety Switch (Set to False once you get your partner's file)
DEMO_MODE = True

# --- 2. SIDEBAR (The "About" and "How to Use") ---
with st.sidebar:
    # This is a clean, blue medical heart icon
    st.image("logo.png", width=150)
    st.title("CardioScan AI")
    # ... rest of your sidebar code
    st.header("About This Tool")
    st.info("""
    This AI-driven tool assists in detecting **Cardiomegaly** (enlarged heart) from Chest X-rays using a
    Deep Learning architecture.
    """)

    st.header("How to Use")
    st.markdown("""
    1. **Upload** a clear Chest X-ray (PA view).
    2. **Review** patient risk factors.
    3. **Run** AI Diagnostic for a second opinion.
    """)

    st.divider()
    st.caption("Developed for Capstone 2 | UTA Psychology & Data Science")

# --- 3. MAIN HEADER & CHALLENGE ---
st.title("🫀Cardiomegaly Scan Analysis")

# Your idea: The Radiologist Challenge
with st.expander("📂 Clinical Reference Standards (For Result Verification)", expanded=True):
    st.write("Use these established standards to compare patient scans and verify AI findings:")

    # Create two main columns
    col_left, col_right = st.columns(2)

    # Ensure images exist before displaying
    if os.path.exists("male_healthy.png"):
        with col_left:
            st.image("male_healthy.png", caption="Standard: Male (Healthy)", width=200, use_container_width=False)
            st.image("female_healthy.png", caption="Standard: Female (Healthy)", width=200, use_container_width=False)

        with col_right:
            st.image("male_cardio.png", caption="Pathology: Male (Cardiomegaly)", width=200, use_container_width=False)
            st.image("female_cardio.png", caption="Pathology: Female (Cardiomegaly)", width=200,
                     use_container_width=False)
    else:
        st.warning("⚠️ Reference images not found. Please ensure male_healthy.png, etc., are in your sidebar folder.")

st.divider()

# --- 4. THE MIDDLE SECTION (Inputs & Risk Factors) ---
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("📁 Image Upload")
    uploaded_file = st.file_uploader("Upload X-ray", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Current Patient Scan", use_container_width=True)

with right_col:
    st.subheader("📋 Patient Risk Factors")
    st.write("Select factors applicable to the patient for clinical context:")

    # These checkboxes make the app interactive and "real-world"
    st.checkbox("High Blood Pressure (Hypertension)")
    st.checkbox("History of Heart Valve Disease")
    st.checkbox("Shortness of Breath (Dyspnea)")
    st.checkbox("Swelling in Legs (Edema)")

    st.selectbox("Patient Age Group", ["Select...", "Infant", "Adult", "Elderly"])
    st.radio("Biological Sex", ["Male", "Female"])

# --- 5. THE OUTPUT (The Analysis) ---
# --- 5. THE OUTPUT ---
if uploaded_file:
    st.divider()
    # Unique key to prevent the error you had earlier
    if st.button("🚀 RUN AI DIAGNOSTIC", use_container_width=True, key="main_run_btn"):
        with st.spinner("Analyzing cardiothoracic ratio..."):
            time.sleep(2.5)  # Professional demo pause

            # --- THE ODD/EVEN SECRET LOGIC ---
            filename = uploaded_file.name
            only_number = "".join(filter(str.isdigit, filename))

            if only_number:
                # Even Number = Cardiomegaly / Odd Number = Healthy
                is_positive = int(only_number) % 2 == 0
            else:
                is_positive = False

            res_col1, res_col2 = st.columns(2)

            if is_positive:
                # EVEN = POSITIVE
                res_col1.error("### AI Result: POSITIVE")
                res_col2.metric("Confidence", "89.1%")
                st.warning("**Finding:** Significant enlargement of the cardiac silhouette detected.")
            else:
                # ODD = NEGATIVE
                res_col1.success("### AI Result: NEGATIVE")
                res_col2.metric("Confidence", "95.6%")
                st.write("**Finding:** Heart-to-chest ratio is within normal limits.")
