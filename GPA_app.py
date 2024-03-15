import streamlit as st
import numpy as np
from GPA_prediction import predict

st.title('GPA PREDICTION MODEL')

st.markdown('Predict your GPA with accuracy. Set your targte GPA now!')

st.header("STUDENTS STUDY PATTERNS")
col1, col2 = st.columns(2)

with col1:
    st.text("STUDY TIME")
    attendance = st.number_input('Attendance(%)', min_value=0, max_value=100, step=1, value=5)
    class_hours = st.number_input('Hours in Class', min_value=0, max_value=25, step=1, value=1)
    library_hours = st.number_input('Hours in Library', min_value=0, max_value=25, step=1, value=1)
    online_learning = st.number_input('Online Hours', min_value=0, max_value=15, step=1, value=0)

with col2:
    st.text("ENGAGEMENTS")
    jobs =st.number_input('Jobs', min_value=0, max_value=1, step=1, value=0)
    extracurricular = st.number_input('No. of Extracurriculars', min_value=0, max_value=10, step=1, value=0)
    sleep_hours = st.number_input('Sleep_hours', min_value=0, max_value=10, step=1, value=0)
    major = st.selectbox('Major', ['Business', 'Science', 'Engineering', 'Humanities'])

st.text('')
if st.button("Predict GPA"):
    # Call predict function
    result = predict(np.array([[attendance, class_hours, online_learning,jobs, extracurricular, sleep_hours, library_hours, major == 'Arts', major == 'Business', major == 'Science', major == 'Engineering']]))
    result += 0.2
    if result[0] < 2.0:
        st.warning("Your predicted GPA is below 2.0. Consider seeking academic advice and improving your study habits.")
    st.markdown(f'<p style="font-size:36px;font-weight:bold;">Predicted GPA: {result[0]:.2f}</p>', unsafe_allow_html=True)

st.text('')
st.text('')
st.markdown('Developed By: IRANZI INNOCENT vs MARGRET AMONDI | ` Code:` [GitHub](https://github.com/IRANZI-INNOCENT/Data-Sciennce)')
