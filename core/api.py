# from rest_framework.decorators import api_view
from requests import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.admpermission import AdminForbiden
from core.models import Ticket
from core.serializers import TicketLightSerializer, TicketSerializer

# from rest_framework.response import Response


class TicketsListAPI(ListAPIView):
    serializer_class = TicketLightSerializer

    def get_queryset(self):
        return Ticket.objects.filter(client=self.request.user)


class TicketsCreateAPI(CreateAPIView):
    permission_classes = (AdminForbiden, IsAuthenticated)
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class TicketRetrieveAPI(RetrieveAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Ticket.objects.filter(client=self.request.user)


class TicketCreateandListAPIView(ListAPIView, CreateAPIView):  # create and list in one
    permission_classes = [IsAuthenticated]  # disable now
    serializer_class = TicketLightSerializer

    def get_queryset(self):
        return Ticket.objects.all()

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# @permissions_classes
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
