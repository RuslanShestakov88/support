from rest_framework.permissions import BasePermission

from authentication.models import DEFAUL_ROLES


class OperatorOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.role_id == DEFAUL_ROLES["admin"]:
            return True

        return False