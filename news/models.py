from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


    

