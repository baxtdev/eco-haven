from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django_resized import ResizedImageField



class Category(models.Model):
    title = models.CharField( 
        max_length=250
        )
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self) -> str:
        return self.title
   



class News(models.Model):
    category = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE, 
        related_name='news'
        )
    photo = ResizedImageField(
        upload_to='media/news/images/', 
        force_format='WEBP', quality=90, 
        )
    
    title = models.CharField(
            max_length=250
        )
    description = models.TextField()
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        )

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self) -> str:
        return self.title





class Adviсe(models.Model):
    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL, 
        related_name='advices',
        null=True
        )
    title  = models.CharField(
        max_length=250
        )
    description = models.TextField()
    user = models.ForeignKey(
        User,      
        on_delete=models.CASCADE,
        )

    class Meta:
        verbose_name = 'Advice'
        verbose_name_plural = 'Advices'
    
    def __str__(self) :
        return self.title