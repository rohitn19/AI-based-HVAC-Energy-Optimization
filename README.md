# 🏢 AI-Powered HVAC Energy Prediction & Optimization Platform

## 📌 Project Overview

Commercial buildings consume a significant amount of energy through HVAC (Heating, Ventilation, and Air Conditioning) systems. Inefficient HVAC operation increases energy costs, reduces operational efficiency, and impacts sustainability goals.

This project leverages Machine Learning and HVAC domain engineering to forecast building energy consumption and provide intelligent optimization recommendations for smart building systems.

The platform predicts HVAC energy usage using environmental, operational, and building-related parameters while also suggesting optimization strategies to improve energy efficiency.

---

# 🚀 Key Features

* 🔮 HVAC Energy Consumption Prediction using XGBoost
* 🌡️ Dynamic HVAC Setpoint Optimization
* ⚡ Estimated Energy Savings Calculation
* 💰 Estimated Cost Savings Analysis
* 📈 Peak Demand Detection
* 🧠 AI-Based Optimization Recommendations
* 🏢 Occupancy-Aware HVAC Optimization
* 🩺 HVAC Operational Health Monitoring
* 📊 Interactive Streamlit Dashboard
* 📉 Real-Time Energy Consumption Analytics

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib

---

# 📂 Dataset

Dataset Used:
ASHRAE - Great Energy Predictor III Dataset

The dataset includes:

* Building metadata
* Weather conditions
* HVAC operational behavior
* Energy meter readings
* Time-series energy consumption data

---

# 🧠 Machine Learning Workflow

## Data Preprocessing

* Missing value handling
* Time-series sorting
* Log transformation of meter readings
* Outlier handling

## Feature Engineering

* Lag energy features
* Rolling 24-hour average consumption
* Cooling load factor
* Building age calculation
* Time-based features
* Occupancy-aware optimization features

## Model Training

* XGBoost Regressor
* Train/Test Split
* Performance evaluation using:

  * MAE
  * RMSE
  * R² Score

---

# 📊 Model Performance

| Metric   | Value  |
| -------- | ------ |
| MAE      | 32.57  |
| RMSE     | 124.18 |
| R² Score | 0.89   |

---

# 💡 Optimization Techniques Implemented

* HVAC Setpoint Optimization
* Occupancy-Based Airflow Reduction
* Peak Demand Management
* Chiller Efficiency Recommendations
* Fan Speed Optimization
* Estimated Energy Savings Analytics
* Cost Savings Estimation
* HVAC Health Score Monitoring

---

# 🖥️ Streamlit Dashboard Features

The dashboard allows users to:

* Input building and weather conditions
* Predict HVAC energy consumption
* Receive optimization recommendations
* Monitor system health
* Estimate energy and cost savings
* Analyze HVAC operational efficiency

---

# 📸 Dashboard Preview

(Add screenshots here)

Example:

![Dashboard Screenshot](dashboard.png)

---

# 🌐 Deployment

Live Application:
(Add Streamlit deployment link here)

GitHub Repository:
(Add GitHub repository link here)

---

# ▶️ How to Run Locally

## Clone Repository

```bash
git clone <your-repository-link>
```

## Navigate to Project Folder

```bash
cd AI-HVAC-Energy-Optimization
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit App

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

* Real-time IoT sensor integration
* BACnet/Modbus connectivity
* Deep Learning-based forecasting
* Reinforcement Learning HVAC optimization
* Real-time anomaly detection
* Predictive maintenance analytics

---

# 👨‍💻 Author

Instrumentation Engineer transitioning into AI/ML with focus on:

* Smart Building Analytics
* HVAC Optimization
* Industrial AI Applications
* Energy Analytics
* Intelligent Automation Systems
