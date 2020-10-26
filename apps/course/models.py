from django.db import models

from apps.period.models import Period

class Course(models.Model):
    period = models.ForeignKey(Period, related_name='courses', on_delete=models.SET_NULL, blank=True, null=True)

    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    tags = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
