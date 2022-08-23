from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    operator = UserSerializer()
    client = UserSerializer()

    class Meta:
        model = Ticket
        fields = [
            "id",
            "operator",
            "client",
            "theme",
            "description",
            "resolved",
        ]


#class RoleLightSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ["id", "username", "role"]
#
#
#class UserLightSerializer(serializers.ModelSerializer):
#    role = RoleLightSerializer()
#
#    class Meta:
#        model = User
#        fields = ["id", "username", "email", "role"]


class TicketLightSerializer(serializers.ModelSerializer):
    #operator = UserLightSerializer()
    #client = UserLightSerializer()

    class Meta:
        model = Ticket
        fields = ["id", "theme", "resolved", "operator", "client"]


@api_view(["GET"])
def get_all_tickets(request):
    tickets = Ticket.objects.all()
    data = TicketLightSerializer(tickets, many=True).data
    return Response(data=data)


@api_view(["GET"])
def get_ticket(request, id_: int):
    tickets = Ticket.objects.get(id=id_)
    data = TicketSerializer(tickets).data
    return Response(data=data)


