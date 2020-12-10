from django.urls import path
from .views import *


urlpatterns =[
    path('', index, name='home'),
    path('contact_page/', contact_page, name='contact_page'),
    path('contact/', contact, name='contact'),
]
