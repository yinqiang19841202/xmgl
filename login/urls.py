from django.contrib import admin
from django.urls import path,include
from login import views
app_name = 'login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('logout/', views.logout,name='logout'),
    path('captcha/', include('captcha.urls')),



]