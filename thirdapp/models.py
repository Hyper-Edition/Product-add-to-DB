from django.db import models

# Create your models here.
class product(models.Model):
    pro_name=models.CharField(max_length=50)
    pro_des=models.CharField(max_length=100)
    pro_qun=models.IntegerField()
    price=models.FloatField()