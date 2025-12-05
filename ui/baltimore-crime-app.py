import streamlit as st
import pandas as pd
import joblib

st.title("Crime Description Prediction Based on Spatial-Temporal Data")

hgb_model = joblib.load("models/hgb_model.pkl")
cb_model = joblib.load("models/cb_model.pkl")

st.subheader("Please choose the location.")