from django import forms

class PredictionForm(forms.Form):
    age = forms.FloatField(label="Age", min_value=0)
    gender = forms.ChoiceField(label="Gender", choices=[('male', 'Male'), ('female', 'Female')])
    pclass = forms.ChoiceField(label="Class", choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third')])
    fare = forms.FloatField(label="Fare", min_value=0)
