from django.shortcuts import render
import pandas as pd
import joblib
from .forms import PredictionForm


# Load model
model = joblib.load("C:/Users/User/Documents/Rayhan/AI/titanic/titanic/predictions/titanic_model.joblib")


def preprocess_data(data):
    # Mengonversi gender menjadi angka (0: male, 1: female)
    data['Sex'] = 0 if data['gender'] == 'male' else 1
    
    # Memetakan 'pclass' ke dalam bentuk integer
    data['Pclass'] = int(data['pclass'])
    
    # Mengubah 'age' dan 'fare' menjadi format numerik
    data['Age'] = data['age']  # pastikan menggunakan 'age' dari form
    data['Fare'] = data['fare']  # pastikan menggunakan 'fare' dari form

    # Menambahkan nilai untuk kolom lain yang diperlukan
    data['FamilySize'] = 1  # Asumsi, karena tidak ada data untuk sibsp atau parch
    data['CabinKnown'] = 0  # Asumsi, karena tidak ada data untuk cabin
    
    # Membuat kolom Embarked yang sesuai, gunakan asumsi untuk form
    data['Embarked_Q'] = 0  # Asumsi, jika tidak ada data Embarked dari form
    data['Embarked_S'] = 0  # Asumsi, jika tidak ada data Embarked dari form

    # Menyiapkan dataframe dengan fitur yang diperlukan
    features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'CabinKnown', 'Embarked_Q', 'Embarked_S']
    
    # Membuat dataframe baru untuk prediksi
    processed_data = pd.DataFrame([data], columns=features)
    return processed_data


# Fungsi untuk prediksi
def predict_survival(request):
    prediction = None  # Inisialisasi variabel prediction dengan nilai None
    
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # Proses data sebelum dimasukkan ke dalam model
            processed_data = preprocess_data(data)
            
            # Prediksi menggunakan model
            prediction = model.predict(processed_data)
            
            # Menampilkan hasil prediksi
            prediction_result = "Alhamdulillah Selamat Coyy 😁" if prediction[0] == 1 else "Hello World!😂"
            return render(request, 'predict.html', {'form': form, 'prediction': prediction_result})
    
    else:
        form = PredictionForm()
    
    return render(request, 'predict.html', {'form': form, 'prediction': prediction})
