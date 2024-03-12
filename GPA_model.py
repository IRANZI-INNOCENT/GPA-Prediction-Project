import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import joblib

Datathon = pd.read_csv('data.csv')
x,y = Datathon[['Class_hours_week','Attendance','Online_learning','Extracurricular','Sleep_hours','Business','Library_hours','Arts',
               'Engineering','Science','jobs']].values, Datathon["College GPA"].values
x_train, x_test,y_train,y_test = train_test_split(x,y, test_size=0.3, random_state=0)
model = LinearRegression().fit(x_train, y_train)


predictions = model.predict(x_test)
mse = mean_squared_error(y_test, predictions)
print('Mean Squared Error:', mse)
joblib.dump(model, 'gpa_prediction_model.pkl')
