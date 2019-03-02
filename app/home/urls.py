from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('add/', views.add_bot, name='add'),
]
