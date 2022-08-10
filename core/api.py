from django.http import JsonResponse


class TicketServivce:
    def get_all_tickets(self) -> dict:
        return {}


def get_all_tickets(requst):
    ticket_service = TicketServivce()
    data = ticket_service.get_all_tickets()

    return JsonResponse(data)
