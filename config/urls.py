from django.contrib import admin
from django.urls import path

from exchange_rates.api import btc_usd, history, home
from core.api import get_all_tickets

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    # exchange rates
    path("btc_usd/", btc_usd),
    path("history/", history),
    # tickets
    path("tickets/", get_all_tickets),
]
