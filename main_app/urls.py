from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('sauces/', views.sauces_index, name='index'),
    path('sauces/<int:sauce_id>/', views.sauces_detail, name='detail'),
    path('sauces/create/', views.SauceCreate.as_view(), name='sauces_create'),
    path('sauces/<int:pk>/update/', views.SauceUpdate.as_view(), name='sauces_update'),
    path('sauces/<int:pk>/delete/', views.SauceDelete.as_view(), name='sauces_delete'),
    path('sauces/<int:sauce_id>/add_stock/', views.add_stock, name='add_stock'), 
    path('sauces/<int:sauce_id>/assoc_dish/<int:dish_id>/', views.assoc_dish, name='assoc_dish'),
    path('sauces/<int:sauce_id>/unassoc_dish/<int:dish_id>/', views.unassoc_dish, name='unassoc_dish'),
    path('dishes/', views.DishList.as_view(), name='dishes_index'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dishes_detail'),
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
]
