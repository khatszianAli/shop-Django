from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Category Name', max_length=45)
    description = models.TextField('Category Description')
    price = models.IntegerField('Category Price')

    def get_absolute_url(self):
        return f'/shop/{self.id}'

    def __str__(self):
        return self.name
