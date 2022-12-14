import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse
from .models import Sauce, Dish, Photo
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

def add_photo(request, sauce_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to sauce_id or sauce (if you have a sauce object)
            Photo.objects.create(url=url, sauce_id=sauce_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
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