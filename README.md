<!-- HERO SECTION START -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C9FF,50:92FE9D,100:6A11CB&height=250&section=header&text=⚡%20Household%20Power%20Prediction&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Machine%20Learning%20Project%20using%20Python%20%7C%20Scikit-Learn%20%7C%20Random%20Forest&descAlignY=60&descSize=18"/>

<br>

<h1 style="
font-size:55px;
font-weight:900;
background: linear-gradient(90deg,#00C9FF,#92FE9D,#6A11CB);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
font-family:Segoe UI, sans-serif;
margin-top:20px;
">
</h1>

<p style="
font-size:20px;
color:#555;
max-width:850px;
line-height:1.8;
font-family:Segoe UI, sans-serif;
">
An industry-level <b>Machine Learning Project</b> that predicts household electricity consumption using
<b>Python, Pandas, NumPy, Scikit-learn, and Random Forest Regression</b>.
Built with complete ML workflow including preprocessing, visualization, training, evaluation, and model saving.
</p>

<br>

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Open%20Source-Yes-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Data%20Science-Project-red?style=for-the-badge">

<br>
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=28&duration=3000&color=00C9FF&center=true&vCenter=true&width=700&lines=Machine+Learning+Project;Power+Consumption+Prediction;Random+Forest+Regression;Data+Science+%7C+AI+%7C+Analytics"/>

</div>

<!-- HERO SECTION END -->

---

# 🌟 Project Overview

This project analyzes household electricity consumption data and predicts:

## 🎯 Target Variable
- **Global Active Power Consumption**

The workflow includes:

✔ Data Cleaning  
✔ Feature Engineering  
✔ Datetime Processing  
✔ Feature Scaling  
✔ Model Training  
✔ Performance Evaluation  
✔ Visualization  
✔ Model Saving  

---

# 🚀 Features

<table align="center">
<tr>
<td>✅ Data Preprocessing</td>
<td>✅ Feature Engineering</td>
</tr>

<tr>
<td>✅ Linear Regression</td>
<td>✅ Random Forest Regressor</td>
</tr>

<tr>
<td>✅ RMSE & R² Evaluation</td>
<td>✅ Visualization</td>
</tr>

<tr>
<td>✅ Feature Importance Analysis</td>
<td>✅ Model Serialization</td>
</tr>
</table>

---

# 🛠️ Tech Stack

<div align="center">

| Technology | Usage |
|---|---|
| Python | Core Programming |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| Joblib | Model Saving |

</div>

---

# 📂 Dataset Information

The dataset contains household electrical power consumption measurements collected over time.

## 📌 Features Used

```python
[
 'Global_reactive_power',
 'Voltage',
 'Sub_metering_1',
 'Sub_metering_2',
 'Sub_metering_3',
 'hour',
 'day',
 'month',
 'weekday'
]
```

## 🎯 Target

```python
Global_active_power
```

---

# 📊 Data Preprocessing

## ✔ Datetime Conversion

```python
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
```

---

## ✔ Feature Extraction

```python
df['hour'] = df['DateTime'].dt.hour
df['day'] = df['DateTime'].dt.day
df['month'] = df['DateTime'].dt.month
df['weekday'] = df['DateTime'].dt.weekday
```

---

## ✔ Removing Unnecessary Columns

```python
df = df.drop(['Date', 'Time', 'DateTime'], axis=1)
```

---

# 🤖 Machine Learning Models

<div align="center">

| Model | Purpose |
|---|---|
| Linear Regression | Baseline Model |
| Random Forest Regressor | Advanced Prediction |

</div>

---

# 📈 Model Performance

## 🔹 Linear Regression

```python
RMSE : 0.5216
R² Score : 0.7578
```

---

# 🌲 Random Forest Regressor

```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=50)
rf.fit(X_train, y_train)
```

---

# 📉 Visualizations

## ✔ Feature Importance Analysis

Top Important Features:

- Sub_metering_3
- Sub_metering_1
- Sub_metering_2
- Hour

---

## ✔ Actual vs Predicted Comparison

The graph compares:
- Actual household power consumption
- Predicted power consumption

to evaluate model accuracy.

---

# 💾 Model Saving

```python
import joblib

joblib.dump(rf, 'random_forest_power_model.pkl')
joblib.dump(scaler, 'scaler.save')
```

---

# 📁 Project Structure

```bash
Household-Power-Consumption/
│
├── power.ipynb
├── random_forest_power_model.pkl
├── scaler.save
├── README.md
```

---

# ⚙️ Installation

## 📥 Clone Repository

```bash
git clone https://github.com/your-username/Household-Power-Consumption.git
```

---

## 📂 Move to Folder

```bash
cd Household-Power-Consumption
```

---

## 📦 Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

---

# ▶️ Run the Project

```bash
jupyter notebook
```

Then open:

```bash
power.ipynb
```

---

# 📌 Future Improvements

✨ Streamlit Deployment  
✨ Flask API Integration  
✨ Deep Learning Models  
✨ Real-Time Prediction  
✨ Dashboard Analytics  
✨ Time-Series Forecasting  

---

# 📚 Learning Outcomes

This project helped in understanding:

- Data preprocessing
- Feature engineering
- Regression models
- Performance metrics
- Data visualization
- End-to-end ML workflow

---

# 👩‍💻 Author

<div align="center">

## Anushka Singh

🎓 B.Tech CSE (AI & Data Science)  
🏫 Khwaja Moinuddin Chishti Language University (KMCLU)

### 💻 Skills

Python • Machine Learning • Data Analysis • Pandas • Scikit-learn • Visualization

</div>

---

<div align="center">

# ⭐ If you like this project, give it a star on GitHub ⭐

</div>
