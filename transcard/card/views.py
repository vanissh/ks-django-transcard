from django.shortcuts import render, HttpResponseRedirect

from . import forms
from . import models
from . import cron
from . import filters

def index(request):
	err = ''
	if request.method == 'POST':
		form = forms.CardForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		else:
			err = 'Форма введена неверно'

	form = forms.CardForm()

	context = {
    		'form': form,
		'error': err,
    	}

	return render(request, 'index.html', context) 

def card(request):
	cards = models.Card.objects.all()

	order_count = cards.count()

	myFilter =  filters.CardFilter(request.GET, queryset=cards)
	cards = myFilter.qs 

	context = {'cards':cards, 'myFilter':myFilter}
	return render(request, 'list.html', context)

def generate_loadout(request):
	cron.MyCronJob()
	context = {}
	return HttpResponseRedirect('/./admin/')
