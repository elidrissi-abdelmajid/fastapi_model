# Iris Classification Model with FastAPI and Docker

This repository contains an Iris classification model deployed using **FastAPI** and **Docker**. The model is trained on the famous **Iris dataset** and is capable of classifying Iris flowers based on their features (sepal length, sepal width, petal length, and petal width). The model is served as an API that takes input data and returns the predicted class.

## Features

- **Iris Flower Classification**: The model classifies iris flowers into three species: **Setosa**, **Versicolor**, and **Virginica**.
- **FastAPI**: A fast and efficient web framework to serve the model.
- **Docker**: The app is containerized for easy deployment and scalability.

## Setup

Follow these steps to run the Iris classification model with FastAPI in a Docker container.

### 1. Clone the Repository


    git clone https://github.com/your-username/iris-model-fastapi.git
    cd iris-model-fastapi
2. Install Dependencies

# Create virtual environment (optional)
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt
The requirements.txt includes FastAPI, Uvicorn, and other necessary libraries.

3. Docker Setup
If you prefer to run the app in a Docker container, follow these steps:

Build the Docker image:

docker build -t iris-fastapi-app .
Run the Docker container:


docker run -d -p 8000:80 iris-fastapi-app
This will start the FastAPI application on port 8000.

4. API Endpoints
The FastAPI app exposes a POST endpoint where you can send the input features of the Iris flower and get the predicted class.

URL: http://127.0.0.1:8000/predict/

Method: POST

Request Body: A JSON object with the following structure:

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
Response: The response will return a JSON object with the predicted class of the Iris flower:


{
  "prediction": "setosa"
}
5. Example Request with curl
You can test the API using curl or a REST client like Postman.

curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
6. Example Request with Python

import requests

url = 'http://127.0.0.1:8000/predict/'
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
response = requests.post(url, json=data)
print(response.json())
7. Stopping the Docker Container
To stop the container:

docker stop <container-id>
You can find the container ID by running:


docker ps
8. How the Model Was Trained
The model is trained using the famous Iris dataset from scikit-learn.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'iris_model.pkl')
The trained model (iris_model.pkl) is then loaded in the FastAPI app to make predictions.

### Key Sections in `README.md`:
1. **Introduction**: Explains what the repository is about.
2. **Setup**: Details on how to install dependencies and run the app locally or in Docker.
3. **API Endpoints**: How to interact with the API for predictions.
4. **Training Model**: How the model was trained (optional, if you want to include it).
5. **License & Author**: Your information and the license you want to use.




