from django.contrib import admin

from .models import Comment, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "operator", "client", "theme"]
    list_filter = ["operator"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "ticket"]
