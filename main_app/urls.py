from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('sauces/', views.sauces_index, name='index'),
    path('sauces/<int:sauce_id>/', views.sauces_detail, name='detail'),
]
