from django.shortcuts import render
import pandas as pd
import joblib
import os
from .forms import PredictionForm


# Load model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, 'titanic', 'predictions', 'titanic_model.joblib')
model = joblib.load(MODEL_PATH)

def preprocess_data(data):
    # Mengonversi gender menjadi angka (0: male, 1: female)
    data['Sex'] = 0 if data['gender'] == 'male' else 1
    
    # Memetakan 'pclass' ke dalam bentuk integer
    data['Pclass'] = int(data['pclass'])
    
    # Mengubah 'age' dan 'fare' menjadi format numerik
    data['Age'] = float(data['age'])
    data['Fare'] = float(data['fare'])

    # Kolom tambahan dari form
    data['FamilySize'] = int(data['familysize'])
    data['CabinKnown'] = int(data['cabinknown'])
    data['Embarked_Q'] = int(data['embarked_q'])
    data['Embarked_S'] = int(data['embarked_s'])

    # Menyiapkan dataframe dengan fitur yang diperlukan
    features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'CabinKnown', 'Embarked_Q', 'Embarked_S']
    processed_data = pd.DataFrame([data], columns=features)
    
    return processed_data



def predict_survival(request):
    prediction = None
    data = None  # Untuk menyimpan data yang diinputkan

    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                
                # Proses data sebelum dimasukkan ke dalam model
                processed_data = preprocess_data(data)
                
                # Prediksi menggunakan model
                prediction = model.predict(processed_data)
                
                # Menampilkan hasil prediksi
                prediction_result = "Alhamdulillah Selamat Coyy 😁" if prediction[0] == 1 else "Hello World!😂"
            except Exception as e:
                prediction_result = f"An error occurred: {str(e)}"
            
            return render(request, 'predict.html', {'form': form, 'prediction': prediction_result, 'data': data})
    else:
        form = PredictionForm()
    
    return render(request, 'predict.html', {'form': form, 'prediction': prediction, 'data': data})
