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

def check_inn(request):
	msg = ''
	if request.method == 'POST':
		form = forms.InnForm(request.POST, request.FILES)
		if form.is_valid():
			models.Ready_inn.objects.all().delete()
			form.save()
	elif request.method == 'GET':
		query = request.GET.get('inn')
		path = models.Ready_inn.objects.all()
		if path.count() > 0:
			path = path[0].excel
			if query:
				msg = 'Ваша карта не готова'
				if cron.check_inn(query, path):
					msg = 'Ваша карта готова'

	form = forms.InnForm()

	context = {
		'form': form,
		'message': msg,
		}

	return render(request, 'ready_inn.html', context)
	

def generate_loadout(request):
	cron.MyCronJob()
	context = {}
	return HttpResponseRedirect('/./admin/')
