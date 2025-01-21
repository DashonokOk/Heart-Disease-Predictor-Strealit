import streamlit as st
import joblib
import pandas as pd

model = joblib.load('best_model.pkl')

def main():
    st.title('Heart Disease Prediction')

    # Ввод данных пользователем
    st.sidebar.header('User Input Parameters')

    def user_input_features():
        age = st.sidebar.slider('Age', 0, 120, 50)
        sex = st.sidebar.selectbox('Sex', ['M', 'F'])
        chest_pain_type = st.sidebar.selectbox('Chest Pain Type', ['ATA', 'NAP', 'ASY', 'TA'])
        resting_bp = st.sidebar.slider('Resting Blood Pressure', 0, 200, 120)
        cholesterol = st.sidebar.slider('Cholesterol', 0, 600, 200)
        fasting_bs = st.sidebar.selectbox('Fasting Blood Sugar', [0, 1])
        resting_ecg = st.sidebar.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
        max_hr = st.sidebar.slider('Max Heart Rate', 0, 200, 150)
        exercise_angina = st.sidebar.selectbox('Exercise Angina', ['N', 'Y'])
        oldpeak = st.sidebar.slider('Oldpeak', 0.0, 10.0, 1.0)
        st_slope = st.sidebar.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

        data = {
            'Age': age,
            'Sex': sex,
            'ChestPainType': chest_pain_type,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'RestingECG': resting_ecg,
            'MaxHR': max_hr,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # Отображение введенных данных
    st.subheader('User Input parameters')
    st.write(input_df)

    # Предсказание
    if st.button('Predict'):
        prediction = model.predict(input_df)
        st.subheader('Prediction')
        st.write(f'The prediction is: {"Heart Disease" if prediction[0] == 1 else "No Heart Disease"}')

if __name__ == '__main__':
    main()
