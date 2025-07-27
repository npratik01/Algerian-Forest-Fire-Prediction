from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Get the directory of the current file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load models with error handling
ridge_model = None
standard_scaler = None

try:
    model_path = os.path.join(BASE_DIR, 'Models', 'ridge.pkl')
    scaler_path = os.path.join(BASE_DIR, 'Models', 'scaler.pkl')
    
    if os.path.exists(model_path) and os.path.exists(scaler_path):
        ridge_model = pickle.load(open(model_path, 'rb'))
        standard_scaler = pickle.load(open(scaler_path, 'rb'))
except Exception as e:
    print(f"Error loading models: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_data', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        if ridge_model is None or standard_scaler is None:
            return render_template('home.html', error="Models not loaded properly")
            
        try:
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
            result = ridge_model.predict(new_data_scaled)

            return render_template('home.html', result=result[0])
        except Exception as e:
            return render_template('home.html', error=str(e))
    
    else:
        return render_template('home.html')

# Export the app for Vercel
def handler(request, response):
    return app(request, response)

# This is the main entry point for Vercel
if __name__ == "__main__":
    app.run(debug=True)
