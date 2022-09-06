from django.urls import path

from core.api import TicketsCreateAPI, TicketsListAPI, TicketRetrieveAPI


urlpatterns = [
    path("", TicketsListAPI.as_view()),
    path("create/", TicketsCreateAPI.as_view()),
    path("<int:id>/", TicketRetrieveAPI.as_view()),
]
