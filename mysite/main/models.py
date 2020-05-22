from django.db import models
from datetime import datetime

# Create your models here.
class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "category"

    def __str__(self):
        return self.category

class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    category = models.ForeignKey(TutorialCategory, 
                    default=1, 
                    verbose_name="category",
                    on_delete=models.SET_DEFAULT)
    summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "series"

    def __str__(self):
        return self.series

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField("Date Published",default=datetime.now())

    series = models.ForeignKey(TutorialSeries, 
                    default=1, 
                    verbose_name="series",
                    on_delete=models.SET_DEFAULT)
    slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title
