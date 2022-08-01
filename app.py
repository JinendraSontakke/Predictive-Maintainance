from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model_2.pkl','rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_features = [float(x) for x in request.form.values()]
        features_value = [np.array(input_features)]

        #features_name = ['Cycle', 'OpSet1', 'OpSet2', 'OpSet3', 'SM1', 'SM2', 'SM3', 'SM4',
        #  'SM5', 'SM6', 'SM7', 'SM8', 'SM9', 'SM10', 'SM11', 'SM12', 'SM13',
        #  'SM14', 'SM15', 'SrM16', 'SM17', 'SM18', 'SM19', 'SM20', 'SM21']

        features_name = ['Cycle', 'SM2', 'SM3', 'SM4', 'SM7', 'SM8', 'SM11', 'SM12', 'SM13',
       'SM15', 'SM17', 'SM20', 'SM21']

        df = pd.DataFrame(features_value,columns=features_name)
        output = model.predict(df)

        if output[0] == 0:
            res_val = "Condition is Good"
        elif output[0] == 1:
            res_val = "Condition is Moderate"
        elif output[0] == 2:
            res_val = "is in a warning stage."
        else:
            res_val = "Error"
            
    except Exception as e:
        print("the exception messeage : ", e)
        return "Something went wrong"



    #return render_template('index.html', prediction_text='Engine  {}'.format(res_val))
    return render_template('predict.html',prediction_text='Engine  {}'.format(res_val))


if __name__ == "__main__":
    app.run()