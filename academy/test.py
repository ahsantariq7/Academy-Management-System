from django.core.mail import send_mail
from django.conf import settings

subject = "Test Email"
message = "This is a test email."
from_email = settings.EMAIL_HOST_USER
to_email = [
    "sundastariq2006@example.com"
]  # Replace with your recipient's email address

send_mail(subject, message, from_email, to_email)
