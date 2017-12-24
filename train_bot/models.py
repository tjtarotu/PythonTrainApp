from django.db import models

class Railway(models.Model):
  title = models.CharField(max_length = 20)
  railway = models.CharField(max_length = 100)
  operator = models.CharField(max_length = 100)

  def __str__(self):
    return self.title
