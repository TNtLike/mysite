
from django.urls import include, path
from . import views_ent
# ../apis/ent+  接口
urlpatterns = [
    path('entSubmitUser', views_ent.entSubmitUser),
    path('entLogin', views_ent.entLogin),
    path('subEntBaseInfo', views_ent.subEntBaseInfo),
    path('subEntJobInfo', views_ent.subEntJobInfo),
]
