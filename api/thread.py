import threading
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import *



## Send Mail To Assigned Vendor.

class SendMailToVendorThread(threading.Thread):
    def __init__(self, record_data):
        self.record_data = record_data
        threading.Thread.__init__(self)

    def run(self) -> None:
        name = self.record_data['name']
        user_id = self.record_data['user_id']
        userrecord = User.objects.filter(id=user_id).last()
        msg_plain = ''
        subject = 'Assigned Vendor'
        from_email = settings.DEFAULT_FROM_EMAIL
        email_to = userrecord.email
        msg_html = render_to_string('mail/vendor_assigned.html', {'name': name,'email':userrecord.email,})
        send_mail(subject, msg_plain, from_email, [email_to], html_message=msg_html)
        return super().run()