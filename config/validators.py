# from django.core.exceptions import ValidationError

# from django.contrib.auth import get_user_model


# User = get_user_model()

# """" doesn't work, type error"""


# class MyCustomPasswordValidator:
#     def validate(self, passwoed: str, user: User | None = None):  # type: ignore
#         raise ValidationError