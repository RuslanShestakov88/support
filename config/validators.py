from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class MyCustomPasswordValidator:
    def validate(self, passwoed: str, user: User):  # type: ignore
        raise ValidationError("my custom validator")
