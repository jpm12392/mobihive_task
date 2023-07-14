from django.contrib import admin
from .models import *

class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['name', 'status', ]

class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'country', ]

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['first_name', 'last_name', 'email', 'mobile', 'is_active' ]

class VendorAdmin(admin.ModelAdmin):
    model = Vendor
    list_display = ['name', 'phone_number', 'address', 'country', 'city', 'user' ]

class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = ['name', 'image', 'currency', 'offer_price', 'vendor', 'status' ]

class LeadAdmin(admin.ModelAdmin):
    model = Lead
    list_display = ['name', 'email', 'phone_number', 'address', 'country', 'city','referral_code', 'status' ]

class WalkInAdmin(admin.ModelAdmin):
    model = WalkIn
    list_display = ['lead', 'vendor', 'device', 'currency', 'offer_price', 'token_number', ]

class WebPageAdmin(admin.ModelAdmin):
    model = WebPage
    list_display = ['title', 'device', ]

class PageSectionAdmin(admin.ModelAdmin):
    model = PageSection
    list_display = ['title', 'image', 'desc', 'order', 'page', 'status']

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(WalkIn, WalkInAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(PageSection, PageSectionAdmin)
