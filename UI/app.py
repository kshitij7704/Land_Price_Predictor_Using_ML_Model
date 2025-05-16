import streamlit as st
import pandas as pd
import joblib

# ——— Page config & CSS ———
st.set_page_config(
    page_title="🏡 Real Estate Price Predictor",
    page_icon="🏞️",
    layout="wide",
)

# Custom CSS
st.markdown(
    """
    <style>
    /* Hide default menu & footer */
    #MainMenu, footer {visibility: hidden;}
    
    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #E3F2FD 0%, #FFFFFF 100%);
    }
    /* Header styling */
    .header {
        background-color: #1565C0;
        padding: 2rem;
        border-radius: 0.5rem;
        color: white;
        text-align: center;
    }
    /* Card container */
    .card {
        background-color: white;
        padding: 2rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    /* Button styling */
    div.stButton > button {
        background-color: #0288D1;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        font-size: 1rem;
    }
    div.stButton > button:hover {
        background-color: #0277BD;
        color: #FFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ——— Header ———
st.markdown('<div class="header"><h1>🏡 Real Estate Price Predictor</h1>'
            '<p style="font-size:1.1rem;">Estimate land prices based on area, crime rate & location</p>'
            '</div>', unsafe_allow_html=True)

# ——— Load model & feature names ———
model = joblib.load('trained_model_all_data.joblib')
feature_columns = list(model.feature_names_in_)

# Extract location options
locations = sorted(col.split('_', 1)[1] for col in feature_columns if col.startswith('Location_'))

# ——— Layout: Sidebar for inputs ———
with st.sidebar:
    st.header("🔎 Enter Details")
    location = st.selectbox("Location", options=locations)
    area = st.number_input("Area (sq. units)", min_value=0.0, step=0.1, format="%.2f")
    crime_rate = st.number_input("Crime Rate (per 1000 people)", min_value=0.0, max_value=10.0, step=0.1, format="%.2f")
    predict = st.button("Predict Price")

# ——— Prediction & Display ———
if predict:
    # Build input vector
    data = {f: 0 for f in feature_columns}
    data['Area'] = area
    data['Crime Rate'] = crime_rate
    loc_col = f"Location_{location}"
    if loc_col in data:
        data[loc_col] = 1
    else:
        st.error(f"Location '{location}' not recognized by model.")
        st.stop()

    # Predict
    input_df = pd.DataFrame([data], columns=feature_columns)
    price = model.predict(input_df)[0]

    # Show result in a card
    st.markdown(
        f"""
        <div class="card">
            <h2 style="color:#1565C0;">💰 Predicted Price</h2>
            <p style="font-size:2.5rem; font-weight:bold; margin:0;">₹ {price:,.2f}</p>
            <p style="color:gray; margin-top:0.5rem;">for {location}, {area:.2f} sq units, crime rate {crime_rate:.2f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
