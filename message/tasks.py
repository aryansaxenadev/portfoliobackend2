from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

@shared_task
def send_contact_email(name, email, message):
    current_datetime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    email_content = render_to_string('mail.html', {'name': name, 'email': email, 'message': message, 'datetime': current_datetime})

    send_mail(
        f'Contact With {name}',
        '',
        'saxenashivansh48123@gmail.com',  # Replace with your email
        ['aryan07developer@gmail.com'],  # Replace with your email
        html_message=email_content,
        fail_silently=False,
    )
