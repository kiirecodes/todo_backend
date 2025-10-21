from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Represents a task owned by a single user.

    Fields:
    - user: FK to Django user so every item is private to its owner.
    - title, description: core metadata.
    - completed: boolean for status.
    - priority: small controlled choice set to help filtering.
    - due_date: optional deadline that can be used for sorting/filters.
    - created_at: auto timestamp for ordering and analytics.
    """
    PRIORITY_CHOICES = [('Low','Low'),('Medium','Medium'),('High','High')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # integer ordering field used by the frontend for manual ordering
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({'✓' if self.completed else ' '})"
