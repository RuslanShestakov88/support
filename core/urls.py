from django.urls import path

from core.api import (TicketCreateandListAPIView,  # noqa F401
                      TicketRetrieveAPI, TicketsCreateAPI, TicketsListAPI)

urlpatterns = [
    path("", TicketCreateandListAPIView.as_view()),
    # path("", TicketsListAPI.as_view()),
    # path("create/", TicketsCreateAPI.as_view()),
    path("<int:id>/", TicketRetrieveAPI.as_view()),
]
