from django import forms
from .models import *


##WebPage Form
class WebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage
        fields = ['title', 'device']


##PageSection Form
class PageSectionForm(forms.ModelForm):
    class Meta:
        model = PageSection
        fields = ['title', 'image','desc', 'order', 'page', 'status']


## User Form.
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']


## Vendor Form.
class VendorForm(forms.ModelForm):
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=200)
    class Meta:
        model = Vendor
        fields = ['name','phone_number','address','country','city', 'user']


## Lead Form.
class LeadForm(forms.ModelForm):
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=200)
    class Meta:
        model = Lead
        fields = ['name','email','phone_number','country','city', 'address', 'referral_code', 'status']
