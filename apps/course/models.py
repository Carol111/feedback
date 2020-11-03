from django.db import models

from django.contrib.auth.models import User

class Course(models.Model):
    user = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE, default='')

    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
