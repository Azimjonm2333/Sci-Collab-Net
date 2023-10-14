import hashlib
import os
import random
import string
import uuid
import requests
from django.core.mail import send_mail


def reduce_path(file_name, times):
    result = os.path.realpath(file_name)
    for i in range(times):
        result = os.path.dirname(result)
    return result


def get_amount(amount, discount):
    return amount - (amount * discount / 100)


def send_sms_notification(phone_numbers: list | str, message: str):
    LOGIN = 'smartlife'
    PASSWORD = 'sm@rtlife'
    MESSAGE = message

    if isinstance(phone_numbers, str):
        phone_numbers = [phone_numbers]
    phone_numbers = [str(phone).replace('+', '') for phone in phone_numbers]
    RECIPIENTS = ','.join(phone_numbers)
    APIKEY = hashlib.md5(f"{LOGIN}{PASSWORD}{MESSAGE}".encode("utf-8")).hexdigest()

    response = requests.get("http://109.74.70.2:7678/sms_notification/sms.php", {
        "login": LOGIN,
        "apikey": APIKEY,
        "message": MESSAGE,
        "recipients": RECIPIENTS
    })

    result = int(response.text.split('<result>')[1].split('</result>')[0])
    return not bool(result)


def send_email_notification(subject: str, message: str, recipients: list | str) -> None:
    from_email = 'send.message.2333@gmail.com'
    if isinstance(recipients, str):
        recipients = [recipients]
    send_mail(subject, message, from_email, recipients)


def generate_unique_string(length):
    generated_string = str(uuid.uuid4())[:length]
    return generated_string


def generate_password(length: int = 8) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
