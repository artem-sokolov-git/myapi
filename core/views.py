from rest_framework import generics

# from rest_framework.renderers import JSONRenderer
from .models import Task
from .serializers import TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # renderer_classes = [JSONRenderer]


class TaskListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # renderer_classes = [JSONRenderer]
