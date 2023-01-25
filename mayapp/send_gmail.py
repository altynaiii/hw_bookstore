from django.core.mail import EmailMessage

from django.conf import settings

def send_msg(email, username):
    mail = EmailMessage('Hello',
    f'HELLO {username}', settings.EMAIL_HOST_USER,
    [email]
    )
    mail.send()
