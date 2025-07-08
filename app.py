from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)
model = tf.keras.models.load_model("waste_classifier.keras")  # Load trained model

UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists

# Class labels (update based on your dataset)
class_names = ["Dry", "Paper", "Wet"]

# Mapping classes to binary codes
class_to_binary = {
    "Dry": "01",
    "Wet": "10",
    "Paper": "11"
}

def predict_image(image_path):
    """Preprocess image and make a prediction"""
    img = load_img(image_path, target_size=(224, 224))  # Resize image
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]  # Get class with highest probability
    binary_code = class_to_binary.get(predicted_class, "00")  # Default to "00" if unknown
    return predicted_class, binary_code

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400
        
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)  # Save the uploaded file

        predicted_class, binary_code = predict_image(file_path)  # Make prediction
        
        return render_template("indexs.html", filename=file.filename, prediction=predicted_class,binary_code= binary_code)

        # return jsonify({
        #     "filename": file.filename,
        #     "prediction": predicted_class,
        #     "binary_code": binary_code
        # })

    return render_template("indexs.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")





# from flask import Flask, request, jsonify
# import tensorflow as tf
# from tensorflow.keras.utils import load_img, img_to_array
# import numpy as np
# import os

# app = Flask(__name__)
# model = tf.keras.models.load_model("waste_classifier.h5")  # Load trained model

# UPLOAD_FOLDER = "static/uploads/"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# # Class labels
# class_names = ["Dry", "Paper", "Wet"]
# class_to_binary = {"Dry": "01", "Wet": "10", "Paper": "11"}

# def predict_image(image_path):
#     """Preprocess image and make a prediction"""
#     img = load_img(image_path, target_size=(224, 224))  # Resize image
#     img_array = img_to_array(img) / 255.0  # Normalize
#     img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#     predictions = model.predict(img_array)
#     predicted_class = class_names[np.argmax(predictions)]
#     binary_code = class_to_binary.get(predicted_class, "00")
#     return predicted_class, binary_code

# @app.route("/upload", methods=["POST"])
# def upload_file():
#     if "file" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400
    
#     file = request.files["file"]
#     file_path = os.path.join(app.config["UPLOAD_FOLDER"], "captured.jpg")
#     file.save(file_path)  # Save the image

#     predicted_class, binary_code = predict_image(file_path)  # Predict class
    
#     return jsonify({
#         "prediction": predicted_class,
#         "binary_code": binary_code
#     })

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)












