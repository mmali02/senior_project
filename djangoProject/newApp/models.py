from django.db import models

class Vegetables(models.Model):
    name = models.CharField('Vegetable name', max_length=200)
    latin_name = models.CharField('Latin name', max_length=200)
    season = models.CharField(max_length=120)
    water = models.CharField(max_length=120)
    soil = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Fruits(models.Model):
    name = models.CharField('Fruit name', max_length=200)
    latin_name = models.CharField('Latin name', max_length=200)
    season = models.CharField(max_length=120)
    water = models.CharField(max_length=120)
    soil = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Plants(models.Model):
    name = models.CharField('Plant name', max_length=200)
    latin_name = models.CharField('Latin name', max_length=200)
    season = models.CharField(max_length=120)
    water = models.CharField(max_length=120)
    soil = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name