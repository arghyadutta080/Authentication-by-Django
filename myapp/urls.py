from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'), 
    path('logout', views.logoutPage, name='logout')
]