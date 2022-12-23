from celery import shared_task
from django.core.mail import send_mail
from backend.celery import celery


# Creating Celery for email background task
@shared_task
def notify_emails(subject, message, email_from, recipient_list):
    for i in range(100):
        send_mail(subject, message, email_from, recipient_list)
