from django.shortcuts import render
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics, status, permissions, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from mhlabs.paginations import MVPPagination
from .serializers import *

# Create your views here.

## Country Viewset.
class CountryViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CountrySerializer
    queryset = Country.objects.all()   ## Country Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

## City Viewset.
class CityViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CitySerializer
    queryset = City.objects.all()   ## City Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

## Vendor Viewset.
class VendorViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()   ## Vendor Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone_number',]


## Device Viewset.
class DeviceViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()   ## Device Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


## Lead Viewset.
class LeadViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()   ## Lead Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


## WalkIn Viewset.
class WalkInViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = WalkInSerializer
    queryset = WalkIn.objects.all()   ## WalkIn Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['currency',]


## WebPage Viewset.
class WebPageViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = WebPageSerializer
    queryset = WebPage.objects.all()   ## WebPage Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]


## PageSection Viewset.
class PageSectionViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PageSectionSerializer
    queryset = PageSection.objects.all()   ## PageSection Model
    pagination_class = MVPPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]
