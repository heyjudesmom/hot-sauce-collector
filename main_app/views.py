from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse
from .models import Sauce, Dish
from .forms import StockForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sauces_index(request):
    sauces = Sauce.objects.all()
    return render(request, 'sauces/index.html', {'sauces': sauces})

def sauces_detail(request, sauce_id):
    sauce = Sauce.objects.get(id=sauce_id)
    id_list = sauce.dishes.all().values_list('id')
    dishes_sauce_doesnt_have = Dish.objects.exclude(id__in=id_list)
    stock_form = StockForm()
    return render(request, 'sauces/detail.html', { 
        'sauce': sauce, 
        'stock_form': stock_form, 
        'dishes': dishes_sauce_doesnt_have
        })

def add_stock(request, sauce_id):
    form = StockForm(request.POST)
    if form.is_valid():
        new_stock = form.save(commit=False)
        new_stock.sauce_id = sauce_id
        new_stock.save()
    return redirect('detail', sauce_id=sauce_id)

def assoc_dish(request, sauce_id, dish_id):
    Sauce.objects.get(id=sauce_id).dishes.add(dish_id)
    return redirect('detail', sauce_id=sauce_id)

def unassoc_dish(request, sauce_id, dish_id):
    Sauce.objects.get(id=sauce_id).dishes.remove(dish_id)
    return redirect('detail', sauce_id=sauce_id)


class SauceCreate(CreateView):
    model = Sauce
    fields = ['name', 'region', 'notable_ingredients', 'scoville_scale']

class SauceUpdate(UpdateView):
    model = Sauce
    fields = ['region', 'notable_ingredients', 'scoville_scale']

class SauceDelete(DeleteView):
    model = Sauce
    success_url = '/sauces/'

class DishList(ListView):
  model = Dish

class DishDetail(DetailView):
  model = Dish

class DishCreate(CreateView):
  model = Dish
  fields = '__all__'

class DishUpdate(UpdateView):
  model = Dish
  fields = ['name', 'meal']

class DishDelete(DeleteView):
  model = Dish
  success_url = '/dishes/'