import pandas as pd

df = pd.read_csv("D:/Datasets/iris.csv")
print(df.head())

X = df.iloc[:, :-1].values
print(X.shape)
print(X[:3])


y = df.iloc[:, -1]
print(y.shape)
print(y[:6])


from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y = encoder.fit_transform(y)

print(y[:3])


import joblib

joblib.dump(encoder, "saved_models/02.iris_label_encoder.pkl")


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
print("Accuracy: % {:10.2f}".format(accuracy * 100))


import joblib
joblib.dump(classifier, "saved_models/01.knn_with_iris_dataset.pkl")



classifier_loaded = joblib.load("saved_models/01.knn_with_iris_dataset.pkl")
encoder_loaded = joblib.load("saved_models/02.iris_label_encoder.pkl")


X_manual_test = [[4.0, 4.0, 4.0, 4.0]]
print("X_manual_test", X_manual_test)

prediction_raw = classifier_loaded.predict(X_manual_test)
print("prediction_raw", prediction_raw)

prediction_real = encoder_loaded.inverse_transform(classifier.predict(X_manual_test))
print("Real prediction", prediction_real)
