from django.shortcuts import render, redirect
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from .forms import *
from .thread import SendMailToVendorThread

def home(request):
    webpage = WebPage.objects.all().order_by('-created_on')
    user_list = User.objects.all().order_by('-created_on')
    pagesection_list = PageSection.objects.all().order_by('-created_on')
    vendor_list = Vendor.objects.all().order_by('-created_on')
    lead_list = Lead.objects.all().order_by('-created_on')
    context = {'title': 'Home','webpage_form': WebPageForm(),'pagesection':PageSectionForm(),
    'webpage':webpage,'pagesection_list':pagesection_list, 'user_form':UserForm(), 'user_list':user_list,
    'vendor_form':VendorForm(),'vendor_list':vendor_list,'lead_form':LeadForm(),'lead_list':lead_list}
    return render(request, 'web/index.html', context)


## Store Web Page data.abs
def store_webpage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        device = request.POST.get('device')
        WebPage.objects.create(title=title, device_id=device)
        messages.success(request, 'Data added successfully.')
        return redirect('home')
    else:
        return redirect('home')

## Store PageSection Views
def store_pagesection(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        desc = request.POST.get('desc')
        order = request.POST.get('order')
        page = request.POST.get('page')
        status = request.POST.get('status')
        if status == 'on':
            status = True
        else:
            status = False
        
        PageSection.objects.create(title=title,image=image, desc=desc, order=order, page_id=page,status=status)
        messages.success(request, 'Data added successfully.')
        return redirect('home')
    else:
        return redirect('home')


## User Views data.
def store_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        User.objects.create(email=email,username=email, first_name=first_name, last_name=last_name)
        messages.success(request, 'Data added successfully.')
        return redirect('home')
    else:
        return redirect('home')


## Store User Vendor data.abs
def store_vendor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        user = request.POST.get('user')
        if Vendor.objects.filter(user_id=user).exists():
            messages.success(request, 'User already exists!!!.')
        else:
            messages.success(request, 'Data added successfully.')
            record_data = {'name':name,'user_id':user}
            SendMailToVendorThread(record_data).start()
            Vendor.objects.create(name=name, phone_number=phone_number,address=address,country_id=country,city_id=city,user_id=user)
        return redirect('home')
    else:
        return redirect('home')



## Store Lead data.
def store_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        referral_code = request.POST.get('referral_code')
        status = request.POST.get('status')
        Lead.objects.create(name=name,email=email,status=status, phone_number=phone_number,address=address,country_id=country,city_id=city,referral_code=referral_code)
        messages.success(request, 'Data added successfully.')
        return redirect('home')
    else:
        return redirect('home')
    