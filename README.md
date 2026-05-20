# ⚡ Household Global Active Power Prediction System

An end-to-end Machine Learning project that predicts **Household Global Active Power Consumption** using historical electrical consumption data.  
The project leverages data preprocessing, feature engineering, regression modeling, and an interactive Streamlit web application for real-time prediction.

---

# 🚀 Project Overview

This project focuses on predicting household power consumption patterns using machine learning techniques.  
It helps analyze electrical energy usage based on multiple household parameters such as voltage, reactive power, and sub-metering values.

The application provides a user-friendly interface where users can input electrical parameters and instantly receive predicted global active power consumption.

---

# 🎯 Objectives

- Analyze household power consumption data
- Perform feature engineering on time-series attributes
- Train a Machine Learning regression model
- Build a real-time prediction interface using Streamlit
- Deploy an interactive AI-powered energy prediction system

---

# 🧠 Machine Learning Workflow

## 1. Data Collection
The dataset used contains household electrical power consumption measurements over time.

### Dataset Features:
- Global Reactive Power
- Voltage
- Sub Metering 1
- Sub Metering 2
- Sub Metering 3
- Date & Time Information

---

## 2. Data Preprocessing

Performed:
- Handling missing values
- Datetime conversion
- Feature extraction
- Numerical transformations
- Scaling using StandardScaler

### Extracted Time Features:
- Hour
- Day
- Month
- Weekday

---

## 3. Feature Engineering

Engineered meaningful temporal features from raw datetime values to improve prediction performance.

---

## 4. Model Training

### Algorithm Used:
- Random Forest Regressor

### Why Random Forest?
- Handles nonlinear relationships effectively
- Robust against overfitting
- Provides strong regression performance

---

## 5. Model Evaluation

The model performance was evaluated using regression metrics such as:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Manipulation |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning |
| Streamlit | Web Application |
| Joblib | Model Serialization |
| Matplotlib | Visualization |

---

# 📂 Project Structure

```bash
Household-Power-Prediction/
│
├── app.py
├── power_prediction.ipynb
├── model.pkl
├── scaler.pkl
├── household_power_consumption.txt
├── requirements.txt
├── README.md
```

---

# 🌐 Streamlit Application

The project includes a fully interactive Streamlit web application.

### User Inputs:
- Global Reactive Power
- Voltage
- Sub Metering Values
- Hour
- Day
- Month
- Weekday

### Output:
- Predicted Household Global Active Power Consumption

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/your-username/Household-Power-Prediction.git
```

---

## Navigate to Project Folder

```bash
cd Household-Power-Prediction
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📊 Example Prediction

## Input:

| Feature | Value |
|---|---|
| Voltage | 234 |
| Reactive Power | 0.4 |
| Sub Metering 1 | 0 |
| Sub Metering 2 | 1 |
| Sub Metering 3 | 17 |
| Hour | 18 |
| Day | 16 |
| Month | 12 |
| Weekday | 5 |

---

## Output:

```bash
Predicted Global Active Power: 4.28 kW
```

---

# 🔥 Key Highlights

✅ End-to-End Machine Learning Pipeline  
✅ Real-world Energy Consumption Dataset  
✅ Feature Engineering  
✅ Regression-Based Prediction  
✅ Streamlit Deployment Ready  
✅ Interactive User Interface  
✅ Scalable Project Architecture

---

# 📈 Future Improvements

- Deep Learning-based Forecasting
- Time-Series Prediction using LSTM
- Real-time Smart Meter Integration
- Energy Usage Visualization Dashboard
- Cloud Deployment
- API Integration

---

# 👩‍💻 Author

## Anushka Singh

BTech CSE (AI & Data Science) Student  
Passionate about Machine Learning, NLP, and AI-based Applications.

---

# 📜 License

This project is developed for educational and research purposes.

---

# ⭐ Acknowledgements

- UCI Household Electric Power Consumption Dataset
- Scikit-learn Documentation
- Streamlit Community

