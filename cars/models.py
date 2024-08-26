#models to define data strctures in db tables. each model mapping to a single db table and each attribute represent db field
#model needed for db abstraction,data validation, object relational mapping, automatic interface, rs
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    brand = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.name} ({self.model}, {self.year})"