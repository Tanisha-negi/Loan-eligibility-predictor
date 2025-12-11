from flask import Flask, render_template, request, url_for, redirect
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
MODEL_FILE = 'model.pkl' 

try:
    model = joblib.load(MODEL_FILE)
    print(f"Model {MODEL_FILE} loaded successfully.")
except Exception as e:
    print(f"ERROR: Failed to load model {MODEL_FILE}. Ensure it is in the root directory: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('error.html', error="Model not loaded. Cannot predict.")
    
    try:
        data = request.form.to_dict()

        gender = int(data.get('gender', '0'))
        married = int(data.get('married', '0'))
        education = int(data.get('education', '0'))
        self_employed = int(data.get('self_employed', '0'))
        credit_history = float(data.get('credit_history', '0'))
        
        applicant_income = float(data.get('applicant_income', '0'))
        coapplicant_income = 0.0 
        loan_amount = float(data.get('loan_amount', '0'))
        loan_amount_term = float(data.get('loan_amount_term', '0'))

        total_income = applicant_income + coapplicant_income

        total_income_log = np.log(total_income + 1) if total_income > 0 else 0
        loan_amount_log = np.log(loan_amount + 1) if loan_amount > 0 else 0

        dependents = 0 
        property_area = 2 
        
        # input_data = {
        #     'Gender': [gender],
        #     'Married': [married],
        #     'Dependents': [dependents],        
        #     'Education': [education],
        #     'Self_Employed': [self_employed],
        #     'Loan_Amount_Term': [loan_amount_term],
        #     'Credit_History': [credit_history],
        #     'Property_Area': [property_area]   
            
        # }
        
        input_data_8_features = {
            'Gender': [gender],
            'Married': [married],
            'Education': [education],
            'Self_Employed': [self_employed],
            'Credit_History': [credit_history],
            'Loan_Amount_Term': [loan_amount_term],
            'Total_Income_Log': [total_income_log], 
            'LoanAmount_Log': [loan_amount_log]    
        }

        input_df = pd.DataFrame(input_data_8_features)

        prediction = model.predict(input_df)[0]
        
        if prediction == 1:
            result = "Eligible"
        else:
            result = "Not Eligible"

        return render_template('result.html', prediction=result)

    except ValueError:
        return render_template('error.html', error="Invalid input. Please ensure all number fields are filled correctly.")
        
    except Exception as e:
        return render_template('error.html', error=f"An unexpected error occurred during prediction: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)