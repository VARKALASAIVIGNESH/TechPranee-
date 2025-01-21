from flask import Flask, request, jsonify
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)

# path
UPLOAD_FOLDER = './data'
MODEL_FOLDER = './model'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Welcome to the Manufacturing Predictive Analysis API!"

# Upload Dataset
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({"message": f"File '{file.filename}' uploaded successfully!"}), 200

# Train Model
@app.route('/train', methods=['POST'])
def train_model():
    file_path = os.path.join(UPLOAD_FOLDER, 'synthetic_manufacturing_data.csv')  # Hardcoded for now
    if not os.path.exists(file_path):
        return jsonify({"error": "Dataset not found. Please upload the file first."}), 400

    # Load the dataset
    data = pd.read_csv(file_path)

    # Preprocess the data
    X = data[['Temperature', 'Run_Time']]  # Features or independent
    y = data['Downtime_Flag']  # Target variable or dependent

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    model_path = os.path.join(MODEL_FOLDER, 'model.pkl')
    joblib.dump(model, model_path)

    #accuracy
    accuracy = model.score(X_test, y_test)

    return jsonify({"message": "Model trained successfully!", "accuracy": accuracy}), 200

# Predict Downtime
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validate input data
    if 'Temperature' not in data or 'Run_Time' not in data:
        return jsonify({"error": "Please provide 'Temperature' and 'Run_Time'."}), 400

    # Load the trained model
    model_path = os.path.join(MODEL_FOLDER, 'model.pkl')
    if not os.path.exists(model_path):
        return jsonify({"error": "Model not trained yet. Please train the model first."}), 400

    model = joblib.load(model_path)

    # Predict the downtime
    input_data = [[data['Temperature'], data['Run_Time']]]
    prediction = model.predict(input_data)
    confidence = max(model.predict_proba(input_data)[0])  # Confidence level

    result = {
        "Downtime": "Yes" if prediction[0] == 1 else "No",
        "Confidence": round(confidence, 2)
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
