from django.urls import path
from .views import TaskListCreate, TaskListUpdate

urlpatterns = [
    path("tasks/", TaskListCreate.as_view(), name="task-list-create"),
    path("tasks/<int:pk>", TaskListUpdate.as_view(), name="task-detail"),
]
