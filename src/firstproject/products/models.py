from django.db import models

# Create your models here.
class product(models.Model) :
    name = models.CharField(max_length=120, blank=False) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
    featured = models.BooleanField() #null=True, default=True