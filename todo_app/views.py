from rest_framework import viewsets, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    """CRUD for tasks. Only authenticated users may access, and they only see their tasks."""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['completed', 'priority', 'due_date']

    def get_queryset(self):
        # Limit tasks to the requesting user for privacy
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Attach the logged-in user automatically when creating a task
        serializer.save(user=self.request.user)
