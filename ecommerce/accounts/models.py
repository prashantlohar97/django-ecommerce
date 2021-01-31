from django.db import models


# Create your models here.

class Detail(models.Model):
    first_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length= 150) 
    
    def __str__(self):
        return self.first_name