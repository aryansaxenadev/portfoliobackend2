from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils import timezone
from .models import ContactMessage

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Render email template with form data and current date/time
        current_datetime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        email_content = render_to_string('mail.html', {'name': name, 'email': email, 'message': message, 'datetime': current_datetime})

        # Send email notification
        send_mail(
            f'Contact With {name}',
            '',
            'saxenashivansh48123@gmail.com',  # Replace with your email
            ['aryan07developer@gmail.com'],  # Replace with your email
            html_message=email_content,
            fail_silently=False,
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})