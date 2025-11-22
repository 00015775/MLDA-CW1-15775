import streamlit as st
import pandas as pd
import joblib

st.title("Student Final Grade (G3) Prediction App")

#rf_model = joblib.load("../src/models/rf_model.pkl")
#rf_features = joblib.load("../src/selected_features/rf_features.pkl")

rf_model = joblib.load("src/models/rf_model.pkl")
rf_features = joblib.load("src/selected_features/rf_features.pkl")

st.subheader("Please provide the student information")

def yes_no_input(label: str):
  value = st.radio(label, ["No", "Yes"])
  return 1 if value == "Yes" else 0

school_MS = yes_no_input("Does the student study at the 'MS' school? (Yes=MS, No=GP)")

Mjob_other = yes_no_input("Is the mother's job 'other'?")

Mjob_teacher = yes_no_input("Is the mother's job 'teacher'?")

reason_other = yes_no_input("Is the reason for choosing the school = 'other'?")

famsup_yes = yes_no_input("Does the student receive family support?")

age_allowed = [15, 16, 17, 18, 19, 20, 21, 22]
age = st.radio("Age (15–22)", age_allowed)

Medu_allowed = [0, 1, 2, 3, 4]
Medu = st.radio(
    "Mother's Education (0: none, 1: primary, 2: 5–9th, 3: secondary, 4: higher)",
    Medu_allowed
)

Fedu_allowed = [0, 1, 2, 3, 4]
Fedu = st.radio(
    "Father's Education (0: none, 1: primary, 2: 5–9th, 3: secondary, 4: higher)",
    Fedu_allowed
)

traveltime_allowed = [1, 2, 3, 4]
traveltime = st.radio(
    "Home → School Travel Time (1: <15min, 2: 15–30min, 3: 30–60min, 4: >1hr)",
    traveltime_allowed
)

studytime_allowed = [1, 2, 3, 4]
studytime = st.radio(
    "Weekly Study Time (1: <2h, 2: 2–5h, 3: 5–10h, 4: >10h)",
    studytime_allowed
)

failures_allowed = [0, 1, 2, 3]
failures = st.radio(
    "Number of Past Failures (0–3)",
    failures_allowed
)

famrel_allowed = [1, 2, 3, 4, 5]
famrel = st.radio("Family Relationship Quality (1–5)", famrel_allowed)

freetime_allowed = [1, 2, 3, 4, 5]
freetime = st.radio("Free Time After School (1–5)", freetime_allowed)

goout_allowed = [1, 2, 3, 4, 5]
goout = st.radio("Going Out With Friends (1–5)", goout_allowed)

Dalc_allowed = [1, 2, 3, 4, 5]
Dalc = st.radio("Workday Alcohol Consumption (1–5)", Dalc_allowed)

Walc_allowed = [1, 2, 3, 4, 5]
Walc = st.radio("Weekend Alcohol Consumption (1–5)", Walc_allowed)

health_allowed = [1, 2, 3, 4, 5]
health = st.radio("Health Status (1–5)", health_allowed)

absences = st.number_input("Number of School Absences (0–93)", min_value=0, max_value=93)

G1 = st.number_input("G1 – First Period Grade (0–20)", min_value=0, max_value=20)

G2 = st.number_input("G2 – Second Period Grade (0–20)", min_value=0, max_value=20)

input_dict = {
    "school_MS": school_MS,
    "Mjob_other": Mjob_other,
    "Mjob_teacher": Mjob_teacher,
    "reason_other": reason_other,
    "famsup_yes": famsup_yes,
    "age": age,
    "Medu": Medu,
    "Fedu": Fedu,
    "traveltime": traveltime,
    "studytime": studytime,
    "failures": failures,
    "famrel": famrel,
    "freetime": freetime,
    "goout": goout,
    "Dalc": Dalc,
    "Walc": Walc,
    "health": health,
    "absences": absences,
    "G1": G1,
    "G2": G2
}

user_df = pd.DataFrame([input_dict])

user_df = user_df.reindex(columns=rf_features, fill_value=0)

if st.button("Predict Final Grade (G3)"):
    prediction = rf_model.predict(user_df)[0]
    st.success(f"Predicted G3 Final Grade: {prediction:.2f}")

