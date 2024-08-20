#models to define data strctures in db tables. each model mapping to a single db table and each attribute represent db field
#model needed for db abstraction,data validation, object relational mapping, automatic interface, rs
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    is_new = models.BooleanField(default=True)
    is_electric = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"