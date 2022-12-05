import streamlit as st
import tensorflow as tf
# import cv2

# from tensorflow.keras import layers
# from tensorflow.keras import models, utils
import pandas as pd

# from tf.keras.models import load_model
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras import utils
import PIL
from PIL import Image, ImageDraw
import numpy as np

model_path = "models/dogs-vs-cats.tflite"

gpus = tf.config.experimental.list_physical_devices("GPU")
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)


def getInference(uploaded_file):
    # text over upload button "Upload Image"
    if uploaded_file is not None:

        # read and resize the image
        img = Image.open(uploaded_file)
        img = img.resize((150, 150), Image.ANTIALIAS)
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.expand_dims(img, axis=0).astype(np.float32)
        img /= 255.0

        # tflite model loading
        interpreter = tf.lite.Interpreter(model_path=str(model_path))
        interpreter.allocate_tensors()
        input_index = interpreter.get_input_details()[0]["index"]
        output_index = interpreter.get_output_details()[0]["index"]
        interpreter.set_tensor(input_index, img)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_index)

        print("PREDICTION-------", prediction)

        if prediction[0][0] < 0.5:
            predictionFunny = "That's you Feline Friend!"
            predClass = "cat"
            classNo = 0
            conf = -1 * (2 * prediction[0][0] - 1)  # mapping for confidence
        else:
            predictionFunny = "Woof! That's a Dog!"
            predClass = "dog"
            classNo = 1
            conf = (2 * prediction[0][0]) - 1  # mapping for confidence

        return [predictionFunny, predClass, classNo, round(conf * 100, 2)]
