import streamlit as st
import numpy as np
from GPA_prediction import predict

st.title('GPA PREDICTION MODEL')

st.markdown('Enter your preferred parameters to predict your GPA. For Science, Engineering, Arts, Business, and jobs; Enter 1 for Yes and 0 for NO')

st.header("STUDENTS STUDY PATTERNS")
col1, col2 = st.columns(2)

with col1:
    st.text("STUDY TIME")
    attendance = st.number_input('Attendance', min_value=0, max_value=100, step=1, value=5)
    class_hours = st.number_input('Class_hours_week', min_value=0, max_value=25, step=1, value=1)
    online_learning = st.number_input('Online_learning', min_value=0, max_value=25, step=1, value=1)
    library_hours = st.number_input('Library_hours', min_value=0, max_value=25, step=1, value=1)

with col2:
    st.text("ENGAGEMENTS")
    jobs = st.number_input('jobs (Enter 1 for Yes, 0 for No)', min_value=0, max_value=1, step=1, value=0)
    extracurricular = st.number_input('Extracurricular', min_value=0, max_value=10, step=1, value=0)
    sleep_hours = st.number_input('Sleep_hours', min_value=0, max_value=10, step=1, value=0)
    major = st.selectbox('Major', ['Business', 'Science', 'Engineering', 'Arts'])

    if major in ['Business', 'Science', 'Engineering', 'Arts']:
        major_yes_or_no = st.number_input(f'{major} (Enter 1 for Yes, 0 for No)', min_value=0, max_value=1, step=1, value=0)

st.text('')
if st.button("Predict GPA"):
    # Call predict function
    result = predict(np.array([[attendance, class_hours, online_learning, jobs, extracurricular, sleep_hours, library_hours,
                                 major == 'Arts', major == 'Business', major == 'Science', major == 'Engineering',
                                 major_yes_or_no if major in ['Business', 'Science', 'Engineering', 'Arts'] else 0]]))
    predicted_gpa = result[0]
    st.text('Predicted GPA: {:.2f}'.format(predicted_gpa))
    
    # Check if predicted GPA is below 2.0
    if predicted_gpa < 2.0:
        st.warning("Your predicted GPA is below 2.0. We recommend seeking advice from academic advisors, increasing classwork, considering group work, identifying personal problems, etc., to improve your GPA.")

st.text('')
st.text('')
st.markdown('`By`  IRANZI ft MARGRET | ` Code:` [GitHub](https://github.com/IRANZI-INNOCENT/Data-Sciennce)')
