from django.db import models
from config import settings
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    Sarlavha = models.CharField(max_length=200)
    Muallif = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    Matn = models.TextField()

    def __str__(self):
        return self.Sarlavha
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    