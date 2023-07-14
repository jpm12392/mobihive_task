from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

## City Serializer.
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

## City Serializer.
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


## Device Serializer.
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


## Lead Serializer.
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


## WalkIn Serializer.
class WalkInSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkIn
        fields = '__all__'


## WebPage Serializer.
class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = '__all__'


## PageSection Serializer.
class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = '__all__'