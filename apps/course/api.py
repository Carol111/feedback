import json

from django.http import JsonResponse

from .models import Course
from ..core.models import Comment

def api_date_range(request):
    data = json.loads(request.body)

    comments = Comment.objects.filter(course__code=data['course_code'])

    comments = comments.filter(date__range=[data['start_date'], data['end_date']])

    positive_comments = comments.filter(rating='positive').count()
    negative_comments = comments.filter(rating='negative').count()

    context = {
        'positive_comments_by_range': positive_comments,
        'negative_comments_by_range': negative_comments
    }

    return JsonResponse(context)

def api_remove_course(request):
    data = json.loads(request.body)

    course = Course.objects.get(code=data['course_code'])

    course.delete()

    return JsonResponse({'success': True})
