from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Set, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("flashcard:set_detail", kwargs={"slug": self.slug})


class Card(models.Model):
    front = models.CharField(max_length = 200)
    back = models.CharField(max_length= 200)
    of_set = models.ForeignKey(Set, on_delete=models.CASCADE)

    def __str__(self):
        return self.front

    def show_answer(self):
        return self.back
    

