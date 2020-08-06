
from django.urls import include, path
from ..views import views
# ../apis/+  接口
urlpatterns = [
    path('loginOut', views.loginOut),
    path('searchJob', views.searchJob),
    path('searchPsn', views.searchPsn),
    path('getAccountInfo', views.getAccountInfo),
    path('subAccountInfo', views.subAccountInfo),
    path('sendResume', views.sendResume),
    path('getSentJob', views.getSentJob),
    path('closeSent', views.closeSent),
    path('passSent', views.passSent),
    path('delSent', views.delSent)

]
