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

@app.route('/')
def root():
    return render_template("index.html")


@app.route('/keras', methods=["GET","POST"])
def keras():
  if request.method == "POST":
    # Process input from user and cast to a float
    speed = [float(request.form["speed"])]
    
    # Loading in the model to test accuracy
    model = tf.keras.models.load_model('models/model')
    
    # Predict using model 1
    model_prediction = model.predict(speed)

    return render_template("keras.html", output=model_prediction[0])
  return render_template("keras.html")

@app.route('/tree', methods=["GET","POST"])
def tree():
  if request.method == "POST":
    # Process input from user and cast to a float
    speed2 = [float(request.form["speed"])]
    
    # Loading in the model to test accuracy
    model2 = pickle.load(open('models/model2.sav', 'rb'))
    
    # Predict using model 2
    model_prediction2 = model2.predict(speed2)

    return render_template("tree.html", output2=model_prediction2[0])
  return render_template("tree.html")

if __name__ == 'main':
  app.debug = True
  app.run(port=5000, debug=True)
