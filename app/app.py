from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Health Insurance Cost Predictor")

st.write(
    """
    Enter patient information to estimate
    medical insurance charges using our trained AI model.
    """
)

# =========================
# LOAD MODEL
# =========================
MODEL_PATH = Path("models/health_insurance_xgboost_model.joblib")

model = joblib.load(MODEL_PATH)

# =========================
# USER INPUTS
# =========================
age = st.slider("Age", 18, 100, 30)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

bmi = st.slider(
    "BMI",
    10.0,
    60.0,
    25.0
)

children = st.slider(
    "Number of Children",
    0,
    10,
    0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    [
        "northeast",
        "northwest",
        "southeast",
        "southwest"
    ]
)

# =========================
# PREDICTION
# =========================
if st.button("Predict Insurance Charges"):

    input_data = pd.DataFrame([
        {
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "children": children,
            "smoker": smoker,
            "region": region
        }
    ])

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Medical Charges: ${prediction:,.2f}"
    )