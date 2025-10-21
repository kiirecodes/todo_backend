from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Serialize Task for API. user field is read-only (set on server)."""
    class Meta:
        model = Task
        # Explicit fields so it's clear for reviewers
        fields = ['id','user','title','description','completed','priority','due_date','created_at','order']
        read_only_fields = ['id','user','created_at']
