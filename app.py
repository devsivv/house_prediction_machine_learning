import streamlit as st
import pandas as pd
from xgboost import XGBRegressor

model = XGBRegressor()
model.load_model("xgb_model.json")

st.title("🏠 Boston House Price Prediction")

st.sidebar.title("Model Information")
st.sidebar.write("Model: XGBoost Regressor")
st.sidebar.write("R² Score: 0.905")
st.sidebar.write("Dataset: Boston Housing")

crime_rate = st.number_input("Crime Rate", min_value=0.0)
residential_land_ratio = st.number_input("Residential Land Ratio", min_value=0.0)
non_retail_business_ratio = st.number_input("Non Retail Business Ratio", min_value=0.0)
near_charles_river = st.selectbox("Near Charles River", [0, 1])
nitric_oxide_concentration = st.number_input("Nitric Oxide Concentration", min_value=0.0)
avg_rooms_per_dwelling = st.number_input("Average Rooms Per Dwelling", min_value=0.0)
old_houses_ratio = st.number_input("Old Houses Ratio", min_value=0.0)
distance_to_employment_centers = st.number_input("Distance To Employment Centers", min_value=0.0)
highway_accessibility_index = st.number_input("Highway Accessibility Index", min_value=0)
property_tax_rate = st.number_input("Property Tax Rate", min_value=0.0)
pupil_teacher_ratio = st.number_input("Pupil Teacher Ratio", min_value=0.0)
black_population_index = st.number_input("Black Population Index", min_value=0.0)
lower_status_population_pct = st.number_input("Lower Status Population %", min_value=0.0)

if st.button("Predict Price"):

    input_data = pd.DataFrame([[
        crime_rate,
        residential_land_ratio,
        non_retail_business_ratio,
        near_charles_river,
        nitric_oxide_concentration,
        avg_rooms_per_dwelling,
        old_houses_ratio,
        distance_to_employment_centers,
        highway_accessibility_index,
        property_tax_rate,
        pupil_teacher_ratio,
        black_population_index,
        lower_status_population_pct
    ]], columns=[
        'crime_rate',
        'residential_land_ratio',
        'non_retail_business_ratio',
        'near_charles_river',
        'nitric_oxide_concentration',
        'avg_rooms_per_dwelling',
        'old_houses_ratio',
        'distance_to_employment_centers',
        'highway_accessibility_index',
        'property_tax_rate',
        'pupil_teacher_ratio',
        'black_population_index',
        'lower_status_population_pct'
    ])

    prediction = model.predict(input_data)

    st.metric(
    label="Predicted House Price",
    value=f"${prediction[0]*1000:,.2f}"
)