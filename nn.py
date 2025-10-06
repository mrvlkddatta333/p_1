import numpy as np 
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense 
from tensorflow.keras.optimizers import Adam 
# Training data (XOR truth table) 
X = np.array([[0, 0], 
 [0, 1], 
 [1, 0],[1, 1]], dtype=np.float32) 
y = np.array([0, 1, 1, 0], dtype=np.float32) 
# Neural Network model 
model = Sequential([ 
 Dense(4, activation='relu', input_shape=(2,)), 
 Dense(1, activation='sigmoid') 
]) 
# Compile the model 
model.compile(optimizer=Adam(learning_rate=0.1), 
 loss='binary_crossentropy', 
 metrics=['accuracy']) 
# Train the model 
print("Training progress:") 
history = model.fit(X, y, epochs=1000, verbose=0) 
# Print training progress at intervals 
for i in range(0, 1000, 100): 
 loss, acc = history.history['loss'][i], history.history['accuracy'][i] 
 print(f"Epoch {i}: loss = {loss:.4f}, accuracy = {acc:.4f}") 
# Predictions 
predictions = model.predict(X) 
predicted_classes = (predictions > 0.5).astype(int) 
print("\nFinal Predictions:") 
for i in range(len(X)): 
 print(f"Input: {X[i]}, Predicted: {predicted_classes[i][0]} "f"(prob: {predictions[i][0]:.4f}), Actual: {y[i]}")
# Display model architecture
print("\nModel architecture:")
model.summary()
