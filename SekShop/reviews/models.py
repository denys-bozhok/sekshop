from django.db import models


# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=223)
    review_txt = models.TextField()
    tags = models.CharField(max_length=223)
    rating = models.IntegerField(default=3)
    isMember = models.BooleanField()
    
    
    