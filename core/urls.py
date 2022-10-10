from django.urls import path

# from core.api import TicketCreateandListAPIView
from core.api import (
    TicketAssighAPI,
    TicketResolveAPI,
    TicketRetrieveAPI,
    TicketsCreateAPI,
    TicketsListAPI,
    CommentCreateApi,
    )


ticket_urls = [
    # path("", TicketCreateandListAPIView.as_view()),
    path("", TicketsListAPI.as_view()),
    path("create/", TicketsCreateAPI.as_view()),
    path("<int:id>/", TicketRetrieveAPI.as_view()),
    path("<int:id>/assign/", TicketAssighAPI.as_view()),
    path("<int:id>/resolve/", TicketResolveAPI.as_view()),
]

comment_urls = [
    path("<int:ticket.id>/comment/", CommentCreateApi.as_view())
]

urlpatterns = ticket_urls + comment_urls
