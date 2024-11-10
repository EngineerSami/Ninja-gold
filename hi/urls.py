# ninja_gold/urls.py
from django.contrib import admin
from django.urls import path
from hi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gold, name='gold'),
    path('process_money', views.process_money, name='process_money'),
]
