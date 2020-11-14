from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm
from ..core.models import Comment
from .stopwords import STOPWORDS

import pandas as pd
import datetime
import json

@login_required
def list_course(request):
    courses = Course.objects.filter(user=request.user).order_by('title').values()
    empty_list = not bool(courses.count())

    for course in courses:
        comments = Comment.objects.filter(course__code=course['code'])
        course['comments'] = comments.count()
        course['plural'] = course['comments'] != 1
        positive_comments = comments.filter(rating='positive').count()
        negative_comments = comments.filter(rating='negative').count()
        course_rating = 'positive' if positive_comments >= negative_comments else 'negative'
        course['rating'] = course_rating

    return render(request, 'course/list.html', {'courses':courses, 'empty_list':empty_list})

@login_required
def add_course(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            new_course = Course(
                user=request.user,
                title = form.data['title'],
                code = form.data['code'],
            )
            new_course.save()

            return redirect('add_course')

    return render(request, 'course/add.html', {'form':form})

@login_required
def course_overview(request, course_code):
    courses = Course.objects.filter(user=request.user)
    course = get_object_or_404(courses, code=course_code)

    comments = Comment.objects.filter(course__code=course_code)

    positive_comments = comments.filter(rating='positive')
    negative_comments = comments.filter(rating='negative')

    count_positive_comments = positive_comments.count()
    count_negative_comments = negative_comments.count()

    date_range = course.created_at.strftime('%d/%m/%Y') + ' - ' + datetime.datetime.now().strftime('%d/%m/%Y')

    period = pd.date_range(start=course.created_at.date(), end=datetime.datetime.now().date(), freq='D')

    linear_positive_series = []
    linear_negative_series = []
    linear_label = []

    for day in period:
        linear_positive_series.append(positive_comments.filter(date=day).count())
        linear_negative_series.append(negative_comments.filter(date=day).count())
        linear_label.append(day.strftime('%d/%m'))

    frequent_words = ''

    for comment in comments:
        frequent_words += ' ' + comment.text.lower()

    context = {
        'course': course,
        'count_positive_comments': count_positive_comments,
        'count_negative_comments': count_negative_comments,
        'date_range': date_range,
        'linear_dataset': {
            'linear_label': json.dumps(linear_label),
            'linear_positive_series': linear_positive_series,
            'linear_negative_series': linear_negative_series
        },
        'word_cloud_dataset': {
            'frequent_words': frequent_words,
            'stopwords': json.dumps(STOPWORDS)
        }
    }

    return render(request, 'course/overview.html', context)

@login_required
def course_messages(request, course_code):
    course = Course.objects.get(code=course_code)
    comments = Comment.objects.filter(course__code=course_code)

    return render(request, 'course/messages.html', {'course':course, 'comments':comments})

@login_required
def course_frequent_words(request, course_code):
    course = Course.objects.get(code=course_code)

    return render(request, 'course/frequent-words.html', {'course':course})
