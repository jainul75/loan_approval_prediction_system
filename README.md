Loan Approval Prediction System

This repository contains a machine learning model for predicting loan approval and the necessary code to deploy it.

Overview
The loan approval prediction system is built using machine learning algorithms to automate the process of approving or rejecting loan applications. The model takes various features related to the applicant's financial history, credit score, employment status, and other relevant factors, and predicts whether the loan application should be approved or denied.

Model Development
The machine learning model is developed using Python programming language and popular libraries such as scikit-learn, pandas, and numpy. The model is trained on a labeled dataset containing historical loan application data, where each entry includes features of the applicant and the corresponding loan approval decision.

Several machine learning algorithms (SVM, Random Forest, Gradient Boosting, XGBoost) are explored and evaluated to identify the most suitable one for the task. The model is then evaluated using performance metrics such as accuracy, precision, recall, and F1-score. And then the Random Forest model is tested using unlabeled dataset.

Deployment
The model is deployed using Flask, a lightweight WSGI web application framework in Python. Flask provides a simple and flexible way to create web APIs, making it suitable for deploying machine learning models as web services.

Create a HTML form for users inputs. The data then sent to the backend(Flask) and the RF model make prediction based on thoese data.
