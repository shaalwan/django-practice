from django.urls import path
from . import views

app = 'portfolio'
urlpatterns = [
    path('',views.project,name = 'home'),
]
