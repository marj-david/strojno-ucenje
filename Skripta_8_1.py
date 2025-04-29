import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow.keras as keras
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras import callbacks

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)


model = models.Sequential([
layers.Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)),
layers.MaxPooling2D((2, 2)),
layers.Flatten(),
layers.Dense(32, activation='relu'),
layers.Dense(10, activation='softmax')
])


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

tensorboard_callback = callbacks.TensorBoard(
    log_dir='./logs',  # Direktorij za spremanje logova
    histogram_freq=1,  # Učestalost zapisivanja histograma
    write_graph=True,  # Zapisivanje grafa modela
    write_images=True  # Zapisivanje težina kao slika
)



model.fit(x_train, y_train_s, epochs=1, batch_size=128, validation_split=0.1)

train_pred = np.argmax(model.predict(x_train), axis=1)
test_pred = np.argmax(model.predict(x_test), axis=1)

print("Točnost na trening skupu:", accuracy_score(y_train, train_pred))
print("Točnost na testnom skupu:", accuracy_score(y_test, test_pred))

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.heatmap(confusion_matrix(y_train, train_pred), annot=True, fmt="d", cmap="Blues")
plt.title("Matrica zabune - Trening")

plt.subplot(1, 2, 2)
sns.heatmap(confusion_matrix(y_test, test_pred), annot=True, fmt="d", cmap="Greens")
plt.title("Matrica zabune - Test")
plt.show()