from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('inspirations/', views.inspirations_index, name='index'),
    path('inspirations/<int:inspiration_id>/', views.inspirations_detail, name='detail'),
]