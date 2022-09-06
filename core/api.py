# from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Ticket
from core.serializers import TicketLightSerializer, TicketSerializer

# from rest_framework.response import Response


# class TicketsListCreateApi(ListCreateAPIView):
#     serializer_class = TicketSerializer
#     queryset = Ticket.objects.all()

#     def get_permissions(self):
#         if self.request.method == "POST":
#             return [IsAuthenticated()]
#         else:
#             return []

#     def get_serializer(self, *args, **kwargs):
#         return TicketLightSerializer if self.request.method == "GET"else TicketSerializer


class TicketsListAPI(ListAPIView):
    serializer_class = TicketLightSerializer
    queryset = Ticket.objects.all()


class TicketsCreateAPI(CreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticated]


# @api_view(["GET", "POST"])
# def get_post_tickets(request):
#     if request.method == "GET":
#         tickets = Ticket.objects.all()
#         serializer = TicketLightSerializer(tickets, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = TicketSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         instance = serializer.create(serializer.validated_data)
#         results = TicketSerializer(instance).data

#         return Response(data=results, status=status.HTTP_201_CREATED)


class TicketRetrieveAPI(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"


# @api_view(["GET", "PUT", "DELETE"])
# def retrieve_update_delete_ticket(request, id_: int):
#     choisen_ticket = Ticket.objects.get(id=id_)
#     if request.method == "GET":
#         tickets = Ticket.objects.get(id=id_)
#         data = TicketSerializer(tickets).data
#         return Response(data=data)
#     elif request.method == "PUT":
#         serializer = TicketSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         instance = serializer.update(choisen_ticket, serializer.validated_data)
#         results = TicketSerializer(instance).data

#         return Response(data=results)

#     elif request.method == "DELETE":
#         choisen_ticket.delete()
#         return Response("ticket всё")
