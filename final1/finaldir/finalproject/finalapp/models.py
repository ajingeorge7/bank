from django.db import models

# Create your models here.
class form(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length = 254)
    gender=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    Branch=models.CharField(max_length=250)

    def __str__(self):
        return self.name