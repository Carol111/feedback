from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Comment
from ..course.models import Course
from .forms import CommentForm

import pickle

def about(request):
    return render(request, 'core/about.html')

def home(request):
    form = CommentForm()
    success = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        invalid = {}


        if form.is_valid():
            comment = [form.data['text']]

            classifier_multi_NB = pickle.load(open('classifier/classifier_multi_NB.sav','rb'))
            vectorizer = pickle.load(open('classifier/vectorizer.sav','rb'))

            processed_comment = vectorizer.transform(comment)
            comment_rating = classifier_multi_NB.predict(processed_comment)

            new_comment = Comment(
                text = comment[0],
                course = Course.objects.get(code=form.data['course']),
                rating = comment_rating[0]
            )

            new_comment.save()
            success = True

    return render(request, 'core/home.html', {'form': form, 'success': success})
