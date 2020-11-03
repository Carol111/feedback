from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm

@login_required
def list_course(request):
	courses = Course.objects.filter(user=request.user).order_by('title')

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
