from django.contrib import admin

from .models import Comment
from ..period.models import Period
from ..course.models import Course

admin.site.register(Comment)
admin.site.register(Period)
admin.site.register(Course)
