import json

from django.http import JsonResponse

from .models import Comment
from .views import classifier

def api_classifier(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    comment = data['comment']
    courseCode = data['courseCode']

    classifier(courseCode=courseCode, comment=comment)

    return JsonResponse(jsonresponse)
