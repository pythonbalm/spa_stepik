from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Style(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Features(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class House(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    features = models.ManyToManyField(Features)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('house', kwargs={"pk": self.pk})


class Photo(models.Model):
    # main_photo = models.BooleanField()
    photo = models.ImageField(upload_to='photos')
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=True)


