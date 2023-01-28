from django.db import models

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  priority = models.IntegerField(default=1)
  completed = models.BooleanField(default=False, blank=True, null=True)
  
  def __str__(self):
    return self.title