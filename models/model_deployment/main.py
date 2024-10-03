from flask import Flask, request, jsonify

app = Flask('churn')

@app.route('/predict', methods=['POST']) # turn the function into web service, POST 
def predict():
    customer = request.get_json() # get it and turn it into python dictionary

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred <= 0.5

    result = {'churn_probability': y_pred,
              'churn': churn}
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 9696)