from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model_file = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model_file.predict(features)
    return render_template("index.html", prediction_text = "The risk level is {}".format(prediction))


if __name__ == "__main__":
    app.run(debug = True)
