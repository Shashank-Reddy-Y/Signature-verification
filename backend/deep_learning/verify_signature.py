import numpy as np
import os
from flask import Flask, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
import cv2
import base64
from pymongo import MongoClient
import urllib.parse
from dotenv import load_dotenv
import tflite_runtime.interpreter as tflite

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable not set")

mongo_client = MongoClient(MONGO_URI)

# Safely extract the default database from the URI, or fallback to 'test' (Mongoose default)
try:
    default_db = mongo_client.get_default_database().name
except:
    default_db = "test"

db_name = os.getenv("MONGO_DB_NAME", default_db)
db = mongo_client[db_name]
collection = db.accounts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "feature_extractor.tflite")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Missing model file: {MODEL_PATH}. Please upload the .tflite file.")

interpreter = tflite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/health')
def health():
    return jsonify({"status": "running"})

def retrieve_signature_bytes(account_number):
    record = collection.find_one({"accountNumber": str(account_number)})
    
    if record and "image" in record:
        signature_data = record["image"]
        if isinstance(signature_data, str): 
            # Cleanly split off the base64 prefix if the frontend sent it
            if "," in signature_data:
                signature_data = signature_data.split(",")[1]
            signature_data = base64.b64decode(signature_data)
            
        return signature_data
    else:
        raise ValueError("Signature not found in the database.")

def preprocess_image_from_memory(image_bytes):
    img_array = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR) 
    img = cv2.resize(img, (224, 224))
    
    img_array = img.astype(np.float32)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

def extract_features(img_array):
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    return interpreter.get_tensor(output_details[0]['index']).flatten()

@app.route('/api/signature/verify', methods=['POST'])
def verify_signature():
    try:
        if 'account_number' not in request.form or 'verifying_signature' not in request.files:
            return jsonify({"error": "Missing required fields"}), 400

        account_number = request.form['account_number']
        verifying_signature_file = request.files['verifying_signature']

        stored_signature_bytes = retrieve_signature_bytes(account_number)
        verifying_signature_bytes = verifying_signature_file.read()

        stored_image = preprocess_image_from_memory(stored_signature_bytes)
        verifying_image = preprocess_image_from_memory(verifying_signature_bytes)

        stored_embedding = extract_features(stored_image)
        verifying_embedding = extract_features(verifying_image)

        similarity = cosine_similarity([stored_embedding], [verifying_embedding])[0][0]

        threshold = 0.8
        result = "Genuine" if similarity > threshold else "Forged"

        return jsonify({"similarity": float(similarity), "result": result})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 5001))
    app.run(host="0.0.0.0", port=PORT)
