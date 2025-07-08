# from flask import Flask, request, jsonify
# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model

# app = Flask(__name__)
# model = load_model("waste_classifier.h5")  # Your trained model

# labels = ["dry", "wet", "paper"]

# @app.route('/classify', methods=['POST'])
# def classify():
#     file = request.data
#     npimg = np.frombuffer(file, np.uint8)
#     image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
#     image = cv2.resize(image, (224, 224)) / 255.0
#     image = np.expand_dims(image, axis=0)
    
#     prediction = model.predict(image)
#     class_index = np.argmax(prediction)
#     result = labels[class_index]
    
#     return result

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify
from PIL import Image
import io
import random

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' in request.files:
        image = Image.open(request.files['image'])
    else:
        image = Image.open(io.BytesIO(request.data))

    # Dummy classification logic
    categories = ['dry', 'wet', 'paper']
    result = random.choice(categories)

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

