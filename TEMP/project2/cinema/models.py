from django.db import models

# Create your models here.
class cin(models.Model):
    img=models.ImageField(upload_to='cine/img',null=True,blank=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)

