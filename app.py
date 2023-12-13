import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("MODELS/LogisticRegression.pkl", "rb"))

@flask_app.route("/",  methods = ["GET","POST"] )
def Home():
    return render_template("home.html")

@flask_app.route("/home",  methods = ["GET","POST"] )
def index():
    return render_template("index.html")

@flask_app.route("/home_page", methods=["GET", "POST"])
def other_page():
    if request.method == "POST":
        # Code to handle button click on other_page
        print("Button clicked on other_page")
        # Redirect to the index page after the button click
        return redirect(url_for("index"))
    else:
        return render_template("home.html")
    
@flask_app.route("/predict", methods = ["GET","POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    print(features)
    print(prediction)

    if(prediction==1):
        return render_template("index.html", prediction_text = "Result Positive")
    else:
        return render_template("index.html", prediction_text = "Result Negative ")
        
        
    

if __name__ == "__main__":
    flask_app.run(debug=True)