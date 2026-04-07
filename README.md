# ✍️ Signature Verification System

A **deep learning-based Signature Verification System** that authenticates handwritten signatures using a **custom-trained neural network** and **cosine similarity on feature embeddings**.

This system is designed for **real-world financial security applications**, such as cheque verification and fraud detection.

---

## Deployed Link
https://signature-verification-rmf8.onrender.com

## 🧠 Core Idea

Instead of comparing images directly, this system:

* Extracts **deep feature embeddings** from signatures
* Compares them using **cosine similarity**
* Determines whether signatures are **genuine or forged**

---

## 🚀 Key Features

* 🔐 Secure user authentication (MERN stack)
* 🧠 **Custom-trained deep learning model**
* 📐 **Embedding-based comparison using cosine similarity**
* ⚡ Real-time verification via Flask API
* 🗄️ MongoDB integration (stores signatures as base64)
* 🌐 React frontend for smooth UX

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
