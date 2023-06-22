from django.db import models

# Create your models
class place(models.Model):
    img=models.ImageField(upload_to='travel/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200,default=True)

class team(models.Model):
    img=models.ImageField(upload_to='travel/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

