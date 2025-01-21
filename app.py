import streamlit as st
import joblib
import pandas as pd

# Загрузка модели
model = joblib.load('best_model.pkl')

# Streamlit приложение
def main():
    st.title('Предсказание сердечных заболеваний')

    # Ввод данных пользователем
    st.sidebar.header('Параметры ввода пользователя')

    def user_input_features():
        age = st.sidebar.slider('Возраст', 0, 120, 50)
        sex = st.sidebar.selectbox('Пол', ['М', 'Ж'])
        chest_pain_type = st.sidebar.selectbox('Тип боли в груди', ['ATA', 'NAP', 'ASY', 'TA'])
        resting_bp = st.sidebar.slider('Артериальное давление в покое', 0, 200, 120)
        cholesterol = st.sidebar.slider('Уровень холестерина', 0, 600, 200)
        fasting_bs = st.sidebar.selectbox('Уровень сахара в крови натощак', [0, 1])
        resting_ecg = st.sidebar.selectbox('ЭКГ в покое', ['Нормальный', 'ST', 'LVH'])
        max_hr = st.sidebar.slider('Максимальная частота сердечных сокращений', 0, 200, 150)
        exercise_angina = st.sidebar.selectbox('Стенокардия, вызванная физической нагрузкой', ['Нет', 'Да'])
        oldpeak = st.sidebar.slider('Oldpeak', 0.0, 10.0, 1.0)
        st_slope = st.sidebar.selectbox('Наклон ST', ['Вверх', 'Плоский', 'Вниз'])

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
    st.subheader('Параметры ввода пользователя')
    st.write(input_df)

    # Предсказание
    if st.button('Предсказать'):
        prediction = model.predict(input_df)
        st.subheader('Предсказание')
        st.write(f'Предсказание: {"Сердечное заболевание" if prediction[0] == 1 else "Нет сердечного заболевания"}')

if __name__ == '__main__':
    main()
