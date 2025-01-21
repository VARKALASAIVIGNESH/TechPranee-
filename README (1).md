# Manufacturing Predictive Analysis API

This project provides a RESTful API to predict machine downtime in manufacturing operations based on features such as temperature and runtime. It uses a logistic regression model to predict the likelihood of machine downtime.

## Table of Contents

- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
  - [Upload Dataset](#upload-dataset)
  - [Train Model](#train-model)
  - [Predict Downtime](#predict-downtime)
- [Testing the API with cURL](#testing-the-api-with-curl)
- [License](#license)

## Overview

This API predicts machine downtime using a logistic regression model. The model is trained on a synthetic manufacturing dataset with features such as temperature, run time, and downtime flag. It provides the following functionalities:

- Upload a CSV dataset
- Train a machine learning model
- Predict machine downtime based on given features

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/manufacturing_predictive_model.git
cd manufacturing_predictive_model

## Overview

This API predicts machine downtime using a logistic regression model. The model is trained on a synthetic manufacturing dataset with features such as temperature, run time, and downtime flag. It provides the following functionalities:

- Upload a CSV dataset
- Train a machine learning model
- Predict machine downtime based on given features

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/manufacturing_predictive_model.git
cd manufacturing_predictive_model
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If you don’t have a `requirements.txt` file, you can use the following command to install necessary dependencies:

```bash
pip install flask pandas scikit-learn joblib
```

### 4. Run the Flask API

To start the Flask application, run the following command:

```bash
python app.py
```

The Flask server will be running at `http://127.0.0.1:5000/`.

## API Endpoints

### Upload Dataset
open command prompt in vs code 

**POST** `/upload`

This endpoint accepts a CSV file to upload the manufacturing data.

#### Request Body:
- `file`: A CSV file containing manufacturing data (e.g., `synthetic_manufacturing_data.csv`).

#### Example:

```bash
curl -X POST -F "file=@synthetic_manufacturing_data.csv" http://127.0.0.1:5000/upload
```

#### Response:

```json
{
    "message": "File 'synthetic_manufacturing_data.csv' uploaded successfully!"
}
```

### Train Model

**POST** `/train`

This endpoint trains the machine learning model on the uploaded dataset.

#### Example:

```bash
curl -X POST http://127.0.0.1:5000/train
```

#### Response:

```json
{
    "accuracy": 0.85,
    "message": "Model trained successfully!"
}
```

### Predict Downtime

**POST** `/predict`

This endpoint predicts whether the machine will experience downtime based on input data (temperature and run time).

#### Request Body:
```json
{
  "Temperature": 85,
  "Run_Time": 200
}
```

#### Example:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"Temperature\": 85, \"Run_Time\": 200}" http://127.0.0.1:5000/predict
```

#### Response:

```json
{
    "Downtime": "Yes",
    "Confidence": 0.91
}
```

## Testing the API with cURL

### 1. Upload the dataset:

```bash
curl -X POST -F "file=@synthetic_manufacturing_data.csv" http://127.0.0.1:5000/upload
```

### 2. Train the model:

```bash
curl -X POST http://127.0.0.1:5000/train
```

### 3. Make a prediction:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"Temperature\": 85, \"Run_Time\": 200}" http://127.0.0.1:5000/predict
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

