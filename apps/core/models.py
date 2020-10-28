from django.db import models
from datetime import date

from apps.course.models import Course

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.SET_NULL, blank=True, null=True)

    text = models.CharField(max_length=200)
    rating = models.CharField(default='positive', max_length=10)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.text[0:20]
