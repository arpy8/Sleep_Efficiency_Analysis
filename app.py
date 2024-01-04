import pickle
import streamlit as st

def predict_quality(input_data):
    with open('model/rf_model.pkl', 'rb') as file:
        model = pickle.load(file)
    predictions = model.predict(input_data)
    return predictions

st.title('Sleep Efficiency Analysis')
st.write('This app predicts the quality of your sleep based on your sleep data')

gender = st.selectbox("Gender", ["Male", "Female"], index=1)

left, mid, right = st.columns((10, 1, 10))
with left:
    age = st.slider('Age', 18, 100, 46)
    s_duration = st.slider('Sleep duration', 0.0, 24.0, 7.04)
    caffeine = st.slider('Caffeine consumption', 0, 1000, 0)
    
with mid:
    st.write('')
    
with right:
    awakenings = st.slider('Awakenings', 0, 10, 1)
    deep_sleep = st.slider('Deep sleep percentage', 0, 100, 60)
    light_sleep = st.slider('Light sleep percentage', 0, 100, 10)
    
rem_sleep = 100-(deep_sleep+light_sleep)
    
if st.button('Predict', use_container_width=True):
    input_data = [[age, 1 if gender=="Male" else 0, s_duration, rem_sleep, deep_sleep, light_sleep, float(awakenings), float(caffeine)]]
    predictions = predict_quality(input_data)
    final_prediction = int(round(predictions[0]*100, 3))
    final = ""
    
    if final_prediction>=80:
        st.balloons()
        final = "good"
    elif final_prediction>=50:
        final = "moderate"
    else:
        final = "poor"
        
    
    st.info(f'##### Sleep Score : {final_prediction}%\nYour sleep was {final}.')