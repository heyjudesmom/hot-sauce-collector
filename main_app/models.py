from django.db import models

# Create your models here.
class Sauce(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    notable_ingredients = models.TextField(max_length=100)
    scoville_scale = models.PositiveIntegerField()
    # def __str__(self):
    #     return f'({self.id}) {self.name}'


