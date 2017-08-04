from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Change thos to be a product
class Product(models.Model):
    First_Name = models.CharField(max_length = 20)
    Last_Name = models.CharField(max_length = 30)
    Country = models.CharField(max_length = 50)
    Price_in_Dollars = models.CharField(max_length = 7)
    Product = models.CharField(max_length = 30)
    Product_Description = models.TextField()

    def __str__(self):
        return self.Product
