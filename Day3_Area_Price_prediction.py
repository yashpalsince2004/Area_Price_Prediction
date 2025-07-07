import tensorflow as tf
from tensorflow import keras
import numpy as np

# Original data
x = np.array([500, 750, 1000, 1250, 1500], dtype=float)
y = np.array([50, 75, 100, 125, 150], dtype=float)  # price in lakhs

# Normalize the input data for better stability
x_scaled = x / 1000.0  # values now: 0.5, 0.75, ..., 1.5
y_scaled = y / 100.0   # values now: 0.5, 0.75, ..., 1.5

# Create model
model = keras.Sequential([
        keras.layers.Dense(10, activation='relu', input_shape=[1]),  # hidden layer with 10 neurons
    keras.layers.Dense(1)
])

# Compile with Adam optimizer (smarter & safer)
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01),
              loss='mean_squared_error')

# Train model
model.fit(x_scaled, y_scaled, epochs=500, verbose=0)

# Predict for 3000 sqft → scale input
scaled_input = np.array([[3000.0 / 1000.0]])  # = 2.0
scaled_prediction = model.predict(scaled_input)

# Rescale output to original range
final_prediction = scaled_prediction * 100.0

print("Prediction for 3000 sqft area:", final_prediction)
