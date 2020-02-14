from django.db import models
import random


def random_string():
    return str(random.randint(10000, 99999))


# Create your models here.
class Post(models.Model):
    date = models.DateTimeField()
    name = models.CharField("Podaj swoje imię:", max_length=120)
    email = models.EmailField("Podaj adres email:")
    key = models.CharField(max_length=5, default=random_string)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Umówione wizyty'
