⚡ Household Power Consumption Prediction using Machine Learning

An end-to-end Machine Learning project that predicts Global Active Power Consumption using household electrical measurements.
This project demonstrates the complete ML workflow including:

- Data preprocessing
- Feature engineering
- Data visualization
- Model training
- Model evaluation
- Model saving

Built using Python, Pandas, Scikit-learn, and Matplotlib.

---

📌 Project Overview

The goal of this project is to analyze household electricity consumption data and predict:

🎯 Target Variable

- "Global_active_power"

The project uses machine learning algorithms to understand energy usage patterns and generate accurate predictions.

---

🚀 Features

✅ Data Cleaning & Preprocessing
✅ Datetime Feature Extraction
✅ Feature Scaling using StandardScaler
✅ Linear Regression Model
✅ Random Forest Regressor Model
✅ RMSE & R² Score Evaluation
✅ Feature Importance Analysis
✅ Actual vs Predicted Visualization
✅ Model Saving with Joblib

---

🛠️ Tech Stack

Programming Language

- Python

Libraries Used

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

📂 Dataset Information

The dataset contains household electrical power consumption measurements collected over time.

Features Used

- Global_reactive_power
- Voltage
- Sub_metering_1
- Sub_metering_2
- Sub_metering_3
- Hour
- Day
- Month
- Weekday

Target

- Global_active_power

---

📊 Data Preprocessing

✔ Datetime Conversion

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

✔ Feature Extraction

df['hour'] = df['DateTime'].dt.hour
df['day'] = df['DateTime'].dt.day
df['month'] = df['DateTime'].dt.month
df['weekday'] = df['DateTime'].dt.weekday

✔ Removing Unnecessary Columns

df = df.drop(['Date', 'Time', 'DateTime'], axis=1)

---

🤖 Machine Learning Models

1️⃣ Linear Regression

Performance

- RMSE: "0.5216"
- R² Score: "0.7578"

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

---

2️⃣ Random Forest Regressor

Random Forest provided better prediction performance and feature importance analysis.

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=50)
rf.fit(X_train, y_train)

---

📈 Visualizations

✔ Feature Importance Graph

The model identifies the most important features affecting power consumption.

Top Important Features

- Sub_metering_3
- Sub_metering_1
- Sub_metering_2
- Hour

---

✔ Actual vs Predicted Comparison

Visual comparison between actual and predicted household power consumption values.

---

💾 Saving the Model

import joblib

joblib.dump(rf, 'random_forest_power_model.pkl')
joblib.dump(scaler, 'scaler.save')

---

📁 Project Structure

Household-Power-Consumption/
│
├── power.ipynb
├── random_forest_power_model.pkl
├── scaler.save
├── README.md

---

⚙️ Installation

Clone the Repository

git clone https://github.com/your-username/Household-Power-Consumption.git

Navigate to Folder

cd Household-Power-Consumption

Install Dependencies

pip install pandas numpy matplotlib scikit-learn joblib

---

▶️ Run the Project

Open Jupyter Notebook:

jupyter notebook

Then open:

power.ipynb

---

📌 Future Improvements

- Deploy using Flask or Streamlit
- Add Deep Learning models
- Real-time energy prediction
- Hyperparameter tuning
- Dashboard integration
- Time-series forecasting

---

📚 Learning Outcomes

Through this project, I learned:

- Data preprocessing techniques
- Feature engineering
- Regression algorithms
- Model evaluation metrics
- Data visualization
- Model serialization

---

👩‍💻 Author

Anushka Singh

B.Tech CSE (AI & Data Science)
Khwaja Moinuddin Chishti Language University (KMCLU)

Skills

Python • Machine Learning • Data Analysis • Pandas • Scikit-learn • Visualization

---

⭐ Support

If you like this project, give it a ⭐ on GitHub!
