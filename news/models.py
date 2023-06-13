from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=123)
    description = models.CharField(max_length=123)
    created_date = models.DateTimeField

    def __str__(self):
        return f'{self.title}'
    

