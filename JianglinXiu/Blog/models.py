from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.CharField(max_length=200)
    updatetime = models.DateField(null=True)
    imageadress = models.TextField()
    img = models.ImageField(upload_to='upload',default='none')

class Atlas(models.Model):
    updatetime = models.DateField(null=True)
    imageadress = models.TextField()
    img = models.ImageField(upload_to='upload', default='none')