from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.URLField(max_length=300)
    price=models.CharField(max_length=6)

    def __str__(self):
        return self.name