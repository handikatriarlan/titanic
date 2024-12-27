from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_survival, name='predict_survival'),
]
