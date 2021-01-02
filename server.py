# Flask imports
import flask as fl
from flask import Flask, render_template, request
# Tensorflow to load in the models
import tensorflow as tf
# Numpy for numerical work
import numpy as np
import pickle

# Create a new web app.
app = fl.Flask(__name__)

@app.route('/', methods=["GET","POST"])
def predict():
  if request.method == "POST":
    # Process input from user and cast to a float
    speed = request.form["speed"]
    speed=[float(speed)]
    
    # Loading in the two models to compare accuracy
    model = tf.keras.models.load_model('models/model')
    model2 = pickle.load(open('models/model2.sav', 'rb'))
    
    # Predict using model 1 and model 2 - only model 1 working
    model_prediction = model.predict(speed)
    # model_prediction2 = model2.predict(speed)
    return render_template("index.html", output=model_prediction[0])
  return render_template("index.html")

if __name__ == 'main':
  app.run(port=5000, debug=True)
