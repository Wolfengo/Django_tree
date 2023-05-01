from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<path:menu_name>/', views.menu, name='menu'),
]
