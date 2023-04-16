from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):

        # Validating email
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff = True.'
            )

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser = True.'
            )

        return self.create_user(email, user_name, first_name, password, **other_fields)



class User(AbstractBaseUser, PermissionsMixin): #use default permission facilities that Django has

    email = models.EmailField(_('email address'), unique = True)
    user_name = models.CharField(max_length = 150, unique = True)
    first_name = models.CharField(max_length = 150) 
    last_name = models.CharField(max_length=250)
    contact = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=250)
    date_joined = models.DateField(null=True)
    about = models.TextField(_('about'), max_length = 500, blank = True)

    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False) # set to false on creation of account as we are assuming there will be some secondary check.
                                                     # example: email will be sent to user and only on click will be activated.
    objects = CustomUserManager()
 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'contact']

    def __str__(self):
        return self.email