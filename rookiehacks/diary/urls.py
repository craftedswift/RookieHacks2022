from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'diary-home'),
    path('about/', views.about, name = 'diary-about'),
    path("api/journal", views.add_report, name ="add_report"),
]