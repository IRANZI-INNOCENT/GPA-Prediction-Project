import joblib

def predict(data):
    gpa_model = joblib.load("C:\\Users\\Admin\\OneDrive\\Desktop\\ML PROJECT\\GPA App\\gpa_prediction_model.pkl")
    predicted_gpa = gpa_model.predict(data)
    return predicted_gpa
