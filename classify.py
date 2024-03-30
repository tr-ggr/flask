import tensorflow as tf
import numpy as np

# Load the pre-trained TensorFlow model
model = tf.keras.models.load_model('my_model.h5')

# Define the classes
classes = ['Biodegradable', 'Not Biodegradable']


def predict(image):
    img = tf.keras.utils.load_img(
        image, target_size=(180, 180)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return classes[np.argmax(score)]

def check(image):
    # # Initialize the webcam
    # cap = cv2.VideoCapture(0)

    # # Capture a single frame
    # ret, frame = cap.read()

    # # Release the webcam
    # cap.release()

    # # Preprocess the frame
    # processed_frame = preprocess_image(frame)

    # # Make prediction
    # predictions = model.predict(processed_frame)
    # image = "WIN_20240320_20_33_36_Pro.jpg"

    # Get the predicted class
    predicted_class = predict(image)

    # Display the prediction
    return f"Prediction: {predicted_class}"

# if __name__ == "__main__":
#     check(image)