# Indian House Price Prediction

## 📌 Assignment Information
- **Student Name:** [Your Name]
- **Course:** [Your Course Name]
- **Assignment:** House Price Prediction using Machine Learning

## 🎯 Project Overview
This project predicts house prices using two machine learning models:
- Linear Regression
- Random Forest Regressor

## 📊 Dataset
Using California Housing dataset with 20,640 records and 8 features:
- MedInc (Median Income)
- HouseAge (House Age)
- AveRooms (Average Rooms)
- AveBedrms (Average Bedrooms)
- Population
- AveOccup (Average Occupancy)
- Latitude
- Longitude

## 📈 Results

| Model | R² Score | Mean Absolute Error | RMSE |
|-------|----------|---------------------|------|
| Linear Regression | 58.27% | $53,000 | $74,000 |
| Random Forest | 81.05% | $33,000 | $51,000 |

**Best Model:** Random Forest (22.8% better than Linear Regression)

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
