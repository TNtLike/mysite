
from django.urls import include, path
from . import views
from . import views2
# ../polls/+
urlpatterns = [
    path('submitUser', views.submitUser),
    path('login', views.login),
    path('test', views.test),
    path('test2', views2.test2),
    path('test3', views.test3),
    path('test4', views.test4),
]
