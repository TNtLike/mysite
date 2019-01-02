
from django.urls import include, path
from . import views
# ../polls/+
urlpatterns = [
    path('getData', views.getData),
    path('returnData', views.returnData),
    path('returnSingleData', views.returnSingleData),
    path('deleteData', views.deleteData)
]
