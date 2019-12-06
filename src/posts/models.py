from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    category_choices = ( ('artwork', 'Artwork'),
                         ('graphic', 'Graphic Design'),
                         ('personal', 'Personal'),
                         ('portrait', 'Portrait'),
                         ('professional', 'Professional') )

    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d/')
    category = models.CharField(max_length=12, choices=category_choices)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta():
        ordering = [ '-date_posted' ]
