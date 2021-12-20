from django.db import models
 
 #_gte>=
class Movie(models.Model):
    title = models.CharField(max_length=255)
    quote = models.TextField(blank=True)
    content=models.TextField(blank=True)
    img = models.ImageField(upload_to="img/%Y/%m/%d/")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    rating = models.ForeignKey('Rating', on_delete=models.PROTECT, null=True)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mainp_movieslist'

        ordering = ['-time_created', 'title']


        
from django.urls import reverse

class Rating(models.Model):
    scale = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.scale

    def get_absolute_url(self):
        return reverse('rate', kwargs={'rating_id': self.pk})



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
 
    def __str__(self):
        return self.title