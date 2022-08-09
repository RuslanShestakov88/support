from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


def create_dev_user(*args, **kwargs):
    if settings.DEBUG:
        payload = {
            "email": "admin@admin.com",
            "username": "admin",
            "password": "admin",
            "first_name": "Admin",
            "last_name": "Adminovich",
            "age": 30,
            "phone": "0671234567"
        }
    
        User.objects.create_superuser(**payload)