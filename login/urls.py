#conding=utf-8


from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index_view, name="login"),
    path('register/',views.register_view, name="register"),
    path('logout/', views.logout, name='logout'),
    path('user/',views.user_view, name="user")
]