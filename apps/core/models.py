from django.db import models
from datetime import date

class Comment(models.Model):
    text = models.CharField(max_length=200)
    rating = models.CharField(default='positive', max_length=10)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.text[0:20]
