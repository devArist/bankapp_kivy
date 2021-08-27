from django.db import models

# Create your models here.

class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True



class Blog(Base):
    title = models.CharField(max_length=250, verbose_name = 'titre')
    image = models.FileField(upload_to='Blog_img')
    description = models.TextField()
    
    
