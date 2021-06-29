from django import forms

from . import models


class CardForm(forms.ModelForm):
	class Meta:
		model = models.Card
		fields = ['type', 'reason', 'inn', 'name', 'surname', 'photo']

		widgets = {
			'type': forms.Select(choices=(('Школьная', 'Школьная'), ('Студенческая', 'Студенческая'))),
			'reason': forms.Select(choices=(('Утеря', 'Утеря'), ('Ручная', 'Ручная'))),
		}
