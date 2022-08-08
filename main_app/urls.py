from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('sauces/', views.sauces_index, name='index'),
    path('sauces/<int:sauce_id>/', views.sauces_detail, name='detail'),
    path('sauces/create/', views.SauceCreate.as_view(), name='sauces_create'),
    path('sauces/<int:pk>/update', views.SauceUpdate.as_view(), name='sauces_update'),
    path('sauces/<int:pk>/delete', views.SauceDelete.as_view(), name='sauces_delete'),
]
