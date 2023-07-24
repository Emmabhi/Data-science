from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten

# Load the training dataset.
(x_train, y_train) = load_dataset('disease_dataset.csv')

# Normalize the training data.
x_train = x_train / 255.0

# Create the model.
model = Sequential([
  Dense(128, activation='relu', input_shape=(len(x_train[0]),)),
  Dropout(0.5),
  Dense(64, activation='relu'),
  Dropout(0.5),
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

# Predict the disease of a patient.
symptoms = ['fever', 'cough', 'sore throat']

# Convert the symptoms to a vector.
symptoms_vector = np.array([1 if symptom in symptoms else 0 for symptom in list(x_train[0])])

# Predict the disease.
prediction = model.predict(symptoms_vector)

# Print the prediction.
print('The patient is most likely to have disease:', prediction.argmax())