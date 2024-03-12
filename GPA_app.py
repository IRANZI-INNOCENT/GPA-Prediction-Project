import streamlit as st
import numpy as np
from GPA_prediction import predict

st.title('GPA PREDICTION MODEL')

st.markdown('Enter your preferred parameters to predict your GPA. For Science,Engineering, Arts, Business and jobs; Enter 1 for Yes and 0 for NO')

st.header("STUDENTS STUDY PATTERNS")
col1, col2, col3 = st.columns(3)

with col1:
    st.text("STUDY TIME")
    attendance = st.slider('Attendance', 0, 100, 5)
    class_hours = st.slider('Class_hours_week', 0, 25, 1)
    online_learning = st.slider('Online_learning', 0, 25, 1)
    library_hours = st.slider('Library_hours', 0, 25, 1)

with col2:
    st.text("ENGAGEMENTS")
    jobs = st.slider('jobs', 0, 1, 0)
    extracurricular = st.slider('Extracurricular', 0, 10, 0)
    sleep_hours = st.slider('Sleep_hours', 0, 10, 0)

with col3:
    st.text("MAJOR")
    business = st.slider('Business', 0, 1, 0)
    science = st.slider('Science', 0, 1, 0)
    engineering = st.slider('Engineering', 0, 1, 0)
    arts = st.slider('Arts', 0, 1, 0)

st.text('')
if st.button("Predict GPA"):
    # Call predict function
    result = predict(np.array([[attendance, class_hours, online_learning, jobs, extracurricular, sleep_hours, library_hours, arts,business, science, engineering]]))
    st.text('Predicted GPA: {:.2f}'.format(result[0]))

st.text('')
st.text('')
st.markdown(
    '`By`  IRANZI ft MARGRET | ` Code:` [GitHub](https://github.com/IRANZI-INNOCENT/Data-Sciennce)')
