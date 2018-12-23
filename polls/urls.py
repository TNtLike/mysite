
from django.urls import include, path
from . import views
from . import testdb
# ../polls/+
urlpatterns = [

    path('', views.index, name='index'),
    path('hello', views.polls, name='hello'),
    # path('testdb/insert', views.db_add),
    # path('testdb/show', views.db_show),
    path('getData', views.getData),
    path('returnData', views.returnData)
]
