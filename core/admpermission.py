from django.core.exceptions import ValidationError
from rest_framework import permissions


class AdminForbiden(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role_id == "admin" and request.method == "POST":
            raise ValidationError(
                {"message": ("only regular user may post the ticket")}
            )
