import json
import numpy as np
import pandas as pd
# import tensorflow as tf
from flask import Flask
# from flask import request
# from flask import jsonify

app = Flask(__name__)

# from tensorflow import keras
# model = keras.models.load_model("saved_model/my_model")

@app.route('/')
def test_get():
    return 'api working!'

@app.route('/predict', methods=['POST', 'GET'])
def test_post():
    if request.method == 'POST':
        pred_dicts = request.get_json()
        df = dict(pd.DataFrame(pred_dicts))
        print(df)

        # pred_ds1 = tf.data.Dataset.from_tensor_slices(df)
        # pred_ds1 = pred_ds1.batch(32)

        # model_predicts = model.predict(pred_ds1)

        # predicts = [np.argmax(predict_item).item() for predict_item in model_predicts]

    return jsonify(data={'predictions': 10})