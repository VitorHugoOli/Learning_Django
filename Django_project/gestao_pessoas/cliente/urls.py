
from django.urls import path
from .views import person_list, person_new, person_del, person_up

urlpatterns = [
    path('list/',person_list,name="nick_list"),
    path('new/',person_new, name="nick_new"),
    path('update/<int:id>',person_up, name="nick_up"),
    path('delete/<int:id>',person_del, name="nick_del"),
]
