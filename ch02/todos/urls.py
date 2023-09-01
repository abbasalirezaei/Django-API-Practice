# todos/urls.py
from django.urls import path
from .views import DetailTodoAPIView, ListTodoAPIView

urlpatterns = [
    path("<int:pk>/", DetailTodoAPIView.as_view(), name="todo_detail"),
    path("", ListTodoAPIView.as_view(), name="todo_list"),
]