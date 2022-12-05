import streamlit as st
import tensorflow as tf

# from tensorflow.keras import layers
# from tensorflow.keras import models, utils
import pandas as pd

# from tf.keras.models import load_model
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras import utils
import PIL
from PIL import Image, ImageDraw
import numpy as np

model_path = "models/dogs-vs-cats.h5"


def getInference(uploaded_file):
    # text over upload button "Upload Image"
    if uploaded_file is not None:
        model = tf.keras.models.load_model(model_path)
        display_image = PIL.Image.open(uploaded_file)  # type: ignore

        # # Resize the image for tensorflow predicition
        display_image = display_image.resize((150, 150), Image.ANTIALIAS)
        img_tensor = tf.keras.preprocessing.image.img_to_array(display_image)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.0
        prediction = model.predict(img_tensor)

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
