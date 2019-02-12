
from django.urls import include, path
from . import views
# ../polls/+
urlpatterns = [
    path('submitUser', views.submitUser),
    path('login', views.login),
    path('test', views.test),
    path('test2', views.test2),
]
