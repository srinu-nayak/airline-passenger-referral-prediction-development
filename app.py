import pickle
import pandas as pd
import streamlit as st

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Prediction function (same as before)
def predict(seat_comfort, cabin_service, food_bev, entertainment, ground_service, value_for_money, traveller_type, cabin_class):
    input_data = pd.DataFrame({
        'seat_comfort': [seat_comfort],
        'cabin_service': [cabin_service],
        'food_bev': [food_bev],
        'entertainment': [entertainment],
        'ground_service': [ground_service],
        'value_for_money': [value_for_money],
        'traveller_type_Business': [1 if traveller_type == 'Business' else 0],
        'traveller_type_Couple Leisure': [1 if traveller_type == 'Couple Leisure' else 0],
        'traveller_type_Family Leisure': [1 if traveller_type == 'Family Leisure' else 0],
        'traveller_type_Solo Leisure': [1 if traveller_type == 'Solo Leisure' else 0],
        'cabin_Business Class': [1 if cabin_class == 'Business Class' else 0],
        'cabin_Economy Class': [1 if cabin_class == 'Economy Class' else 0],
        'cabin_First Class': [1 if cabin_class == 'First Class' else 0],
        'cabin_Premium Economy': [1 if cabin_class == 'Premium Economy' else 0],
    })

    prediction = model.predict(input_data)
    return "Recommend" if prediction[0] == 1 else "Not Recommend"

# Streamlit app UI
st.title("Airline Satisfaction Prediction")
st.write("Provide your travel experience ratings and get a recommendation prediction.")

seat_comfort = st.slider("Seat Comfort", 0, 5, 3)
cabin_service = st.slider("Cabin Service", 0, 5, 3)
food_bev = st.slider("Food and Beverage", 0, 5, 3)
entertainment = st.slider("Entertainment", 0, 5, 3)
ground_service = st.slider("Ground Service", 0, 5, 3)
value_for_money = st.slider("Value for Money", 0, 5, 3)

traveller_type = st.selectbox(
    "Traveller Type",
    ['Business', 'Couple Leisure', 'Family Leisure', 'Solo Leisure']
)

cabin_class = st.selectbox(
    "Cabin Class",
    ['Business Class', 'Economy Class', 'First Class', 'Premium Economy']
)

if st.button("Predict"):
    result = predict(
        seat_comfort, cabin_service, food_bev, entertainment, ground_service, value_for_money,
        traveller_type, cabin_class
    )
    st.success(f"Prediction: **{result}**")
