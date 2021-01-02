# Emerging Technology Project - G00356519

# Windows
```
set FLASK_APP=server.py
python -m flask run
```

```
docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image
```

# Linux
```
export FLASK_APP=server.py
python3 -m flask run
```

### References
* [Ian McLoughlin's Github Repository - Keras Linear](https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/keras-linear.ipynb)
* [Tensorflow Basic Regression](https://www.tensorflow.org/tutorials/keras/regression)
* [Tensorflow Save and Load Models](https://www.tensorflow.org/tutorials/keras/save_and_load)