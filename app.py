from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

# Load your trained machine learning model
model = pickle.load(open("model.pkl", "rb"))

# Initialize StandardScaler
scaler = StandardScaler()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get form data
        gender = int(request.form["gender"])
        print(gender)
        married = int(request.form["married"])
        print(married)
        dependents = int(request.form["dependents"])
        print(dependents)
        education = int(request.form["education"])
        print(education)
        self_employed = int(request.form["selfEmployed"])
        print(self_employed)
        applicant_income = int(request.form["applicantIncome"])
        print(applicant_income)
        coapplicant_income = int(request.form["coapplicantIncome"])
        print(coapplicant_income)
        loan_amount = int(request.form["loanAmount"])
        print(loan_amount)
        term = int(request.form["term"])
        print(term)
        credit_history = int(request.form["creditHistory"])
        print(credit_history)
        area = int(request.form["area"])
        print(area)

        # Create DataFrame from form data
        input_data = pd.DataFrame({
            "Gender": [gender],
            "Married": [married],
            "Dependents": [dependents],
            "Education": [education],
            "Self_Employed": [self_employed],
            "ApplicantIncome": [applicant_income],
            "CoapplicantIncome": [coapplicant_income],
            "LoanAmount": [loan_amount],
            "Loan_Amount_Term": [term],
            "Credit_History": [credit_history],
            "Property_Area": [area]
        })

        # Make prediction
        prediction = model.predict(input_data)
        print(prediction)

        # Interpret prediction
        result = "Your loan is approved" if prediction[0] == 'Y' else "Your loan is not approved"

        # Redirect to the result page and pass the prediction as a query parameter
        return redirect(url_for('show_result', prediction=result))
        # return jsonify(result)

@app.route("/result")
def show_result():
    prediction = request.args.get('prediction', 'Prediction not available')
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)