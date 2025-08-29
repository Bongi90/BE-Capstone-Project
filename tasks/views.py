from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['POST'])
def mark_task_complete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        return Response({"message": "Task marked as completed!"})
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)


@api_view(['POST'])
def mark_task_incomplete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.is_completed = False
        task.save()
        return Response({"message": "Task marked as incomplete!"})
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)
