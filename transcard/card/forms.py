from django import forms

from . import models


class CardForm(forms.ModelForm):
	class Meta:
		model = models.Card
		fields = ['type', 'reason', 'inn', 'name', 'surname', 'photo', 'phone', 'pay_method',]

		widgets = {
			'type': forms.Select(choices=(('Школьная', 'Школьная'), ('Студенческая', 'Студенческая'))),
			'reason': forms.Select(choices=(('Утеря', 'Утеря'), ('Ручная', 'Ручная'))),
			'pay_method' : forms.Select(choices=[('Нал', 'Нал'),('Чек', 'Чек'),('Каспи', 'Каспи')]),
			'inn'   : forms.TextInput(attrs={
	   			'size': '12',
				'pattern': '.{12}',
				'title' :'В ИНН должно быть 12 символов',
		  	}),
			'photo' : forms.FileInput(attrs={
				'required':'',
				
			})
		}
  
class InnForm(forms.ModelForm):
	class Meta:
		model = models.Ready_inn
		fields = ['excel', 'inn',]

		widgets = {
			'inn'   : forms.TextInput(attrs={
	   			'size': '12',
				'pattern': '.{12}',
				'title' :'В ИНН должно быть 12 символов',
		  	}),
		}
