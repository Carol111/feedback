from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm
from ..core.models import Comment

@login_required
def list_course(request):
    courses = Course.objects.filter(user=request.user).order_by('title').values()

    for course in courses:
        comments = Comment.objects.filter(course__code=course['code'])
        course['comments'] = comments.count()
        positive_comments = comments.filter(rating='positive').count()
        negative_comments = comments.filter(rating='negative').count()
        course_rating = 'positive' if positive_comments >= negative_comments else 'negative'
        course['rating'] = course_rating

    return render(request, 'course/list.html', {'courses':courses})

@login_required
def add_course(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        print (form)

        if form.is_valid():
            new_course = Course(
                user=request.user,
                title = form.data['title'],
                code = form.data['code'],
            )
            new_course.save()

            return redirect('add_course')

    return render(request, 'course/add.html', {'form':form})
