from django.shortcuts import render, redirect
import telebot
from django.core.mail import send_mail

from .models import Portfolio
from .forms import ApplicationForm


bot = telebot.TeleBot('1448262304:AAERxXKIKzFhF_RWPsDYtjXF3XMwXqhWAPE')


def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio/index.html', {'portfolio': portfolio})


def contact_page(request):
    return render(request, 'portfolio/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            subject = 'Новое сообщение на сайте портфолио!'
            to_email = ['initmenthor@gmail.com',]
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            msg = f'Имя: {name} \nПочта: {mail} \nСообщение: {message}'
            send_mail(subject, message, mail, to_email, fail_silently=False)
            bot.send_message(959339948, msg)
    return redirect('home')
