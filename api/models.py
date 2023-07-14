from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager

# Create your models here.

## User Model class.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=14, unique=True, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email',]),
        ]


## Country.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'country'
        indexes = [
            models.Index(fields=['name',]),
        ]

    def __str__(self):
        return self.name


## CIty.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    class Meta:
        db_table = 'city'
        indexes = [
            models.Index(fields=['name',]),
        ]

    def __str__(self):
        return self.name



## Vendor.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'vendors'
        indexes = [
            models.Index(fields=['user',]),
        ]

    def __str__(self):
        return self.name


## Device.
class Device(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="device/image/", null=True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True)
    offer_price = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'devices'
        indexes = [
            models.Index(fields=['name',]),
        ]

    def __str__(self):
        return self.name


## Lead.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=100, null=True, blank=True)
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("In-progress", "In-progress"),
        ("Converted", "Converted"),
        ("Rejected", "Rejected"),
        )
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'leads'
        indexes = [
            models.Index(fields=['name',]),
        ]

    def __str__(self):
        return self.name


## Walk-IN
class WalkIn(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, null=True, blank=True)
    offer_price = models.IntegerField()
    token_number = models.CharField(max_length=100, null=True, blank=True) 
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'walk_in'
        indexes = [
            models.Index(fields=['vendor','lead', 'device']),
        ]


## Web Page
class WebPage(models.Model):
    title = models.CharField(max_length=200)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'web_pages'
        indexes = [
            models.Index(fields=['title',]),
        ]

    def __str__(self):
        return self.title


## Page Section.
class PageSection(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="page_section/image/", null=True, blank=True)
    desc = models.TextField(blank=True, null=True)
    order = models.CharField(max_length=100, null=True, blank=True)
    page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'page_sections'
        indexes = [
            models.Index(fields=['title',]),
        ]
    def __str__(self):
        return self.title