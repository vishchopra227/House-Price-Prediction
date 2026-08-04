import streamlit as st
import pickle

# Loads the  model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 House Price Predictor")

# taking the User inputs 
area = st.number_input(
    "Enter Area (sq.ft)",
    min_value=0.0,
    step=0.1,
    value=None,
    placeholder="e.g. 1200.5"
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    step=1,
    value=1
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1.0,
    step=0.5,
    value=1.0,
    format="%.1f"
)

# Prediction of the prices 
if st.button("Predict Price"):

    if area is None:
        st.error("Please enter the area.")
    else:
        prediction = model.predict([[area, bedrooms, bathrooms]])
        st.success(f"💰 Predicted Price: ₹{prediction[0]:,.2f}")