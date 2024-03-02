from django.forms import ModelForm
from .models import House

class NewUnit(ModelForm):
	class Meta:
		model = House
		fields = '__all__'


class SoldUnit(ModelForm):
	class Meta:
		model = House
		fields = ['booked','sold']		