
from django.urls import path
from .views import person_list, person_new

urlpatterns = [
    path('list/',person_list,name="nick_list"),
    path('new/',person_new, name="nick_new"),
    path('update/<int:id>',person_up, name="nick_up"),
]
