
from django.urls import include, path
from . import views
from . import testdb

urlpatterns = [

    path('', views.index, name='index'),
    path('hello/', views.polls, name='hello'),
    path('polls/testdb/', testdb.insert),
    path('polls/show/',testdb.show),
    path('testVuejsandDjango', views.testVue)
]