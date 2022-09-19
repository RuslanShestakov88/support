from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model


User = get_user_model()


class MyCustomPasswordValidator:
    def validate(self, passwoed: str, user: User):  # type: ignore
        raise ValidationError("my custom validator")
