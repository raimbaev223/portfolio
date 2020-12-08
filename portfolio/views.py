from django.shortcuts import render
from .models import Portfolio
# Create your views here.


def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio/index.html', {'portfolio': portfolio})

