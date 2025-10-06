import tensorflow as tf 
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import classification_report, accuracy_score 
import matplotlib.pyplot as plt 
import numpy as np 
# 1) Load the MNIST dataset from TensorFlow 
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
# 2) Normalize pixel values to [0, 1] 
X_train = X_train / 255.0 
X_test = X_test / 255.0 
# 3) Flatten images from 28x28 to 784-dimensional vectors 
X_train = X_train.reshape(X_train.shape[0], -1) 
X_test = X_test.reshape(X_test.shape[0], -1) 
# 4) Create an MLP classifier (single hidden layer with 100 neurons) 
mlp = MLPClassifier( 
 hidden_layer_sizes=(100,), 
 max_iter=10, 
 solver='adam', 
 random_state=42 
) 
# 5) Train the model 
mlp.fit(X_train, y_train) 
# 6) Make predictions on the test set 
y_pred = mlp.predict(X_test) 
# 7) Evaluate the model 
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
# 8) Visualize a few test images with predicted labels
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
axes = axes.ravel()
for i in range(10):
 axes[i].imshow(X_test[i].reshape(28, 28), cmap='gray')
 axes[i].set_title(f'Pred: {y_pred[i]}')
 axes[i].axis('off')
plt.tight_layout()
plt.show()
