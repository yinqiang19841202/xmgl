from django.contrib import admin
from django.urls import path,include
from xmgl import views
app_name = 'xmgl'
urlpatterns = [

    path('', views.xmgl,name='xmgl'),
    path('xmgl_add/',views.xmgl_add,name='xmgl_add'),
    path('yinq/', views.yinq,name='yinq'),

]