from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

MODEL_PATH = "model.pkl"

# Load trained pipeline
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

NUMERIC_COLS = ['Year', 'Mileage', 'Engine', 'Power', 'Seats', 'Engine_Size']
CATEGORICAL_COLS = ['Car_ID', 'Brand', 'Model', 'Fuel_Type', 'Transmission', 'Condition']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form.to_dict()

        # Fill numeric columns with 0 if missing
        for col in NUMERIC_COLS:
            value = data.get(col)
            if value is None or value == "":
                data[col] = 0
            else:
                data[col] = float(value)

        # Fill categorical columns with 'Unknown' if missing
        for col in CATEGORICAL_COLS:
            if col not in data or data[col] == "":
                data[col] = "Unknown"

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Predict
        prediction = model.predict(df)[0]
        prediction = round(prediction, 2)

        return render_template("index.html", prediction_text=f"Predicted Price: {prediction} USD")
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
