from django.urls import path
from home.views import home,contact,about,stories,recipes

urlpatterns=[
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('stories/',stories,name='stories'),
    path('recipes/',recipes,name='recipes')
]