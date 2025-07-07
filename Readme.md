# 🏠 Area-Price Prediction using TensorFlow

This repository contains a simple example of predicting house prices based on area using a neural network built with TensorFlow and Keras.

It trains a regression model to predict the price (in lakhs) of a house given its area (in square feet).  
The dataset is tiny and illustrative — designed for educational and demonstration purposes.

---

## 📄 Project Overview

- 📈 **Input:** Area of the house in square feet.
- 🎯 **Output:** Predicted price of the house in lakhs.
- 🧠 **Model:** A small feedforward neural network with one hidden layer.
- ⚙️ **Tech Stack:** Python, TensorFlow, Keras, NumPy.

---

## 🚀 How It Works

✅ Data is normalized for stability during training.  
✅ The model is trained on a very small dataset:

| Area (sqft) | Price (lakhs) |
|-------------|---------------|
| 500         | 50            |
| 750         | 75            |
| 1000        | 100           |
| 1250        | 125           |
| 1500        | 150           |

✅ After training, the model predicts the price for a **3000 sqft** house.

---

## 📂 Files

| File                          | Description                        |
|-------------------------------|------------------------------------|
| `Day3_Area_Price_prediction.py` | Python script that trains the model and predicts the price. |

---

## 📋 Usage

### 🔗 Prerequisites
- Python ≥ 3.7
- TensorFlow ≥ 2.x
- NumPy

### 📦 Install dependencies
```bash
pip install tensorflow numpy
```

### 🏃 Run the script
```bash
python Day3_Area_Price_prediction.py
```

---

## 📊 Output Example
```
Prediction for 3000 sqft area: [[~]]
```
The output shows the predicted price (in lakhs) for a house of 3000 sqft area.

---

## 📖 Notes
- The dataset is minimal and linear — in practice, you’d use a much larger and more realistic dataset.
- The model uses a single hidden layer with ReLU activation.

---

## 🤝 Contributing
Contributions, suggestions, and improvements are welcome. Please open an issue or submit a pull request.

---

## 📜 License
This project is licensed under the MIT License.