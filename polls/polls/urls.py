from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.index,name = 'index' ),
    path('<int:question_id>/',views.question,name = 'details' ),
    path('<int:question_id>/vote/',views.vote,name = 'vote' ),
   path('<int:question_id>/results/',views.result,name = 'results' ),
    
]