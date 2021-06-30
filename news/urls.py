# coding=utf-8
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:new_id>', views.detail, name='detail'),
    path('search_news/<int:num>', views.find_new, name='search_news'),
    path('inlandnews/<int:num>', views.inlandnews, name='inland'),
    path('outlandnews/<int:num>', views.outlandnews, name='outland'),
    path('hotspotnews/<int:num>', views.hotspotnews, name='hotspot'),
]