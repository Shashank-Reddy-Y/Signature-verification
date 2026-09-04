# [🖋️ Signare](https://signature-verification-one.vercel.app/): AI-Powered Bank Signature Verification System

![React](https://img.shields.io/badge/Frontend-React-blue)
![Node.js](https://img.shields.io/badge/Backend-Node.js-green)
![Python](https://img.shields.io/badge/ML_API-Python-yellow)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen)

**Signare** is a production-ready, three-tier microservice web application designed to automate and secure the process of signature verification using Deep Learning.

---

## 🛑 The Problem Statement
In the banking and financial sector, manual signature verification is a critical but deeply flawed process. It is time-consuming, highly subjective, and prone to human error. Human tellers often struggle to detect sophisticated forgeries, leading to millions of dollars in financial fraud, identity theft, and operational bottlenecks. 

## 💡 What It Does (The Solution)
Signare eliminates human error by utilizing a **Customized CNN model** (optimized via TensorFlow Lite) to verify signatures mathematically. 

1. **Enrollment:** Bank administrators create customer accounts and upload a trusted "reference" signature to a secure MongoDB database.
2. **Verification:** When a transaction occurs, the teller uploads the physical signature presented on the check/document.
3. **AI Analysis:** The system instantly retrieves the customer's reference signature, extracts deep visual features from both images, and calculates their cosine similarity.
4. **Decision:** If the mathematical similarity exceeds the strict threshold (80%), the signature is stamped as **Genuine**. Otherwise, it is flagged as **Forged**.

---

## 🏛️ System Architecture & Data Flow

Signare is built on a modern **Microservice Architecture**, splitting the application into three decoupled environments to ensure high performance and scalability.

### 1. The Frontend (React.js)
The user-facing portal. It handles the UI for logging in, creating accounts, and the main verification dashboard. It is responsible for capturing the user's uploaded images and routing API requests to the appropriate backend. 
* *Deployed on Vercel.*

### 2. The Auth & Database API (Node.js / Express)
The central nervous system. This server handles secure user authentication, password hashing, and all CRUD (Create, Read, Update, Delete) operations. When an administrator uploads a reference signature, this server converts it into a Base64 string and securely stores it in **MongoDB Atlas**.
* *Deployed on Render.*

### 3. The Machine Learning API (Python / Flask)
A specialized, lightweight microservice dedicated entirely to heavy mathematical computation. 
* **The Flow:** It receives a verification request, connects directly to MongoDB to pull the original reference signature, and cleans both images (resizing, normalizing, and stripping Base64 HTML tags).
* **The Model:** It passes both images through a highly optimized `feature_extractor.tflite` model (only 749KB) to generate feature embeddings.
* **The Math:** It computes the Cosine Similarity between the two embeddings and returns the final score to the frontend.
* *Deployed on Render.*

---


## 🧠 Core Idea

Instead of comparing images directly, this system:

* Extracts **deep feature embeddings** from signatures
* Compares them using **cosine similarity**
* Determines whether signatures are **genuine or forged**

---


## 🧪 How It Works (Detailed)

The system follows a **feature-based verification pipeline** to determine whether a signature is genuine or forged:

### Step 1: User Input

* The user uploads a **signature image** along with their **account number / user ID**
* This ID is used to fetch the corresponding **stored reference signature** from the database

---

### Step 2: Retrieve Stored Signature

* The system queries **MongoDB** using the provided account number
* The stored signature is saved as a **base64-encoded image**
* It is:

  * Decoded into binary format
  * Converted into an image using OpenCV

---

### Step 3: Image Preprocessing

Both the **uploaded signature** and the **stored signature** go through identical preprocessing:

* Converted to **grayscale** (to remove color noise)
* Resized to a fixed dimension (**224 × 224**)
* Normalized (pixel values scaled between 0 and 1)

This ensures consistency and improves model performance.

---

### Step 4: Feature Extraction (Embedding Generation)

* The preprocessed images are passed through a **custom-trained deep learning model**
* Instead of using the final output layer, an **intermediate layer (`-8`)** is used
* This layer outputs a **feature vector (embedding)** representing the signature’s unique characteristics:

  * Stroke patterns
  * Curvature
  * Writing style

---

### Step 5: Similarity Calculation

* The system computes **cosine similarity** between:

  * Stored signature embedding
  * Uploaded signature embedding

```
similarity = cosine_similarity(stored_embedding, verifying_embedding)
```

* This produces a **similarity score between -1 and 1**

---

### Step 6: Decision Making

* A predefined threshold (e.g., **0.8**) is used:

  * If similarity > 0.8 → ✅ **Genuine Signature**
  * If similarity ≤ 0.8 → ❌ **Forged Signature**

---

### Step 7: Response Output

* The system returns a JSON response:

```
{
  "similarity": 0.87,
  "result": "Genuine"
}
```

---

### 🧠 Summary

Instead of directly comparing images, the system:

* Converts signatures into **mathematical feature vectors**
* Compares them using **cosine similarity**
* Makes a decision based on **pattern similarity**, not pixel matching

This makes the system more **robust to variations** in handwriting.


## 📐 Cosine Similarity

Measures similarity between two vectors:

```
cos(θ) = (A · B) / (||A|| ||B||)
```

* Value range: **[-1, 1]**
* Closer to **1 → more similar**

---

## 🛠️ Tech Stack

### Frontend

* React.js

### Backend

* Node.js (Main API)
* Flask (ML microservice)

### Database

* MongoDB

### Machine Learning

* TensorFlow / Keras
* Custom CNN model
* Feature embedding extraction

---

## 📁 Work Flow

```
React (Frontend)
       ↓
Node.js (API Layer)
       ↓
Flask (ML Service)
       ↓
Deep Learning Model
       ↓
Cosine Similarity Engine
```

---

## ⚙️ API Endpoint

### POST `/api/signature/verify`

**Form Data:**

* `account_number`
* `verifying_signature` (image file)

**Response:**

```
{
  "similarity": 0.87,
  "result": "Genuine"
}
```

---


## 🛠️ Tech Stack

* **Frontend:** React, React Router, CSS
* **Backend (Auth):** Node.js, Express, Mongoose, bcrypt
* **Backend (ML):** Python, Flask, TensorFlow Lite (`tflite_runtime`), OpenCV, Scikit-Learn
* **Database:** MongoDB Atlas
* **Cloud Infrastructure:** Vercel (Frontend), Render (Backends)

---

## 📂 Folder Structure


```

```text
File generated successfully.

```text
Signature-verification/
│
├── frontend/                       # React Frontend
│   ├── public/                     # Static assets (genuine.png, forged.png)
│   ├── src/
│   │   ├── components/             # Signup, Login, Upload, Verification Pages
│   │   └── App.js                  
│   ├── package.json
│   └── .env                        
│
└── backend/                        # Node.js Backend
    ├── models/                     # Mongoose schemas (User.js, Account.js)
    ├── routes/                     # API Routes (auth.js)
    ├── scripts/                    # Account creation routes (addacc.js)
    ├── server.js                   # Express Server Entry Point
    ├── package.json                
    ├── .env                        
    │
    └── deep_learning/              # Python ML API
        ├── model/                 
        │   └── feature_extractor.tflite  
        ├── verify_signature.py     # Flask Server & ML Logic
        ├── requirements.txt        
        └── .env                    

```

---

## 🚀 Installation & Local Setup Guide

Follow these steps to run the entire ecosystem on your local machine.

### Prerequisites

* [Node.js](https://nodejs.org/) (v16+)
* [Python](https://www.python.org/downloads/) (3.8+)
* A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) cluster (Free tier works perfectly)

### Step 1: Clone the Repository

```bash
git clone [https://github.com/yourusername/Signature-verification.git](https://github.com/yourusername/Signature-verification.git)
cd Signature-verification

```

### Step 2: Set up the Node.js Backend

1. Open a new terminal and navigate to the backend folder:
```bash
cd backend
npm install

```


2. Create a `.env` file in the `backend` folder and add:
```env
PORT=5000
MONGO_URI=mongodb+srv://<username>:<password>@yourcluster.mongodb.net/test
FRONTEND_URL=http://localhost:3000

```


3. Start the server:
```bash
npm start

```


*The Node server is now running on http://localhost:5000*

### Step 3: Set up the Python ML API

1. Open a second terminal and navigate to the deep learning folder:
```bash
cd backend/deep_learning

```


2. Install the required Python packages:
```bash
pip install -r requirements.txt

```


3. Create a `.env` file in the `backend/deep_learning` folder and add:
```env
PORT=5001
MONGO_URI=mongodb+srv://<username>:<password>@yourcluster.mongodb.net/test
MONGO_DB_NAME=test

```


4. Start the Flask server:
```bash
python verify_signature.py

```


*The ML API is now running on http://localhost:5001*

### Step 4: Set up the React Frontend

1. Open a third terminal and navigate to the frontend folder:
```bash
cd frontend
npm install

```


2. Create a `.env` file in the `frontend` folder and add:
```env
REACT_APP_NODE_API_URL=http://localhost:5000
REACT_APP_PYTHON_API_URL=http://localhost:5001

```


3. Start the React app:
```bash
npm start

```


*The Frontend is now running on http://localhost:3000*

You can now navigate to `http://localhost:3000` in your browser, create an account, upload a reference signature, and test the verification process!

---

## ☁️ Cloud Deployment Summary

* **Database:** Ensure your MongoDB Atlas Network Access is set to `0.0.0.0/0` to allow cloud servers to connect.
* **Node API (Render):** Deploy the `backend` directory as a Web Service. Set `Build Command` to `npm install` and `Start Command` to `npm start`.
* **Python API (Render):** Deploy the `backend/deep_learning` directory. Set `Build Command` to `pip install -r requirements.txt` and `Start Command` to `gunicorn verify_signature:app --bind 0.0.0.0:10000`.
* **Frontend (Vercel):** Import the repository, set the Root Directory to `frontend`, and add your live Render URLs to the Environment Variables.



## ⚠️ Important Notes

* 📌 Embeddings are extracted from **intermediate model layer (`-8`)**
* 📌 Threshold (`0.8`) is **empirically chosen** and can be tuned
* 📌 Model path should be configured dynamically (not hardcoded)
* 📌 Temporary file handling should be improved for scalability

---

## 🎯 Use Cases

* 🏦 Banking systems (cheque verification)
* 🧾 Document authentication
* 🛡️ Fraud detection systems
* 🆔 Identity verification

---

## 🔮 Future Improvements

* Adaptive threshold tuning
* Use **Siamese Networks / Triplet Loss**
* Store embeddings instead of raw images
* Batch verification support
* Cloud deployment (AWS/GCP/Docker)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---


## 👨‍💻 Author

**Shashank Reddy Y**

**Satvik Vattapali**

**Monisha Sarai**

**Vajra Chaitanya**

**Aditi M**

---
