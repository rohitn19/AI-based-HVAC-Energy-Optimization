import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="HVAC Energy Optimization",
    page_icon="🏢",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton>button {
    width: 100%;
    background-color: #0066cc;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background-color: #004c99;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #003366;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load("hvac_energy_model.pkl")
features = joblib.load("feature_columns.pkl")

# =========================================
# TITLE
# =========================================

st.title("🏢 AI-Powered HVAC Energy Optimization")

st.markdown("""
Predict building HVAC energy consumption and receive
smart optimization recommendations in real time.
""")

st.divider()

# =========================================
# HELPER LABELS
# =========================================

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

weekday_names = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# =========================================
# HOUR LABEL FUNCTION
# =========================================

def get_time_label(hour):

    if 5 <= hour < 12:
        return "🌅 Morning"

    elif 12 <= hour < 17:
        return "☀️ Afternoon"

    elif 17 <= hour < 21:
        return "🌇 Evening"

    else:
        return "🌙 Night"

# =========================================
# LAYOUT
# =========================================

col1, col2 = st.columns(2)

# =========================================
# LEFT COLUMN
# =========================================

with col1:

    st.subheader("🏗️ Building Information")

    square_feet = st.number_input(
        "Building Area (sq ft)",
        min_value=100,
        max_value=1000000,
        value=50000,
        step=100
    )

    building_age = st.number_input(
        "Building Age (Years)",
        min_value=0,
        max_value=100,
        value=10
    )

    st.caption("ℹ️ Site ID Range: 0 to 15")

    site_id = st.number_input(
        "Site ID",
        min_value=0,
        max_value=15,
        value=0,
        step=1
    )

    st.subheader("🌡️ Weather Conditions")

    air_temperature = st.slider(
        "Air Temperature (°C)",
        0,
        60,
        30
    )

    dew_temperature = st.slider(
        "Dew Temperature (°C)",
        0,
        40,
        20
    )

    wind_speed = st.slider(
        "Wind Speed (m/s)",
        0,
        30,
        5
    )

# =========================================
# RIGHT COLUMN
# =========================================

with col2:

    st.subheader("🕒 Time Information")

    hour = st.slider(
        "Hour of Day",
        0,
        23,
        14
    )

    st.info(
        f"Selected Time: {hour}:00 hrs ({get_time_label(hour)})"
    )

    month = st.slider(
        "Month",
        1,
        12,
        6
    )

    st.info(
        f"Selected Month: {month_names[month]}"
    )

    weekday = st.slider(
        "Weekday",
        0,
        6,
        2
    )

    st.info(
        f"Selected Day: {weekday_names[weekday]}"
    )

    is_weekend = st.toggle(
        "Weekend Mode",
        value=False
    )

    is_weekend_value = 1 if is_weekend else 0

    st.subheader("❄️ HVAC Parameters")

    cooling_load_factor = st.slider(
        "Cooling Load Factor "
        "(Relative Cooling Demand Index)",
        0.0,
        2.0,
        1.0
    )

    prev_hour_meter = st.number_input(
        "Previous Hour Energy (kWh)",
        value=100.0
    )

    rolling_24h_avg = st.number_input(
        "24 Hour Avg Energy (kWh)",
        value=120.0
    )

    # =====================================
    # NEW FEATURE — OCCUPANCY
    # =====================================

    occupancy = st.slider(
        "Building Occupancy (%)",
        0,
        100,
        70
    )

# =========================================
# CREATE INPUT DATA
# =========================================

input_data = pd.DataFrame({

    'square_feet': [square_feet],
    'building_age': [building_age],
    'site_id': [site_id],
    'air_temperature': [air_temperature],
    'dew_temperature': [dew_temperature],
    'wind_speed': [wind_speed],
    'hour': [hour],
    'month': [month],
    'weekday': [weekday],
    'is_weekend': [is_weekend_value],
    'cooling_load_factor': [cooling_load_factor],
    'prev_hour_meter': [prev_hour_meter],
    'rolling_24h_avg': [rolling_24h_avg]

})

# =========================================
# MATCH FEATURES
# =========================================

for col in features:

    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[features]

st.divider()

# =========================================
# PREDICTION BUTTON
# =========================================

if st.button("⚡ Predict HVAC Energy Usage"):

    prediction_log = model.predict(input_data)

    prediction_actual = np.expm1(
        prediction_log
    )[0]

    # =====================================
    # DYNAMIC SETPOINT OPTIMIZATION
    # =====================================

    if air_temperature > 38:
        suggested_setpoint = 25

    elif air_temperature > 32:
        suggested_setpoint = 24

    else:
        suggested_setpoint = 22

    # =====================================
    # ENERGY SAVINGS ESTIMATION
    # =====================================

    estimated_savings = prediction_actual * 0.12

    # =====================================
    # KPI METRICS
    # =====================================

    st.subheader("📊 Smart HVAC KPIs")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        st.metric(
            "Predicted Energy",
            f"{prediction_actual:.2f} kWh"
        )

    with kpi2:

        st.metric(
            "Estimated Savings",
            f"{estimated_savings:.2f} kWh"
        )

    with kpi3:

        st.metric(
            "Suggested Setpoint",
            f"{suggested_setpoint}°C"
        )

    with kpi4:

        if prediction_actual < 300:
            hvac_status = "Low Load"

        elif prediction_actual < 700:
            hvac_status = "Moderate Load"

        else:
            hvac_status = "High Load"

        st.metric(
            "HVAC Status",
            hvac_status
        )

    st.divider()

    # =====================================
    # OPTIMIZATION RECOMMENDATIONS
    # =====================================

    st.subheader("💡 AI Optimization Recommendations")

    # =====================================
    # SETPOINT OPTIMIZATION
    # =====================================

    st.info(
        f"Recommended HVAC Setpoint: "
        f"{suggested_setpoint}°C"
    )

    # =====================================
    # HIGH TEMPERATURE + WEEKEND
    # =====================================

    if (
        air_temperature > 35
        and is_weekend_value == 1
    ):

        st.warning(
            "Increase HVAC setpoint by 1°C "
            "to reduce cooling load during "
            "low occupancy operation."
        )

    # =====================================
    # COOLING LOAD ALERT
    # =====================================

    if cooling_load_factor > 1.5:

        st.warning(
            "High cooling load detected. "
            "Inspect AHU efficiency and "
            "check chilled water flow."
        )

    # =====================================
    # PEAK DEMAND MANAGEMENT
    # =====================================

    if (
        hour >= 13
        and hour <= 17
        and prediction_actual > 900
    ):

        st.error(
            "Peak demand period detected. "
            "Consider load shedding strategy "
            "or temperature reset control."
        )

    # =====================================
    # OCCUPANCY-BASED OPTIMIZATION
    # =====================================

    if occupancy < 30:

        st.info(
            "Low occupancy detected. "
            "Reduce AHU airflow by 15% "
            "to improve energy efficiency."
        )

    # =====================================
    # FAN SPEED OPTIMIZATION
    # =====================================

    if (
        occupancy < 40
        and prediction_actual > 700
    ):

        st.info(
            "Reduce VFD fan speed by "
            "10–15% during low occupancy."
        )

    # =====================================
    # CHILLER EFFICIENCY CHECK
    # =====================================

    if (
        prediction_actual > 1200
        and cooling_load_factor > 1.5
    ):

        st.warning(
            "Inspect chiller COP and "
            "chilled water delta-T performance."
        )

    # =====================================
    # SENSOR / AHU FAULT DETECTION
    # =====================================

    if (
        air_temperature > 38
        and cooling_load_factor < 0.5
    ):

        st.error(
            "Possible temperature sensor "
            "calibration issue or AHU "
            "malfunction detected."
        )

    # =====================================
    # NORMAL OPERATION
    # =====================================

    if (
        prediction_actual < 700
        and cooling_load_factor < 1.2
        and occupancy > 40
    ):

        st.success(
            "✅ HVAC system operating efficiently."
        )

    st.divider()

    # =====================================
    # ENERGY STATUS
    # =====================================

    st.subheader("📈 Energy Consumption Status")

    if prediction_actual < 300:

        st.success(
            "🟢 Low Energy Consumption"
        )

    elif prediction_actual < 700:

        st.warning(
            "🟡 Moderate Energy Consumption"
        )

    else:

        st.error(
            "🔴 High Energy Consumption"
        )

    # =====================================
    # SAVINGS ANALYTICS
    # =====================================

    st.subheader("💰 Estimated Optimization Impact")

    st.success(
        f"Potential Daily Energy Savings: "
        f"{estimated_savings:.2f} kWh"
    )

    estimated_cost_savings = (
        estimated_savings * 10
    )

    st.success(
        f"Estimated Daily Cost Savings: "
        f"₹{estimated_cost_savings:.2f}"
    )

    # =====================================
    # SYSTEM HEALTH SCORE
    # =====================================

    st.subheader("🩺 HVAC System Health Score")

    health_score = 100

    if cooling_load_factor > 1.5:
        health_score -= 20

    if prediction_actual > 1000:
        health_score -= 25

    if occupancy < 30:
        health_score -= 10

    if air_temperature > 38:
        health_score -= 15

    st.progress(health_score / 100)

    st.info(
        f"System Health Score: "
        f"{health_score}/100"
    )