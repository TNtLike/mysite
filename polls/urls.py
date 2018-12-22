
from django.urls import include, path
from . import views
from . import testdb

urlpatterns = [

    path('', views.index, name='index'),
    path('hello/', views.polls, name='hello'),
    path('testdb/', testdb.insert),
    path('show/',testdb.show),
    path('testVuejsandDjango', views.testVue)
]