from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=50, default='')
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField(default='')
    image = models.ImageField(upload_to="JmApp/", blank=True, null=True)
    value = models.IntegerField(default=0)
    clickCount = models.IntegerField(default=0)

class Comment(models.Model):
    content = models.TextField(default='')
    writer = models.CharField(max_length=50, default='')
    itemForeign = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)