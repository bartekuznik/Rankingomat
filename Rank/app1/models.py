from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError(_("Users must have an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, username = username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None, **other_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email,username , password, **other_fields)

        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique = True)
    number_of_coins = models.PositiveIntegerField(default=5000)
    is_vip = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
    def __str__(self):
        return "{}".format(self.email)
    
class Rank(models.Model):
    player = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    win_number = models.PositiveIntegerField(default=0)