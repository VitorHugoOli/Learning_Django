from .views import home, my_logout
from django.urls import path



urlpatterns = [
    path('',home,name="home"),
    path('logout',my_logout,name="logout")
]
