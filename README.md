# AgriAI

AgriAI is an innovative project aimed at leveraging artificial intelligence to enhance agricultural practices. This repository contains the source code and related materials for the AgriAI system, which utilizes machine learning and AI techniques to provide valuable insights and predictions for the agricultural sector.

## Overview

AgriAI aims to revolutionize the agriculture industry by offering AI-powered tools and solutions that help farmers make informed decisions, optimize crop yields, and manage resources efficiently. The project includes various modules for data analysis, prediction, and visualization.

## Features

- **Crop Prediction**: Predict the best crops to plant based on soil, weather, and historical data.
- **Yield Estimation**: Estimate crop yields using machine learning models.
- **Soil Analysis**: Analyze soil quality and provide recommendations for improvement.
- **Weather Forecasting**: Integrate weather forecasts to aid in planning agricultural activities.
- **Resource Management**: Optimize the use of water, fertilizers, and other resources.

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn, TensorFlow
- **Database**: SQLite3
- **APIs**: OpenWeatherMap API (for weather data)

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python Package Installer)

### Steps

1. **Clone the Repository**
    
    bash
    
    Copy code
    
    `git clone https://github.com/NagiPragalathan/AgriAI.git
    cd AgriAI` 
    
2. **Install Dependencies**
    
    bash
    
    Copy code
    
    `pip install -r requirements.txt` 
    
3. **Run Migrations**
    
    bash
    
    Copy code
    
    `python manage.py migrate` 
    
4. **Start the Development Server**
    
    bash
    
    Copy code
    
    `python manage.py runserver` 
    
5. **Open your browser** and navigate to `http://localhost:8000` to access the AgriAI dashboard.
    

## Project Structure

csharp

Copy code

`AgriAI/
├── agri_ai/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── crop_prediction/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── soil_analysis/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── prediction.html
│   ├── analysis.html
├── static/
│   ├── css/
│   ├── js/
├── manage.py
├── requirements.txt
└── README.md` 

## Usage

- **Dashboard**: Access the main dashboard to get an overview of current predictions and analyses.
- **Crop Prediction**: Enter relevant data to predict the best crops to plant.
- **Yield Estimation**: Input crop details and get yield estimates.
- **Soil Analysis**: Upload soil data and receive quality assessments and recommendations.
- **Weather Forecasting**: View weather forecasts to plan agricultural activities accordingly.

## Contributing

Contributions are welcome! If you have an idea for an improvement or a new feature, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.
