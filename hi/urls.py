from django.urls import path
from .views import user_list, add_user

urlpatterns = [
    path('', user_list, name='index'),
    path('add_user', add_user, name='add_user'),
]