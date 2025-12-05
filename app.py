from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

feature_cols = [
    "Global_active_power",
    "Global_reactive_power",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    
    if request.method == "POST":
        values = []
        for col in feature_cols:
            values.append(float(request.form[col]))

        arr = np.array(values).reshape(1, -1)
        prediction = round(model.predict(arr)[0], 3)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
