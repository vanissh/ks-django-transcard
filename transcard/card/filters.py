import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *

class CardFilter(django_filters.FilterSet):
	inn = NumberFilter(field_name='inn', lookup_expr='icontains')


	class Meta:
		model = Card
		fields = ['inn']
		exclude = ['customer', 'date_created', 'photo']
  