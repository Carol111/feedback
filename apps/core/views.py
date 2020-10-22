from django.shortcuts import render

import pickle

def home(request):
    return render(request, 'core/home.html')

def classifier(courseCode, comment):
    classifier_multi_NB = pickle.load(open('classifier/classifier_multi_NB.sav','rb'))
    vectorizer = pickle.load(open('classifier/vectorizer.sav','rb'))

    processed_comment = vectorizer.transform(comment)
    comment_class = classifier_multi_NB.predict(processed_comment)
    return
