from django.db import models
import django.utils.timezone

# Create your models here.
class Blog(models.Model):
	author = models.CharField(max_length=50)
	date = models.DateField(default=django.utils.timezone.now)
	title = models.CharField(max_length=50)
	body = models.TextField()
	img = models.URLField(max_length=200, blank='True')
	
	def __str__ (self):
		return self.title
