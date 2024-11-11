# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris
# Charger le modèle pré-entraîné
model = joblib.load("iris_naive_bayes_model.pkl")

# Initialiser FastAPI
app = FastAPI()

# Schéma des données d'entrée pour la prédiction
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Point de terminaison pour prédire la classe de la fleur
@app.post("/predict")
def predict(iris: IrisData):
    data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    prediction = model.predict(data)
    class_name = load_iris().target_names[prediction[0]]
    return {"prediction": class_name}
