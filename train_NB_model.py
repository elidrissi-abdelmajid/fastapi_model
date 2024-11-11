# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib

# Charger le dataset Iris
data = load_iris()
X, y = data.data, data.target

# Diviser en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Évaluer le modèle
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Sauvegarder le modèle
joblib.dump(model, "iris_naive_bayes_model.pkl")
