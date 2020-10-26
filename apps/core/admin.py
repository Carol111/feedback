from django.contrib import admin

from .models import Comment
from ..period.models import Period

admin.site.register(Comment)

admin.site.register(Period)
