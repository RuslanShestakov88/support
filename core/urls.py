from django.urls import path

from core.api import get_post_tickets, retrieve_update_delete_ticket

urlpatterns = [
    path("", get_post_tickets),
    path("<int:id_>/", retrieve_update_delete_ticket),
]

