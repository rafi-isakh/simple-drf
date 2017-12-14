from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    publish_date = models.DateTimeField()
    book_category = models.ForeignKey(BookCategory, related_name='books', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    class Meta:
        ordering =  ('title',)
    
    def __str__(self):
        return self.title

class Reader(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class ReaderPoint(models.Model):
    reader = models.ForeignKey(Reader, related_name='points', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    point = models.IntegerField()
    point_date = models.DateTimeField()

    class Meta:
        ordering = ('-point',)
