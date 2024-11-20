from django.core.mail import send_mail
from django.conf import settings

def send_booking_email(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )
