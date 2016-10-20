from django.db import models
from django.template.defaultfilters import slugify


class Galery(models.Model):
	title = models.CharField(max_length=32)
	description = models.TextField()
	image = models.ImageField()
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Galery, self).save(*args, **kwargs)
	    
	def __str__(self):
		return self.title
