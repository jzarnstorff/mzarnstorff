from django.db import models
from django.urls import reverse

class Profile(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics')
    about = models.TextField()

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return '{} Profile'.format(self.name)


class URL(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url_name = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{} URL'.format(self.name)

