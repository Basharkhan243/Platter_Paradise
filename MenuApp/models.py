from django.db import models

# Create your models here.
class ImageData(models.Model):
  imageName = models.CharField(max_length=100,default='default_image_name')
  srno = models.AutoField(primary_key=True)
  imageval = models.ImageField(upload_to='images/')
  desc = models.TextField(default='default description')
  
  def __str__(self):
    return self.imageName
  
  
class SearchQuery(models.Model):
  query = models.CharField(max_length=200, default='')
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.query
  