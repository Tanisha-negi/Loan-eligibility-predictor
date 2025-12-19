---
title: Loan Eligibility Predictor
emoji: 📈
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
---

# 🏦 Loan Eligibility Prediction Model

This project implements a machine learning solution to automate the loan approval process by predicting the eligibility status of an applicant. The objective is to build a reliable classification model that minimizes risk for financial institutions and speeds up the decision-making process.

## 🎯 Key Features & Methodology

* **Classification Models:** Trained and compared performance of fundamental classification algorithms (Decision Tree, Naive Bayes).
* **Feature Engineering:** Created derived features (e.g., Total Income, Log Transformation) to improve model linearity and accuracy.
* **Data Preprocessing Pipeline:** Handled missing values (Imputation) and converted categorical data (Encoding) for the entire dataset.
* **Web Integration:** Deployed the final model using the Flask framework for live prediction via a web form. 

## 🧰 Tech Stack & Libraries

| Category | Tool / Library | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Core development language |
| **Web Framework** | Flask | Building the prediction API and serving the web interface |
| **Data Handling** | `pandas`, `NumPy` | Data manipulation and numerical operations |
| **Modeling** | `scikit-learn`, `joblib` | Training, evaluating, and model serialization/loading |
| **Visualization** | `matplotlib`, `seaborn` | Exploratory Data Analysis (EDA) and results plotting |

## 📊 Performance Results

| Model | Accuracy Score | Key Metric (F1/Precision) |
| :--- | :--- | :--- |
| **Decision Tree** | **[Insert DT Accuracy]**% | **[Insert DT Precision]** |
| **Naive Bayes (Final)** | **[Insert NB Accuracy]%** | **[Insert NB Precision]** |


## 📁 Project Structure
loan_eligibility_prediction/ ├── data/ │ ├── train.csv # Original training dataset │ └── test.csv # Original testing dataset ├── model.pkl # Final trained prediction model (Serialized object) ├── app.py # Flask application code for web deployment ├── loan_eligibility_prediction.ipynb # Comprehensive data cleaning, EDA, and model training notebook ├── templates/ # HTML templates for the web interface (index.html, result.html) ├── README.md # This file └── requirements.txt # Required Python packages

## 🚀 How to Run Locally

Follow these steps to set up the environment and run the web application:

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL]
    cd loan_eligibility_prediction
    ```

2.  **Set Up Environment:** Create and activate a Python virtual environment, then install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Ensure Model is Present:** Confirm that your trained `model.pkl` file is in the root directory.

4.  **Run the Flask Application:**
    ```bash
    python app.py
    ```
    The application will start, typically accessible at `http://127.0.0.1:5000/`.

## 💡 Future Scope & Deployment

* **Hyperparameter Tuning:** Use GridSearchCV or RandomizedSearchCV to further optimize the chosen model's parameters.
* **Advanced Features:** Integrate derived features like Debt-to-Income Ratio.
* **Cloud Deployment:** Deploy the Flask application to services like Heroku or AWS Elastic Beanstalk.

## 📄 License

This project is licensed under the **MIT License**.