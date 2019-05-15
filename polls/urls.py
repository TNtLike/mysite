
from django.urls import include, path
from . import views
# ../apis/+  接口
urlpatterns = [
    # path('psnSubmitUser', views.psnObj.psnSubmitUser),
    # path('psnLogin', views.psnObj.psnLogin),
    # path('getPsnResumeInfo', views.psnObj.getPsnResumeInfo),
    # path('subPsnBaseInfo', views.psnObj.subPsnBaseInfo),
    # path('subPsnProjectInfo', views.psnObj.subPsnProjectInfo),
    # path('delPsnProjectInfo', views.psnObj.delPsnProjectInfo),
    # path('entSubmitUser', views.entObj.entSubmitUser),
    # path('entLogin', views.entObj.entLogin),
    # path('entBaseInfoSub', views.entObj.entBaseInfoSub),
    path('loginOut', views.loginOut),


]
