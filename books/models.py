from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    cover = models.ImageField(upload_to='covers/', blank=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.author} : {self.title}"
    
    #get absolute url
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])