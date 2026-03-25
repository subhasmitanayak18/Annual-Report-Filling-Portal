from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError




class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role

class UserManager(BaseUserManager):
   def create_user(self, email, password=None, role=None, division=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        # is_superuser = extra_fields.get('is_superuser', False)

        if role and role.role.lower() == 'filling_user' and not division:
            raise ValueError('Filling Users must have a division')
        
        if role and role.role.lower() == 'admin' and division:
            raise ValueError('Admins should not be assigned a division')
        
        user = self.model(email=email, role=role, division=division, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

   def create_superuser(self, email, password, role=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if role is None:
            role = Role.objects.get_or_create(role='admin')[0]
        return self.create_user(email, password, role, division = None, **extra_fields)
    
class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    division = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.division

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # admin user flag
    date_joined = models.DateTimeField(default=timezone.now)
    division = models.ForeignKey('Division', on_delete=models.PROTECT, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & password are required by default

    objects = UserManager()

    def __str__(self):
        return self.email
    
    
    def clean(self):
        super().clean()
        # Ensure division is set when role is "Filling User" (role_id = 2)
        if self.role and self.role.role.lower() == 'filling_user' and not self.division:
            raise ValidationError({'division':"Filling Users must have a division assigned."})
        
        if self.role and self.role.role.lower() == 'admin' and self.division:
            raise ValidationError({'division': "Admins should not be assigned a division."})