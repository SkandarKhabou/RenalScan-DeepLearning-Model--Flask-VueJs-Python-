import numpy as np
from keras.preprocessing import image as keras_image
from keras.applications.resnet import preprocess_input
from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from tensorflow.keras.models import load_model
from ultralytics import YOLO
import os

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['file']
    image = Image.open(image_file)

    model = YOLO("YoloBest.pt")

    # Convert the image to RGB format if not already
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Define function to crop image
    def crop_image(image, box):
        return image.crop(box)

    # Perform object detection on the image
    results = model(image)

    # Assuming results[0] is the detection result for the image
    result = results[0]

    # Check if there are at least two bounding boxes detected
    if len(result.boxes.xyxy) < 2:
        return jsonify(message="Not enough objects detected")

    # Extract bounding box coordinates and assign to variables
    table1 = result.boxes.xyxy[0].tolist()  # Convert the tensor to a list
    table2 = result.boxes.xyxy[1].tolist()  # Convert the tensor to a list

    # Crop images for table1 and table2
    table1_image = crop_image(image, table1)
    table2_image = crop_image(image, table2)

    resnet101_model = load_model('RESNET101.h5')

    # Define the directory to save the images
    save_dir = "images"

    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save table1_image and table2_image
    table1_image_path = os.path.join(save_dir, "table1_image.jpg")
    table2_image_path = os.path.join(save_dir, "table2_image.jpg")

    resize_shape = (48, 48)  # Adjust as needed
    table1_image = table1_image.resize(resize_shape)
    table2_image = table2_image.resize(resize_shape)

    table1_image.save(table1_image_path)
    table2_image.save(table2_image_path)

    # Load and preprocess the images
    img_array1 = preprocess_image(table1_image_path)
    img_array2 = preprocess_image(table2_image_path)

    # Make predictions
    predictions = resnet101_model.predict([img_array1, img_array2])

    # Interpret the predictions
    print("ozijefiozjeofijzeoifjoizejfiojezfiojzeiofjzeoif")
    print(predictions)
    predicted_class = np.argmax(predictions)
    class_labels = {
        0: "Cyst",
        1: "Stone",
        2: "Normal",
        3: "Tumor"
    }

    # Map the predicted class index to the corresponding class label
    predicted_class_label = class_labels[predicted_class]

    print("Predicted class label:", predicted_class_label)
    return jsonify(message=predicted_class_label)

def preprocess_image(image_path):
    # Load the image as a NumPy array
    img = Image.open(image_path).resize((48, 48))  # Adjust size as needed
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


if __name__ == '__main__':
    app.run(debug=True)
