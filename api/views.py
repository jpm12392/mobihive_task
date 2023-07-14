from django.shortcuts import render
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics, status, permissions, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from mhlabs.paginations import MVPPagination
from .serializers import *
from mhlabs.jwt_tokens import generate_access_token, generate_refresh_token

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

## generate a login token.
class LoginAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            response = Response()

            if (email is None) or (password is None):
                context = {'status': False,'message': 'Incorrect login credentials. Please try again'}
                return Response(context, status=status.HTTP_200_OK)

            user = User.objects.filter(email=email).first()

            if(user is None):
                context = {'status': False,'message': 'Email address incorrect.'}
                return Response(context, status=status.HTTP_200_OK)

            if (not user.check_password(password)):
                context = {'status': False,'message': 'Wrong password'}
                return Response(context, status=status.HTTP_200_OK)
            
            access_token = generate_access_token(user.id)
            refresh_token = generate_refresh_token(user.id)
            response.data = {'status': True, 'massage': 'Login Successfully',"access_token": access_token,"refresh_token": refresh_token,}
            return response

        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
