from django import forms

class PredictionForm(forms.Form):
    age = forms.IntegerField(
        label="Usia",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "Usia", "class": "form-control"})
    )
    gender = forms.ChoiceField(
        label="Jenis Kelamin",
        choices=[('male', 'Pria'), ('female', 'Wanita')],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    pclass = forms.ChoiceField(
        label="Kelas",
        choices=[(1, 'Pertama'), (2, 'Kedua'), (3, 'Ketiga')],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    fare = forms.FloatField(
        label="Harga Tiket",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "Harga Tiker Anda", "class": "form-control"})
    )
    familysize = forms.IntegerField(
        label="Ukuran Keluarga",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "Ukuran Keluarga Anda", "class": "form-control"})
    )
    cabinknown = forms.ChoiceField(
        label="Kabin Penumpang",
        choices=[(0, 'Tidak Diketahui'), (1, 'Diketahui')],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    embarked_q = forms.ChoiceField(
        label="Tiba di Queenstown (Q)",
        choices=[(0, 'Tidak'), (1, 'Ya')],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    embarked_s = forms.ChoiceField(
        label="Tiba di Southampton (S)",
        choices=[(0, 'Tidak'), (1, 'Ya')],
        widget=forms.Select(attrs={"class": "form-control"})
    )
