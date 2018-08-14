from django import forms

# from restaurants.models import RestaurantLocation

from django.conf import settings

from category.models import Category
from period.models import Period
from .models import Budget

User = settings.AUTH_USER_MODEL

class BudgetForm(forms.ModelForm):

	# expensedate = forms.DateField(widget=forms.TextInput(
	# 			attrs={
	# 				'class' : 'form-control',
	# 				'placeholder' : 'Enter expense date here..',
	# 				'label' : 'Expense Date',
	# 			}
	# 		))
	amount = forms.DecimalField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter amount here',
				}
			))

	remarks = forms.CharField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter remarks here',
				}
			))

	class Meta:
		model = Budget
		fields = [
			'category',
			'period',
			'amount',
			'remarks',
		]			

	def __init__(self, user=None, *args, **kwargs):
		print(user)
		super(BudgetForm, self).__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(user=user)# .exclude(item__isnull=False)
		self.fields['period'].queryset = Period.objects.filter(user=user)# .exclude(item__isnull=False)

