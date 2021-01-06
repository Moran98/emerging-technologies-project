# Emerging Technology Project

## Overview
The goal of this project is to produce a model that accurately predicts wind turbine power output from wind speed
values, as in the data set. A web service created using Flask responds with
predicted power values based on speed values sent as HTTP requests.

## Windows
```
set FLASK_APP=server.py
python -m flask run
```

## Linux
```
export FLASK_APP=server.py
python3 -m flask run
```

## Dockerfile
```
docker build . -t server-app
docker run --name rando-container -d -p 5000:5000 server-app
```

### Built With 
* Visual Studio Code
* Jupyter Notebook
* Docker

### Author
* [Aaron Moran - G00356519](https://github.com/Moran98)

### References
* [Ian McLoughlin's Github Repository - Keras Linear](https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/keras-linear.ipynb)
* [The Art of Routing in Flask](https://hackersandslackers.com/flask-routes/)
* [Tensorflow Basic Regression](https://www.tensorflow.org/tutorials/keras/regression)
* [Tensorflow Save and Load Models](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [Pickle loading anmd saving models](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/#:~:text=Saving%20Your%20Model-,Save%20Your%20Model%20with%20pickle,it%20to%20make%20new%20predictions.)
* [Flask - POST Method](https://stackoverflow.com/questions/34853033/flask-post-the-method-is-not-allowed-for-the-requested-url)