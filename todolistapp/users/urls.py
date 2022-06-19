from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
]