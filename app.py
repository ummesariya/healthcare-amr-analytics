import streamlit as st
import pandas as pd
from pathlib import Path
import joblib


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Healthcare AMR Prediction",
    page_icon="🧬",
    layout="wide"
)


# --------------------------------------------------
# LOAD TRAINED PIPELINE
# --------------------------------------------------

MODEL_PATH = (
    Path(__file__).parent
    / "models"
    / "amr_prediction_pipeline.joblib"
)

model = joblib.load(MODEL_PATH)

# --------------------------------------------------
# CATEGORY OPTIONS
# --------------------------------------------------

category_values = {
    "age": [
        "18-24",
        "25-34",
        "35-44",
        "45-54",
        "55-64",
        "65-74",
        "75-84",
        "85-89",
        "above 90"
    ],

    "gender": [
        "0",
        "1"
    ],

    "ordering_mode": [
        "Inpatient",
        "Outpatient"
    ],

    "culture_description": [
        "URINE",
        "BLOOD",
        "RESPIRATORY"
    ],

    "organism": [
        "ESCHERICHIA COLI",
        "KLEBSIELLA PNEUMONIAE",
        "STAPHYLOCOCCUS AUREUS",
        "ENTEROCOCCUS FAECALIS"
    ],

    "antibiotic": [
        "Ampicillin",
        "Ertapenem",
        "Meropenem",
        "Tetracycline",
        "Ciprofloxacin",
        "Levofloxacin",
        "Nitrofurantoin"
    ]
}


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title(
    "Healthcare Antimicrobial Resistance (AMR) Prediction"
)

st.write(
    "This application provides a machine-learning interface "
    "for antimicrobial resistance prediction."
)

st.info(
    "This is a portfolio prototype. Predictions should not "
    "be used for clinical decision-making."
)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.header("Patient and Culture Information")

col1, col2 = st.columns(2)


# --------------------------------------------------
# LEFT COLUMN
# --------------------------------------------------

with col1:

    age = st.selectbox(
        "Age Group",
        category_values["age"]
    )

    gender = st.selectbox(
        "Recorded Gender Code",
        category_values["gender"]
    )

    ordering_mode = st.selectbox(
        "Ordering Mode",
        category_values["ordering_mode"]
    )

    culture_description = st.selectbox(
        "Culture Description",
        category_values["culture_description"]
    )

    organism = st.selectbox(
        "Organism",
        category_values["organism"]
    )


# --------------------------------------------------
# RIGHT COLUMN
# --------------------------------------------------

with col2:

    antibiotic = st.selectbox(
        "Antibiotic",
        category_values["antibiotic"]
    )

    order_month = st.number_input(
        "Order Month",
        min_value=1,
        max_value=12,
        value=1,
        step=1
    )

    order_quarter = st.number_input(
        "Order Quarter",
        min_value=1,
        max_value=4,
        value=1,
        step=1
    )

    order_dayofweek = st.number_input(
        "Order Day of Week",
        min_value=0,
        max_value=6,
        value=0,
        step=1
    )

    order_year = st.number_input(
        "Order Year",
        min_value=2006,
        max_value=2025,
        value=2024,
        step=1
    )


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("Predict AMR", type="primary"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "ordering_mode": [ordering_mode],
        "culture_description": [culture_description],
        "organism": [organism],
        "antibiotic": [antibiotic],
        "order_month": [order_month],
        "order_quarter": [order_quarter],
        "order_dayofweek": [order_dayofweek],
        "order_year": [order_year]
    })

    probability = model.predict_proba(input_data)[0, 1]

    prediction = int(probability >= 0.5)

    st.header("Prediction Result")

    st.metric(
        "Predicted AMR Probability",
        f"{probability:.1%}"
    )

    if prediction == 1:

        st.error(
            "Predicted outcome: Resistant (AMR = 1)"
        )

    else:

        st.success(
            "Predicted outcome: Susceptible (AMR = 0)"
        )