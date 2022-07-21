from django.urls import path
from . import views
from .views import UserCity

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_page, name='login'),
    path('', views.logout_user, name='logout'),
    path('city/',  UserCity.as_view(), name='city')

]

