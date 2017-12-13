from django.db import models

# Create your models here.
class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    publish_date = models.DateTimeField()
    book_category = models.CharField(max_length=200, blank=True, default='')
    read = models.BooleanField(default=False)

    class Meta:
        ordering =  ('title',)