
from django.urls import include, path
from . import views_psn
# ../apis/+  接口
urlpatterns = [
    path('psnSubmitUser', views_psn.psnSubmitUser),
    path('psnLogin', views_psn.psnLogin),
    path('getPsnResumeInfo', views_psn.getPsnResumeInfo),
    path('subPsnBaseInfo', views_psn.subPsnBaseInfo),
    path('subPsnProjectInfo', views_psn.subPsnProjectInfo),
    path('delPsnProjectInfo', views_psn.delPsnProjectInfo),


]
