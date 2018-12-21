
from django.urls import include, path
from . import views

urlpatterns = [

    path('polls/', views.index, name='index'),
    path('polls/hello/', views.polls, name='hello'),
]
