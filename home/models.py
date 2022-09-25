from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    subject=models.IntegerField(choices=((1,'Teklif'),(2,'Irad')))
    message=models.TextField()