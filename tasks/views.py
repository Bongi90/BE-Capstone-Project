from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.is_completed = True
        task.save()
        return Response({"message": "Task marked as completed!"})

    @action(detail=True, methods=['post'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.is_completed = False
        task.save()
        return Response({"message": "Task marked as incomplete!"})
