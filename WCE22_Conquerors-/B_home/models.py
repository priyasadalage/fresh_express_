
from uuid import uuid4
from django.db import models


# Create your models here.

class broadcast(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid4)
    topic=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
    description=models.TextField()
    format=models.CharField(max_length=10)
    link=models.CharField(max_length=1000)
    toAllFarmers=models.BooleanField(default=True)

    