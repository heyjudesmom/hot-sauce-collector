from sqlite3 import Timestamp
from django.db import models
from django.urls import reverse

from datetime import date

AMOUNTS = (
    ('F', 'Full'), 
    ('H', 'Half'), 
    ('L', 'Low'), 
    ('E', 'Empty')
)

MEALS = (
  ('Breakfast', 'Breakfast'),
  ('Lunch', 'Lunch'),
  ('Snack', 'Snack'),
  ('Dinner', 'Dinner'),
)

class Dish(models.Model):
    name = models.CharField(max_length=75)
    meal = models.CharField(
    max_length=10,
    choices=MEALS,
    default=MEALS[0][0]
  )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dishes_detail', kwargs={'pk': self.id})


class Sauce(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    notable_ingredients = models.TextField(max_length=100)
    scoville_scale = models.PositiveIntegerField()
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return f'({self.id}) {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sauce_id': self.id})

    def checked_inventory_today(self):
        return self.stock_set.filter(date=date.today()).count() >= 1

class Stock(models.Model):
    date = models.DateField('Stock Date')
    amount = models.CharField(
        max_length=1, 
        choices=AMOUNTS, 
        default=AMOUNTS[0][0]
        )
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_amount_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date', '-id']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)

  def __str__(self):
    return f'Photo for sauce_id {self.sauce_id} at url {self.url}'