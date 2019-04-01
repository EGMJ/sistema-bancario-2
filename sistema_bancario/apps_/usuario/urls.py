from django.urls import path
from .views import registroView, loginView, codigoView, homeView

urlpatterns = [
	path('login', loginView, name = 'login'),
    path('registro', registroView, name='registro'),
    path('codigo', codigoView, name='codigo'),
    path('home', homeView, name='home'),
]
