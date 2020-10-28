from django.db import models

# Create your models here.
class Article(models.Model):
    articlename=models.CharField(max_length=50)

    def __str__(self):
        return self.articlename
    