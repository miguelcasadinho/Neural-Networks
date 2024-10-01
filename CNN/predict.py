import numpy as np
# Importing the libraries
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logging (errors only)
import tensorflow as tf # type: ignore
from keras.preprocessing import image  # type: ignore

# Load the trained model
model = tf.keras.models.load_model('trained_model.h5')


# Load a new image to classify
new_image_path = '../Convolutional Neural Networks (CNN)/dataset/single_prediction/cat_or_dog_2.jpg'  # Replace with the path to your new image
test_image = image.load_img(new_image_path, target_size=(64, 64))  # Ensure the size matches what the model expects
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)  # Add batch dimension

# Make a prediction
result = model.predict(test_image/255.0)

# Mapping the result to the class
if result[0][0] > 0.5:
    prediction = 'dog'
else:
    prediction = 'cat'

# Output the result
print(f'The image is classified as: {prediction}')

