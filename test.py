from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import load_model
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

model = load_model('my_model.h5')

def test(dir, cls):
    correct = 0
    all = 0
    for i in os.listdir(dir):
        all += 1
        img = image.load_img(dir + '//' + i, target_size=(200,200,3))
        X = image.img_to_array(img)
        X = np.expand_dims(X, axis=0)
        img = np.vstack([X])
        val = model.predict_classes(img)
        if val == cls:
            correct += 1
    print("accuracy: ", correct/all)
    return correct/all

test_dir_male = 'dataset/testing/male'
test_dir_female = 'dataset/testing/female'

ma = test(test_dir_male, 1)
fa = test(test_dir_female, 0)

print("model accuracy: ", (ma + fa) / 2)