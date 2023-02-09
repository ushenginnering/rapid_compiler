from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from .backends import MyCustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    GENDER              = [
        ("male","male"),
        ("female", "female")
    ]
    gender              = models.CharField(
                            max_length=50,
                            choices=GENDER
                            )
    first_name          = models.CharField(
                            max_length=70,
                            )
    last_name           = models.CharField( 
                            max_length=50,
                            )
    second_name          = models.CharField(
                            max_length=70,
                            null=True,
                            blank=True
                            )
    date_of_birth       = models.DateField(
                            null=True,
                            blank=True
                            )
    email               = models.EmailField(
                            max_length=254,
                            unique=True
                            )
    phone               = PhoneNumberField(region="NG")
    phone_verified      = models.BooleanField(default=False)
    email_verified      = models.BooleanField(default=False)

    username            = None

    objects = MyCustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.second_name}"

    def get_short_name(self):
        return self.first_name

    def verify_phone(self):
        pass

    def verify_email(self):
        pass
    
    
class School(models.Model):
    name                = models.CharField(
                            max_length=150
                            )
    location            = models.CharField( 
                            max_length=150
                            )
    user                = models.OneToOneField("CustomUser", related_name="school", on_delete=models.CASCADE)

# class Teacher(models.Model):
#     user                = models.OneToOneField("CustomUser", on_delete=models.CASCADE)


# class Student(models.Model):
