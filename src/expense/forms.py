from django import forms
from django.conf import settings

from category.models import Category
from .models import Expense

User = settings.AUTH_USER_MODEL

class ExpenseForm(forms.ModelForm):


	expensedate = forms.DateField(widget=forms.DateInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter expense date here..',
					'label' : 'Expense Date',
					'type' : 'Date',
				}
			))
	amount = forms.DecimalField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter amount here...',
				}
			))

	remarks = forms.CharField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter remarks here...',
				}
			))

	# source = forms.CharField(       # A hidden input for internal use
	# 	max_length=50,              # tell from which page the user sent the message
	# 	widget=forms.HiddenInput()
	# )


	class Meta:
		model = Expense
		fields = [
			'category',
			'expensedate',
			'amount',
			'remarks',
		]			



	def clean(self):
		cleaned_data = super(ExpenseForm, self).clean()
		expensedate = cleaned_data.get('expensedate')
		amount = cleaned_data.get('amount')
		remarks = cleaned_data.get('remarks')
		if not expensedate and not amount and not remarks:
			raise forms.ValidationError('You have to write something!')

	def __init__(self, user=None, *args, **kwargs):
		print(user)
		super(ExpenseForm, self).__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(user=user)# .exclude(item__isnull=False)
		self.fields['expensedate'].label = "Expense Date"
