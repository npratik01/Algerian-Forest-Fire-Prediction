# Algerian Forest Fire Prediction

A machine learning web application that predicts Fire Weather Index (FWI) for Algerian forest fires using meteorological data.

## Features

- **Modern UI**: Beautiful, responsive design with glassmorphism effects
- **Real-time Predictions**: Instant fire risk assessment
- **Interactive Form**: User-friendly input form with tooltips and validation
- **Risk Classification**: Color-coded risk levels (Low, Moderate, High, Very High)
- **Mobile Responsive**: Works seamlessly on all devices

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: Scikit-learn (Ridge Regression)
- **Deployment**: Vercel

## Input Parameters

- **Temperature**: Air temperature in degrees Celsius
- **RH**: Relative humidity percentage
- **Ws**: Wind speed in km/h
- **Rain**: Rainfall in millimeters
- **FFMC**: Fine Fuel Moisture Code
- **DMC**: Duff Moisture Code
- **ISI**: Initial Spread Index
- **Classes**: Fire danger class
- **Region**: Region identifier

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python application.py`
4. Open http://localhost:5000 in your browser

## Deployment

This application is configured for deployment on Vercel with the following files:

- `vercel.json`: Vercel configuration
- `index.py`: Entry point for Vercel
- `runtime.txt`: Python version specification
- `.vercelignore`: Files to exclude from deployment

## Live Demo

[Deploy your own copy to Vercel](https://vercel.com/new/clone)
