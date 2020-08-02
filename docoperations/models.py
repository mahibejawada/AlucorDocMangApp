from django.db import models

# Create your models here.
class UserDocs(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_doc = models.ImageField(null=True,blank=True)