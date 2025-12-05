import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load pre-trained model
model_svc = pickle.load(open('model_svc.pkl', 'rb'))

# Load the processed data for dropdown options
df = pd.read_csv('processed_data.csv')

# Extract unique values for each feature (excluding specific columns)
dropdown_columns = ['bedrooms', 'bathrooms', 'floors', 'waterfront', 'view', 'condition', 'yr_built', 'yr_renovated', 'street', 'city', 'statezip']
dropdown_values = {col: df[col].unique() for col in dropdown_columns}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract selected values from the form, including the missing features
        form_data = {col: request.form[col] for col in dropdown_columns}
        
        # Add the missing features manually (you can add dropdowns or inputs for them in the form)
        sqft_living = float(request.form['sqft_living'])  # Example: Get value from user input
        sqft_lot = float(request.form['sqft_lot'])
        sqft_above = float(request.form['sqft_above'])
        sqft_basement = float(request.form['sqft_basement'])

        # Collect the values from the form and create an input for prediction
        input_data = [
            int(form_data['bedrooms']),
            float(form_data['bathrooms']),
            float(form_data['floors']),
            int(form_data['waterfront']),
            int(form_data['view']),
            int(form_data['condition']),
            int(form_data['yr_built']),
            int(form_data['yr_renovated']),
            sqft_living,
            sqft_lot,
            float(sqft_above),
            float(sqft_basement),
            form_data['street'],  # Assuming you are processing this feature correctly
            form_data['city'],    # You may need to convert this to a numeric format (e.g., using one-hot encoding)
            form_data['statezip'] # Same for statezip
        ]
        
        # Predict using the model
        prediction = model_svc.predict([input_data])
        predicted_price = prediction[0]

        return render_template('index.html', dropdown_values=dropdown_values, predicted_price=predicted_price)
    
    return render_template('index.html', dropdown_values=dropdown_values, predicted_price=None)

if __name__ == '__main__':
    app.run(debug=True)
