# Heart Disease Predictor

https://dashonokok-heart-disease-predictor-strealit-app-5ot5jh.streamlit.app/

## Описание
Heart Disease Predictor — это инструмент для предсказания сердечных заболеваний на основе различных медицинских параметров. Проект использует модель машинного обучения CatBoost, обученную на предобработанных данных, и предоставляет простой интерфейс для ввода данных пользователем и получения предсказаний.

## Установка

### Требования
- Python 3.8 или выше
- Библиотеки: `pandas`, `scikit-learn`, `catboost`, `streamlit`, `joblib`

### Установка библиотек
Установите необходимые библиотеки с помощью следующей команды:
```sh
pip install pandas scikit-learn catboost streamlit joblib

Использование
Обучение модели
Для обучения модели CatBoost выполните следующую команду:

python train_model.py
Этот скрипт загрузит данные, обучит модель и сохранит её в файл best_model.pkl.


Запуск Streamlit приложения
Для запуска Streamlit приложения выполните следующую команду:

streamlit run app.py
Этот скрипт запустит веб-интерфейс, где пользователь может ввести необходимые данные и получить предсказание.

![Снимок экрана от 2025-01-23 08-38-10](https://github.com/user-attachments/assets/8fba0ef2-5c44-4163-b806-4953391ee123)
![Снимок экрана от 2025-01-23 08-38-26](https://github.com/user-attachments/assets/e820d125-2efc-41e0-8a28-322642758ade)
