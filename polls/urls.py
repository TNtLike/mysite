
from django.urls import include, path
from . import views
# ../apis/+
urlpatterns = [
    path('psnSubmitUser', views.psnSubmitUser),
    path('entSubmitUser', views.entSubmitUser),
    path('psnLogin', views.psnLogin),
    path('entLogin', views.entLogin),
]
