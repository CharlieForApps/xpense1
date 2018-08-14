from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

# from restaurants.models import RestaurantLocation

# Create your models here.
class Category(models.Model):
	INCOME = 'Income'
	EXPENSE = 'Expense'    
	CATEGORY_CHOICES = (
		(INCOME, 'Income'),
		(EXPENSE, 'Expense'),
	)

	#associations
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	# category stuffs 
	name		= models.CharField(max_length=120)

	cattype = models.CharField(
		max_length=120,
		help_text='Input Expense / Income.',
		choices=CATEGORY_CHOICES,
		default=EXPENSE,
	)
	# cattype 	= models.CharField(max_length=120, help_text='Input Expense / Income.')

	timestamp	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name + " - " + self.cattype

	# def get_absolute_url(self):
	# 	return reverse('category:list', kwargs={'pk': self.pk})

	def get_absolute_url(self):
		# return reverse('category:detail', kwargs={'pk': self.pk})
		return '/category/update/' + str(self.pk)

	def get_absolute_url_delete(self):
		return '/category/delete/' + str(self.pk)
		# '/Category/delete/' + self.pk
		# reverse('category:delete', kwargs={'pk': self.pk})

	def search(self, query): #RestaurantLocation.objects.all().search(query) #RestaurantLocation.objects.filter(something).search()
  		if query:
  			query = query.strip()
  			return self.filter(
				Q(name__icontains=query)|
				Q(cattype__icontains=query)
				).distinct()
  		return self

	class Meta:
		ordering = ['name','-updated']



