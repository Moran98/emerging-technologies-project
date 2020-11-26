# flask for web app.
import flask as fl
from flask import Flask, render_template

# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route('/')
def index():
    return render_template('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}
