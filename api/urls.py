from django.urls import path, include
from .views import *
from .web_views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'country', CountryViewSets, 'country')
router.register(r'city', CityViewSets, 'city')
router.register(r'vendor', VendorViewSets, 'vendor')
router.register(r'device', DeviceViewSets, 'device')
router.register(r'lead', LeadViewSets, 'lead')
router.register(r'walk-in', WalkInViewSets, 'walk-in')
router.register(r'web-page', WebPageViewSets, 'web-page')
router.register(r'page-section', PageSectionViewSets, 'page-section')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', home, name='home'),
    path('store_webpage/', store_webpage, name='store_webpage'),
    path('store_pagesection/', store_pagesection, name='store_pagesection'),
    path('store_user/', store_user, name='store_user'),
    path('store_vendor/', store_vendor, name='store_vendor'),
    path('store_lead/', store_lead, name='store_lead'),
    path('api/v1/login/', LoginAPIView.as_view(), name='login'),
   
    
]