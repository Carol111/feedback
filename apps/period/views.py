from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Period
from .forms import PeriodForm

@login_required
def list_period(request):
	periods = Period.objects.filter(user=request.user).order_by('title')

	return render(request, 'period/list.html', {'periods':periods})

@login_required
def add_period(request):
	if request.method == 'POST':
		form = PeriodForm(request.POST)

		if form.is_valid():
			period = Period(title=form['title'].value(), user=request.user)

			period.save()

			return redirect('add_period')

	form = PeriodForm()

	return render(request, 'period/add.html', {'form':form})
