# GPA Prediction Application

## Overview
This project is a web application that predicts a student's GPA based on various factors such as study hours, attendance, extracurricular activities, and major. The project leverages a linear regression model trained on student data and uses `Streamlit` for the user interface.

## Project Structure
The project includes the following key files:
1. **GPA_model.py**: This file contains the code for loading and training the GPA prediction model using linear regression. It trains the model on student data and saves the trained model as `gpa_prediction_model.pkl`.
   
2. **GPA_app.py**: This file is the web application built using Streamlit. It allows users to input study patterns and predicts their GPA using the pre-trained model.
   
3. **data.csv**: A dataset containing various features such as attendance, study hours, and extracurricular activities, used to train the model.

## Installation

### Prerequisites
- Python 3.x
- Libraries: You can install all required libraries using the following command:
  ```bash
  pip install -r requirements.txt
  ```

### Required Libraries
- pandas
- numpy
- scikit-learn
- joblib
- streamlit

### How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/IRANZI-INNOCENT/GPA-Prediction-Project.git
    cd GPA-Prediction-Project
    ```

2. Train the model:
   The `GPA_model.py` script is used to train the linear regression model and save it as `gpa_prediction_model.pkl`. If you wish to retrain the model, simply run:
    ```bash
    python GPA_model.py
    ```

3. Launch the web application:
   Use Streamlit to launch the GPA prediction web app:
    ```bash
    streamlit run GPA_app.py
    ```

4. Open the local URL provided by Streamlit in your browser to interact with the application.

## How it Works

### Training
- The `GPA_model.py` script loads the dataset (`data.csv`) and trains a linear regression model to predict students' GPA based on input features such as:
  - Class_hours_week
  - Attendance
  - Online_learning
  - Extracurricular
  - Sleep_hours
  - Library_hours
  - Major (Business, Arts, Engineering, Science)
  - Jobs

The trained model is saved as `gpa_prediction_model.pkl` using `joblib`.

### Prediction
- The `GPA_app.py` uses the Streamlit library to create an interactive user interface.
- Users input their study patterns, and the `predict()` function is called to load the pre-trained model and output a predicted GPA. Adjustments are made to the prediction based on certain conditions (e.g., adding 0.2 to the predicted GPA).

## Example Use Case
1. Input:
   - Attendance: 90%
   - Hours in Class: 15
   - Hours in Library: 5
   - Online Hours: 3
   - Jobs: 0
   - Extracurriculars: 2
   - Sleep Hours: 7
   - Major: Science
2. The predicted GPA will be displayed as a result.

## Dataset
The `data.csv` file contains student records used to train the model. It includes features such as study hours, major, and attendance to predict the `College GPA` of each student.

## Model Evaluation
The model is evaluated using Mean Squared Error (MSE) to measure the prediction accuracy.

## Contributors
- IRANZI INNOCENT
- MARGRET AMONDI
