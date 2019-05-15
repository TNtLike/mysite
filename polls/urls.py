
from django.urls import include, path
from . import views
# ../apis/+  接口
urlpatterns = [
    path('loginOut', views.loginOut),
]
