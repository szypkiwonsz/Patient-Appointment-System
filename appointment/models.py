from django.db import models


# Create your models here.
class Post(models.Model):
    date = models.DateTimeField()
    name = models.CharField("Podaj swoje imię:", max_length=120)
    email = models.EmailField("Podaj adres email:")

    def __str__(self):
        return self.email