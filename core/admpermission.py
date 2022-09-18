
from django.core.exceptions import ValidationError
from rest_framework import permissions
from authentication.models import DEFAUL_ROLES


class AdminForbiden(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role_id == DEFAUL_ROLES["admin"]:
            raise ValidationError(
                {"message": ("only regular user may post the ticket")}
            )
        else: 
            return True