from django.shortcuts import render
# from django.http import HttpResponse
from .models import Sauce

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
    return render(request, 'sauces/detail.html', { 'sauce': sauce })
