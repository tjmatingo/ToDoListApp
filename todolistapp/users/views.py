from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from .models import Todo
# Create your views here.


def home(response):
    todo_items = Todo.objects.all().order_by('-added_date')
    length_of_todos = Todo.objects.all().count()
    return render(response, 'users/home.html', {'todo_items': todo_items, 'length_of_todos': length_of_todos})

def add_todo(response):
    current_date = timezone.now()
    content = response.POST['content']
    created_todo = Todo.objects.create(added_date=current_date, text=content)
    return redirect('/')

def delete_todo(response, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')

