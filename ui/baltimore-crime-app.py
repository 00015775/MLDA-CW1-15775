import streamlit as st
import pandas as pd
import joblib

st.title("Crime Description Prediction Based on Spatial-Temporal Data")

hgb_model = joblib.load("./src/models/hgb_model.pkl")
expected_columns = hgb_model.feature_names_in_

# Location 
default_lat, default_lon = 39.2904, -76.6122
st.map(pd.DataFrame([{"lat": default_lat, "lon": default_lon}]))
lat = st.number_input("Latitude", value=default_lat, min_value=39.0, max_value=39.5, format="%.6f")
lon = st.number_input("Longitude", value=default_lon, min_value=-77.0, max_value=-76.3, format="%.6f")


# Time
st.subheader("Select Hour of the Day")
hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=12)


# Inside or Outside
st.subheader("Inside or Outside?")
inside_outside = st.radio("Location Type", ("Inside", "Outside"))
inside = 1 if inside_outside == "Inside" else 0


# Month
st.subheader("Select Month")
months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
month = st.selectbox("Month", months)


# Day
st.subheader("Select Day of the Week")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = st.selectbox("Day", days)


# Premise Type
st.subheader("Select Premise Type")
premise_types = [
    "DRUG STORE", "GARAGE", "GAS STATION", "OFFICE BUILDING", "OTHER", 
    "RESIDENTIAL", "RESTAURANT", "SCHOOL", "STREET", "WHOLESALE"
]
premise_type = st.selectbox("Premise Type", premise_types)


st.subheader("Prediction Features")
features = {
    "Latitude": lat,
    "Longitude": lon,
    "Hour": hour,
    "Inside_Outside": inside
}

months_model = [
    "Month_August",
    "Month_December",
    "Month_February",
    "Month_January",
    "Month_July",
    "Month_June",
    "Month_March",
    "Month_May",
    "Month_November",
    "Month_October",
    "Month_September"
]

days_model = [
    "Day_Monday",
    "Day_Saturday",
    "Day_Sunday",
    "Day_Thursday",
    "Day_Tuesday",
    "Day_Wednesday"
]

premise_types_model = [
    "PremiseType_DRUG STORE",
    "PremiseType_GARAGE",
    "PremiseType_GAS STATION                                       ",
    "PremiseType_OFFICE BUILDING",
    "PremiseType_OTHER",
    "PremiseType_RESIDENTIAL",
    "PremiseType_RESTAURANT",
    "PremiseType_SCHOOL",
    "PremiseType_STREET",
    "PremiseType_WHOLESALE"
]

# One-hot encoding of months
for col in months_model:
    features[col] = 1 if month.upper() in col.upper() else 0

# One-hot encoding of days
for col in days_model:
    features[col] = 1 if day.upper() in col.upper() else 0

# One-hot encoding of premise types
for col in premise_types_model:
    features[col] = 1 if premise_type.upper() in col.upper() else 0


features_df = pd.DataFrame([features])


# Predict
if st.button("Predict Crime Description"):
    prediction = hgb_model.predict(features_df)
    st.success(f"Predicted Crime Description: {prediction[0]}")

  
