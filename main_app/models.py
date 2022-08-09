from django.db import models
from django.urls import reverse
# Create your models here.

AMOUNTS = (
    ('F', 'Full'), 
    ('H', 'Half'), 
    ('L', 'Low'), 
    ('E', 'Empty')
)

class Sauce(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    notable_ingredients = models.TextField(max_length=100)
    scoville_scale = models.PositiveIntegerField()

    def __str__(self):
        return f'({self.id}) {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sauce_id': self.id})

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
        ordering = ['-date']