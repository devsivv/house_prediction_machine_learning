# 🏠 Boston House Price Prediction using XGBoost

A Machine Learning web application that predicts Boston house prices based on housing, demographic, and economic factors using the **XGBoost Regressor** model.

## 🌱 My Machine Learning Journey
This project is my first end-to-end Machine Learning project.

Through this project, I learned:

Data preprocessing and feature selection
Exploratory Data Analysis (EDA)
Regression algorithms and model evaluation
Comparing multiple ML models
Hyperparameter tuning concepts
Model serialization and deployment
Building interactive web applications using Streamlit

I trained and evaluated multiple regression models, including Linear Regression, Random Forest Regressor, and XGBoost Regressor. After comparing their performance, I selected XGBoost as the final model due to its superior predictive accuracy.

This project marks the beginning of my Machine Learning journey, and I look forward to building more advanced projects involving Deep Learning, NLP, Computer Vision, and MLOps.

Every expert was once a beginner, and this project represents my first step into the world of Machine Learning. 🚀

## 🚀 Live Project

**GitHub Repository:**
https://github.com/devsivv/house_prediction_machine_learning

**Live Link:**
http://housepricepredictiondevsivv.streamlit.app/

---

## 📌 Project Overview

This project uses the Boston Housing Dataset to predict the median value of owner-occupied homes.

The workflow includes:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering Experiments
* Model Training
* Model Evaluation
* Streamlit Web Application Deployment

The final model was selected based on performance comparison across multiple regression algorithms.

---

## 📊 Models Compared

| Model                   |  R² Score |       MAE |      RMSE |
| ----------------------- | --------: | --------: | --------: |
| Linear Regression       |     0.779 |     3.113 |     4.301 |
| Random Forest Regressor |     0.879 |     2.222 |     3.177 |
| XGBoost Regressor       | **0.905** | **2.075** | **2.817** |

### 🏆 Best Model

**XGBoost Regressor**

* R² Score: **0.905**
* MAE: **2.075**
* RMSE: **2.817**

The XGBoost model achieved the highest prediction accuracy and was selected as the final production model.

---

## 📂 Features Used

* Crime Rate
* Residential Land Ratio
* Non Retail Business Ratio
* Near Charles River
* Nitric Oxide Concentration
* Average Rooms Per Dwelling
* Old Houses Ratio
* Distance To Employment Centers
* Highway Accessibility Index
* Property Tax Rate
* Pupil Teacher Ratio
* Black Population Index
* Lower Status Population Percentage

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost

### Data Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

---

## 📈 Evaluation Metrics

The following regression metrics were used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 🖥️ Running Locally

### Clone Repository

```bash
git clone https://github.com/devsivv/house_prediction_machine_learning.git
cd house_prediction_machine_learning
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📷 Application Features

* User-friendly Streamlit interface
* Real-time house price prediction
* XGBoost-powered predictions
* Interactive input fields
* Clean and responsive UI

---

## 📁 Project Structure

```text
house_prediction_machine_learning/
│
├── app.py
├── xgb_model.json
├── boston.csv
├── requirements.txt
├── House_Price_Prediction.ipynb
└── README.md
```

---

## 🎯 Future Improvements

* Hyperparameter tuning with GridSearchCV
* Cross-validation analysis
* SHAP Explainability
* Feature importance dashboard
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)

---

## 👨‍💻 Author

### Shivam Dubey

GitHub: https://github.com/devsivv

Passionate about Machine Learning, Data Science, and Full-Stack Development.

Feel free to connect, contribute, or provide feedback!

---
