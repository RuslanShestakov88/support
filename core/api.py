from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Ticket
from core.serializers import TicketLightSerializer, TicketSerializer


@api_view(["GET", "POST"])
def get_post_tickets(request):
    if request.method == "GET":
        tickets = Ticket.objects.all()
        data = TicketLightSerializer(tickets, many=True).data
        return Response(data=data)
    else:
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        instance = serializer.create(serializer.validated_data)
        results = TicketSerializer(instance).data
        
        return Response(data=results, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def retrieve_update_delete_ticket(request, id_: int):
    choisen_ticket = Ticket.objects.get(id=id_)
    if request.method == "GET":
        tickets = Ticket.objects.get(id=id_)
        data = TicketSerializer(tickets).data
        return Response(data=data)
    elif request.method == "PUT":
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        instance = serializer.update(choisen_ticket, serializer.validated_data)
        results = TicketSerializer(instance).data
        
        return Response(data=results)

    elif request.method == "DELETE":
        choisen_ticket.delete()
        return Response("ticket всё")

 