from django.shortcuts import render

from . import forms
from . import models

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
    	"form": form,
		'error': err,
    }
 
	return render(request, 'index.html', context) 
