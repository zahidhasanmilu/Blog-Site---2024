from django.db import models
from django.contrib.auth.models import AbstractUser
from user_profile.managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        error_messages={
            'unique': "Email Must Be Unique",
        })
    profile_image = models.ImageField(
        upload_to="Profile_images/",
        blank=True, 
        null=True
        )
    
    

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.username
    
    
    def get_profile_picture(self):
        url =  ""
        try:
            url = self.profile_image.url
        except:
            url = ""
        
        return url