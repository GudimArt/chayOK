from django.db import models

# Create your models here.

class Tea(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    grammar = models.IntegerField(null=True, blank=True)

    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name

class TeaImages(models.Model):
    img = models.ImageField()
    tea = models.ForeignKey(Tea, on_delete = models.CASCADE)