import logging

from django.utils.translation import gettext as _
from django.core.mail import send_mail

from . import models


log = logging.getLogger(__name__)


def send_email(request, form):
    settings = models.SiteSettings.objects.first()
    sender_address = settings.email_sender_address
    sender_password = settings.email_sender_password

    data = {
        "subject": "",
        "message": "",
        "from_email": sender_address,
        "recipient_list": [settings.email_receiver],
        "auth_user": sender_address,
        "auth_password": sender_password,
        "fail_silently": False,
    }

    if form.Meta.form_name == 'application_form':
        data['subject'] = _("Received application from https://madaniyat.uz website")
        data['message'] += f"{ _('Region') }: { form.cleaned_data['region'] }\n"
        data['message'] += f"{ _('Full name') }: { form.cleaned_data['full_name'] }\n"
        data['message'] += f"{ _('Email') }: { form.cleaned_data['email'] }\n"
        data['message'] += f"{ _('Phone number') }: { form.cleaned_data['phone_number'] }\n"
        data['message'] += f"{ _('Address') }: { form.cleaned_data['address'] }\n"
        data['message'] += f"{ _('Content') }: { form.cleaned_data['content'] }\n"
        if form.cleaned_data['file']:
            data['message'] += f"{ _('File') }: { form.cleaned_data['file'] }\n"

    if form.Meta.form_name == 'event_form':
        data['subject'] = _("Received event ordering from https://madaniyat.uz website")
        data['message'] += f"{ _('Event') }: { form.cleaned_data['event'] }\n"
        data['message'] += f"{ _('Name') }: { form.cleaned_data['name'] }\n"
        data['message'] += f"{ _('Phone') } number: { form.cleaned_data['phone_number'] }\n"
        data['message'] += f"{ _('People') } count: { form.cleaned_data['people_count'] }\n"
        if form.cleaned_data['description']:
            data['message'] += f"{ _('Description') }: { form.cleaned_data['description'] }\n"

    email_sent = send_mail(**data)
    # print("Email not sent: {}".format(form.Meta.form_name))
    # print(f"Email not sent (form): { form.Meta.form_name }")
    # print(f"Email not sent (data): { data }")
    # print(f"Email not sent (email_sent): { email_sent }")

    return email_sent
