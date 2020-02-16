from django.db import models
import random


def random_string():
    return str(random.randint(10000, 99999))


# Create your models here.
class Post(models.Model):
    date = models.DateTimeField()
    name = models.CharField("Enter your first name:", max_length=120)
    email = models.EmailField("Enter your email adress:")
    key = models.CharField(max_length=5, default=random_string)

    def __str__(self):
        return self.email

    class Meta:
        # Name on the admin page.
        verbose_name_plural = 'Appointments'
