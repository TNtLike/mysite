
from django.urls import include, path
from . import views
from . import testdb

urlpatterns = [

    path('polls/', views.index, name='index'),
    path('polls/hello/', views.polls, name='hello'),
    path('polls/testdb/', testdb.insert),
    path('polls/show/',testdb.show)
]