from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 9000,null=True,blank=True)
    detail = models.TextField(null=True,blank=True)
    link= models.CharField(max_length = 1000,null=True,blank=True)
    news_from = models.CharField(max_length = 2000,null=True,blank=True)
    publish_date = models.DateField(null=True,blank=True)
    created = models.DateField(auto_now_add=True)
