from core.models import Ticket


class TicketCRUD:
    @staticmethod
    def change_resolved_status(instance: Ticket) -> Ticket:
        instance.resolved = not instance.resolved
        instance.save()

        return instance