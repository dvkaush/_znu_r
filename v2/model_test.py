import datetime

import random
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.backend import argmax

from sklearn.model_selection import train_test_split


def create_input():
  __dict = {};
  __dict['age'] = random.randint(10, 40)
  __dict['gender'] = np.random.choice(['Male', 'Female'], 1, [0.55, 0.45])[0]
  __dict['emotion'] = np.random.choice(
      ['Happy', 'Sad', 'Fear', 'Disgust', 'Anger', 'Surprice'], 1, 
      [0.23, 0.18, 0.13, 0.1, 0.19, 0.17])[0]
  __dict['color'] = random.choice(['Red', 'Blue', 'Green', 'White', 'Gray'])
  __dict['animal'] = random.choice(['Tiger', 'Fish', 'Dog', 'Eagal', 'Horse'])
  __dict['q3'] = random.choice(['N1', 'N2', 'N3', 'N4', 'N5'])
  __dict['q4'] = random.choice(['M1', 'M2', 'M3', 'M4', 'M5'])
  return __dict


new_model = tf.keras.models.load_model('saved_model/my_model')

new_model.build(input_shape={})

new_model.summary()

dict1 = {
  'age': 25,
  'gender': 'Male',
  'emotion': 'Happy',
  'color': 'Blue',
  'animal': 'Horse',
  'q3': 'N1',
  'q4': 'M1'
}

dict2 = {
  'age': 26,
  'gender': 'Female',
  'emotion': 'Surprice',
  'color': 'Red',
  'animal': 'Fish',
  'q3': 'N1',
  'q4': 'M1'
}

pred_dicts = [dict1, dict2]
# for pi in range(10):
#   pred_dicts.append(create_input())

pred_ds1 = tf.data.Dataset.from_tensor_slices(dict(pd.DataFrame(pred_dicts)))
pred_ds1 = pred_ds1.batch(32)

predicts = new_model.predict(pred_ds1)

for index, predict in enumerate(predicts):
  print(pred_dicts[index], np.argmax(predict))