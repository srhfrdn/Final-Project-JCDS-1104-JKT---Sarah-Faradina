from contextlib import nullcontext
from flask import Flask, render_template, request, send_from_directory
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/visual")
def visual():
    return render_template("visual.html")

@app.route("/author")
def about():
    return render_template("author.html")

@app.route('/data/<path:x>')
def data(x):
    return send_from_directory("data", x)

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        input = request.form
        
        

        df_to_predict = pd.DataFrame({
            'Gender': [input['Gender']],
            'Customer Type' : [input['Customer Type']],
            'Age': [input['Age']],
            'Type of Travel' : [input['Type of Travel']],
            'Class' : [input['Class']],
            'Seat comfort' : [input['Seat comfort']],
            'Departure/Arrival time convenient' : [input['Departure/Arrival time convenient']],
            'Food and drink' : [input['Food and drink']],
            'Gate location' : [input['Gate location']],
            'Inflight wifi service' : [input['Inflight wifi service']],
            'Inflight entertainment' : [input['Inflight entertainment']],
            'Online support' : [input['Online support']],
            'Ease of Online booking' : [input['Ease of Online booking']],
            'On-board service' : [input['On-board service']],
            'Leg room service' : [input['Leg room service']],
            'Baggage handling' : [input['Baggage handling']],
            'Checkin service' : [input['Checkin service']],
            'Cleanliness' : [input['Cleanliness']],
            'Online boarding' : [input['Online boarding']],
            'Departure Delay in Minutes' : [input['Departure Delay in Minutes']],
            'Arrival Delay in Minutes' : [input['Arrival Delay in Minutes']]

        }, index = [0])

        prediksi = model.predict(df_to_predict)

        if prediksi > 0.5:
            rslt = 'Neutral / Dissatisfied'
            mssg = 'Sorry, this passenger is not satisfied with the airline.'
        else:
            rslt = 'Satisfied'
            mssg = 'Congratulation! This passenger is satisfied with the airline.'
        

        return render_template(
            "prediction.html", data = input, result= rslt, message = mssg 
        )

    

if __name__ == "__main__":
    model = joblib.load("dtc_tuned")
    app.run(debug=True, port=8000)