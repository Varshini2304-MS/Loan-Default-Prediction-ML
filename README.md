
# Loan Default Prediction Using Machine Learning

## 1. Business Problem
Financial institutions face financial losses when customers fail to repay their credit obligations. This project uses machine learning to predict whether a customer is likely to default on their next payment.

## 2. Dataset
The project uses the UCI Default of Credit Card Clients dataset.

Dataset source:
UCI Machine Learning Repository

The dataset contains customer demographic information, credit limits, payment history, bill amounts, and previous payment amounts.

## 3. Data Preparation
The dataset was checked for:
- Missing values
- Duplicate records
- Categorical inconsistencies
- Target distribution

Education and marriage categories were cleaned before model development.

## 4. Machine Learning Models
The following classification models were developed and compared:
- Logistic Regression
- Decision Tree
- Random Forest

## 5. Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

Random Forest achieved the highest ROC-AUC of approximately 0.774 among the three tested models.

## 6. Final Model
Random Forest was selected as the final prediction model.

## 7. Business Recommendation
The model can support financial institutions in identifying customers with higher predicted default risk. High-risk customers can be subjected to additional credit-risk assessment, monitoring, or appropriate repayment support.

## 8. Streamlit Application
An interactive Streamlit application was developed where users can enter customer information and receive a predicted default-risk classification.

## 9. Project Files
- app.py – Streamlit application
- random_forest_loan_default_model.pkl – trained machine learning model
- requirements.txt – required Python libraries
- Loan_Default_Prediction.ipynb – analysis and model development notebook
## 10. How to Run the Project

### Install Libraries

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser at http://localhost:8501
