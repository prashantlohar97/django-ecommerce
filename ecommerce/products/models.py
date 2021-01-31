from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=10)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacture_date = models.DateField(auto_now_add=True)
    expiry_date = models.CharField(max_length=100)
    product_owner = models.CharField(max_length=20)

    class Meta:
        ordering = ['-manufacture_date']

    def __str__(self):
        return self.name