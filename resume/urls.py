from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
]
