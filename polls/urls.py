
from django.urls import include, path
from . import views
# ../apis/+
urlpatterns = [
    path('psnSubmitUser', views.psnSubmitUser),
    path('entSubmitUser', views.entSubmitUser),
    path('login', views.login),
]
