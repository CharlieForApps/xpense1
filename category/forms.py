from django import forms

# from restaurants.models import RestaurantLocation

from django.conf import settings

from .models import Category

User = settings.AUTH_USER_MODEL

class CategoryForm(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'Enter name here',
				}
			))

	categ = [
			('Expense','Expense'),
			('Income','Income'),
		]
	cattype = forms.CharField(widget=forms.Select(
				attrs={
					'class' : 'form-control',
					# 'placeholder' : 'Enter Category Type (Expense/Income)',
				}, choices=categ
			))

	class Meta:
		model = Category
		fields = [
			 # 'user',
			'name',
			'cattype',

		]			

	def __init__(self, user=None, *args, **kwargs):
		#print(kwargs.pop('user'))
		print(user)
		# print(kwargs)
		super(CategoryForm, self).__init__(*args, **kwargs)
		# self.fields['user'].queryset = Category.objects.filter(user=user)#.exclude(item__isnull=False)
		# self.fields['period'].queryset = Period.objects.filter(user=user)# .exclude(item__isnull=False)
		# dropdown = [
		# 	'Expense',
		# 	'Income',
		# ]
		# self.fields['cattype'].queryset = dropdown