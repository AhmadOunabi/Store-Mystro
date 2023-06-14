from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    details=models.TextField(max_length=500)
    prise=models.DecimalField(max_digits=5, decimal_places=2)
    tags = TaggableManager()
    image= models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    product=models.ForeignKey(Product, related_name='product_review',on_delete=models.CASCADE)
    review=models.TextField(max_length=500)
    rate=models.DecimalField(max_digits=5, decimal_places=2)
    timezone=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.review