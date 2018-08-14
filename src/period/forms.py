from django import forms

# from restaurants.models import RestaurantLocation

from django.conf import settings

from .models import Period

User = settings.AUTH_USER_MODEL

class PeriodForm(forms.ModelForm):

	perioddesc = forms.CharField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter name here',
				}
			))

	# startdate = forms.DateField(
 #        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
 #                                       "pickTime": False})),

	startdate = forms.DateField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter start date here',
					'type' : 'Date',
				}
			))
	enddate = forms.DateField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter end date here',
					'type' : 'Date',					
				}
			))

	class Meta:
		model = Period
		fields = [
			'perioddesc',
			'startdate',
			'enddate',
		]			

	def __init__(self, user=None, *args, **kwargs):
		print(user)
		super(PeriodForm, self).__init__(*args, **kwargs)
		# self.fields['period'].queryset = Period.objects.filter(user=user)# .exclude(item__isnull=False)
		self.fields['perioddesc'].label = "Period Description"
		self.fields['startdate'].label = "Start Date"
		self.fields['enddate'].label = "End Date"
