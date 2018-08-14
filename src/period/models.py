from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Period(models.Model):

	#associations
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	# period stuffs 
	perioddesc		= models.CharField(max_length=120)
	startdate		= models.DateField()
	enddate		= models.DateField()

	timestamp	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.perioddesc 

	def get_absolute_url(self):
		# return reverse('category:detail', kwargs={'pk': self.pk})
		return '/period/update/' + str(self.pk)

	def get_absolute_url_delete(self):
		return '/period/delete/' + str(self.pk)

	class Meta:
		ordering = ['perioddesc','-updated']
