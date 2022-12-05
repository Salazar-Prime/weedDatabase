import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices("GPU")
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)

model = tf.keras.models.load_model("models/dogs-vs-cats.h5")
# model = tf.keras.models.load_model(model_path)
# Convert the model
converter = tf.lite.TFLiteConverter.from_keras_model(
    model
)  # path to the SavedModel directory
# converter.optimizations = [tf.lite.Optimize.DEFAULT]
# converter.target_spec.supported_types = [tf.float16]
tflite_model = converter.convert()

# Save the model.
with open("models/model.tflite", "wb") as f:
    f.write(tflite_model)
