from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from category.models import Category
from period.models import Period

# Create your models here.
class Budget(models.Model):

	#associations
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	category	= models.ForeignKey(Category,null=True,on_delete=models.SET_NULL,)
	period	= models.ForeignKey(Period,null=True,on_delete=models.SET_NULL,)

	# period stuffs 
	amount		= models.DecimalField(max_digits=16, decimal_places=2, blank=False, null=False)
	remarks		= models.TextField(blank=True, null=True, max_length=120, help_text='Enter Remarks here')

	timestamp	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return self.category 

	def get_absolute_url(self):
		# return reverse('category:detail', kwargs={'pk': self.pk})
		return '/budget/update/' + str(self.pk)

	def get_absolute_url_delete(self):
		return '/budget/delete/' + str(self.pk)

	class Meta:
		ordering = ['category','-updated']
