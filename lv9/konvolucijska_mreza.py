from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime
import seaborn as sns

# Učitavanje podataka
train_dataset = image_dataset_from_directory(
    "./gtsrb/Train",  
    validation_split=0.2,  
    labels='inferred',
    label_mode='categorical',
    subset="training",
    seed=123,
    image_size=(48, 48),
    batch_size=32
)

val_dataset = image_dataset_from_directory(
    "./gtsrb/Train",  
    validation_split=0.2,  
    labels='inferred',
    label_mode='categorical',
    subset="validation",
    seed=123,
    image_size=(48, 48),
    batch_size=32
)

test_dataset = image_dataset_from_directory(
    "./gtsrb/Test", 
    labels='inferred',
    label_mode='categorical',
    image_size=(48, 48),
    batch_size=32
)

# Definicija modela
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(48, 48, 3)),
    layers.Conv2D(32, (3, 3), activation='relu', padding='valid'),
    layers.MaxPooling2D((2, 2), strides=2),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(43, activation='softmax') 
])

model.compile(optimizer=optimizers.Adam(),
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Callbackovi
checkpoint_cb = ModelCheckpoint("best_model.h5", save_best_only=True)
log_dir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_cb = TensorBoard(log_dir=log_dir)

# Treniranje modela
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=2,
    callbacks=[checkpoint_cb, tensorboard_cb]
)

# Evaluacija na testnom skupu
model.load_weights("best_model.h5")  # Učitavanje najboljeg modela
test_loss, test_accuracy = model.evaluate(test_dataset)
print(f"Točnost na testnim podacima: {test_accuracy:.2f}")

# Predikcije i matrica zabune
y_true = np.concatenate([y for x, y in test_dataset], axis=0)
y_pred = np.argmax(model.predict(test_dataset), axis=1)

conf_matrix = confusion_matrix(y_true, y_pred)


# Plot matrice zabune
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=True, yticklabels=True)
plt.title("Matrica zabune")
plt.xlabel("Predviđene klase")
plt.ylabel("Stvarne klase")
plt.show()

# Opcionalno: ispis detaljnog izvještaja
print("Izvještaj klasifikacije:")
print(classification_report(y_true, y_pred))