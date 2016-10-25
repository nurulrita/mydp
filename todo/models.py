from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
	activity = models.CharField(max_length=120)
	time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.activity
