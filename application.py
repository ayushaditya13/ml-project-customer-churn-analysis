import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.sav", "rb"))

@app.route("/")
def loadPage():
    return render_template('home.html', output1="", output2="", query1="", query2="", query3="", query4="", query5="", query6="")

@app.route("/", methods=['POST'])
def predict():
    # Extract input data from the form
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']

    # Create a DataFrame for prediction data
    data = {
        'Age': [inputQuery1],
        'Gender': [inputQuery2],
        'Location': [inputQuery3],
        'Subscription_Length_Months': [inputQuery4],
        'Monthly_Bill': [inputQuery5],
        'Total_Usage_GB': [inputQuery6]
    }

    input_data = pd.DataFrame(data)

    # Preprocess the input data to match the training data
    input_data['tenure_group'] = pd.cut(input_data['Subscription_Length_Months'].astype(int), range(1, 31, 6), right=False, labels=False)
    input_data['age_group'] = pd.cut(input_data['Age'].astype(int), bins=[18, 46, 70], right=False, labels=False)
    input_data.drop(columns=['Age', 'Subscription_Length_Months'], axis=1, inplace=True)
    
    # One-hot encode the categorical features
    input_data = pd.get_dummies(input_data, columns=['Gender', 'Location', 'tenure_group', 'age_group'])

    # Make predictions
    single = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]

    # Prepare the output messages
    if single == 1:
        output1 = "This customer is likely to be churned!!"
    else:
        output1 = "This customer is likely to continue!!"
    
    output2 = "Confidence: {:.2f}%".format(probability * 100)

    return render_template('home.html', output1=output1, output2=output2,
                           query1=inputQuery1, query2=inputQuery2,
                           query3=inputQuery3, query4=inputQuery4,
                           query5=inputQuery5, query6=inputQuery6)

if __name__ == '__main__':
    app.run(debug=True)
