from django.shortcuts import render
from .models import Comment
from datetime import date

import pickle

def home(request):
    return render(request, 'core/home.html')

def classifier(courseCode, comment):
    classifier_multi_NB = pickle.load(open('classifier/classifier_multi_NB.sav','rb'))
    vectorizer = pickle.load(open('classifier/vectorizer.sav','rb'))

    processed_comment = vectorizer.transform(comment)
    comment_rating = classifier_multi_NB.predict(processed_comment)

    new_comment = Comment(
        text = comment[0],
        rating = comment_rating[0]
    )

    new_comment.save()
    return
