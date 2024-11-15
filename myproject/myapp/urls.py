from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('data/', views.data, name='data'),  # Маршрут для страницы data
    path('test/', views.test, name='test'),  # Маршрут для страницы test
]
