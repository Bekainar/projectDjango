from django.db import models


class Category(models.Model):
    category_name = models.CharField('Category name', max_length=200)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField('Product name', max_length=200)
    product_price = models.FloatField()
    product_description = models.TextField('description')
    product_count = models.IntegerField()
    product_is_active = models.BooleanField()

    def __str__(self):
        return self.product_name



