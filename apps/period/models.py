from django.db import models
from django.contrib.auth.models import User

class Period(models.Model):
    user = models.ForeignKey(User, related_name='periods', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
