from django.urls import path
from . import views

app = 'blog'
urlpatterns = [
    path('',views.blog,name = 'blog'),
]
