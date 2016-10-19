from django.db import models
from django.template.defaultfilters import slugify

class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Genre, self).save(*args, **kwargs)

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class Book(models.Model):
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=128)
    sinopsis = models.TextField()
    author = models.ForeignKey(Author)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
	    self.slug = slugify(self.title)
	    super(Book, self).save(*args, **kwargs)

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.title

