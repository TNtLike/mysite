
from django.urls import include, path
from . import views
# ../apis/+  接口
urlpatterns = [
    path('psnSubmitUser', views.psnSubmitUser),
    path('entSubmitUser', views.entSubmitUser),
    path('psnLogin', views.psnLogin),
    path('entLogin', views.entLogin),
    path('entBaseInfoSub', views.entBaseInfoSub),
    path('loginOut', views.loginOut),
    path('getPsnResumeInfo', views.getPsnResumeInfo),
    path('subPsnBaseInfo', views.subPsnBaseInfo),
    path('subPsnProjectInfo', views.subPsnProjectInfo)
]
