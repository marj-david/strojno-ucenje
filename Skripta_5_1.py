import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report

# ucitaj podatke za ucenje
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()


#dijeljenje pdoataka
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y)

#skaliranje
scaler = StandardScaler()

print(scaler.fit(df))
StandardScaler()

print(scaler.mean_)

#kneigh algoritam
neigh = KNeighborsClassifier(n_neighbors=10)

neigh.fit(X_train, y_train)
KNeighborsClassifier(n_neighbors=1)

print(neigh.kneighbors([[1., 1.]]))

y_true = y_test
y_pred = neigh.predict(X_test)

# Izracunaj matricu zabune i prikazi ju
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class 0', 'Class 1'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

# Izracunaj preciznost
precision = precision_score(y_true, y_pred)
# Izracunaj odziv
recall = recall_score(y_true, y_pred)
# Izracunaj tocnost
accuracy = accuracy_score(y_true, y_pred)
# Report
print(classification_report(y_true, y_pred))

# Scatter plot
plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()
