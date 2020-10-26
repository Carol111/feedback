from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from ..period.models import Period
from .forms import CourseForm

@login_required
def list_course(request):
	courses = Course.objects.filter(period__user=request.user).order_by('title')

	return render(request, 'course/list.html', {'courses':courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('add_course')

    form = CourseForm()
    form.fields['period'].queryset = Period.objects.filter(user=request.user).order_by('title')

    return render(request, 'course/add.html', {'form':form})
