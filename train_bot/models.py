from django.db import models

class Railway(models.Model):
  title = models.CharField(max_length = 20)
  railway = models.CharField(max_length = 100)
  operator = models.CharField(max_length = 100)

  def __str__(self):
    return self.title

class Station(models.Model):
  title = models.CharField(max_length = 20)
  station = models.CharField(max_length = 100)
  geo_lon = models.DecimalField(max_digits = 12, decimal_places = 2)
  geo_lat = models.DecimalField(max_digits = 12, decimal_places = 2)
  railway  = models.ForeignKey('Railway', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title

