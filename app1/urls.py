from django.urls import path
from .views import *
app_name='app1'
urlpatterns=[
    path('',home,name='home'),
    path('gift/',gift,name='gift'),
    path('pro/',pro,name='pro'),
    path('learn/',learn,name='learn'),
    path('profile/',profile,name='profile'),
    path('setting/',setting,name='setting'),
    path('courses/',courses,name='courses'),
    path('find/',find,name='find'),
]