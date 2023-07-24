from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

# Load the training dataset.
(x_train, y_train) = tf.keras.datasets.mnist.load_data()

# Normalize the training data.
x_train = x_train / 255.0

# Create the model.
model = Sequential([
  Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
  MaxPooling2D(pool_size=(2, 2)),
  Conv2D(64, kernel_size=(3, 3), activation='relu'),
  MaxPooling2D(pool_size=(2, 2)),
  Flatten(),
  Dense(128, activation='relu'),
  Dense(10, activation='softmax')
])

# Compile the model.
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model.
model.fit(x_train, y_train, epochs=10)

# Evaluate the model.
loss, accuracy = model.evaluate(x_train, y_train)
print('Loss:', loss)
print('Accuracy:', accuracy)

# Save the model.
model.save('model.h5')

# Load the model.
model = tf.keras.models.load_model('model.h5')

# Predict the emotion of an image.
image = tf.keras.utils.load_img('image.jpg', target_size=(28, 28))
image = tf.keras.utils.img_to_array(image)
image = image / 255.0
image = image.reshape(1, 28, 28, 1)
prediction = model.predict(image)
print(prediction)