from itertools import chain
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from authentication.models import Role
from core.models import Ticket

User = get_user_model()


def user_as_dict(user: User) -> dict:
    return {
        "username": user.username,
        "email": user.email,
        "phone": user.phone,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
    }


def ticket_as_dict(ticket: Ticket) -> dict:
    return {
        "id": ticket.id,
        "theme": ticket.theme,
        "discription": ticket.description,
        "resolved": ticket.resolved,
        "created_at": ticket.created_at,
        "updated_at": ticket.updated_at,
    }


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id"]


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "role",
            "email",
            "username",
            "first_name",
            "last_name",
            "age",
            "phone",
        ]
        # exclude = ["fields you want to hide"]


class TicketSerializer(serializers.ModelSerializer):
    operator = UserSerializer(read_only=True)
    client = UserSerializer(read_only=True)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Ticket
        fields = "__all__"

    def validate(self, attrs: dict) -> dict:
        theme = attrs.get("theme")
        
        if not theme:
            return attrs

        # try:
        #     Ticket.objects.get(theme=theme)
        # except Ticket.DoesNotExist:
        #     return attrs

        # raise ValueError("This ticket is allready in database")
        # data = Ticket.objects.only("theme")
        data = Ticket.objects.values_list("theme")
        
        for element in chain.from_iterable(data):
            if element == theme:
                raise ValueError("This ticket is allready in database")

        attrs["client"] = self.context["request"].user        
        return attrs


# class RoleLightSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ["id", "username", "role"]
#
#
# class UserLightSerializer(serializers.ModelSerializer):
#    role = RoleLightSerializer()
#
#    class Meta:
#        model = User
#        fields = ["id", "username", "email", "role"]


class TicketLightSerializer(serializers.ModelSerializer):
    # operator = UserLightSerializer()
    # client = UserLightSerializer()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Ticket
        fields = ["id", "theme", "resolved", "operator", "client"]
