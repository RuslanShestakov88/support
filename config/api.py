from __future__ import annotations

import requests
from django.http import JsonResponse

def home(request):
    data = {"message": "hello from json response", "num": 12.2}
    return JsonResponse(data)

class ExchangeRate:
    def __init__(self, from_: str, to: str, value: float) -> None:
        self.from_: str = from_
        self.to: str = to
        self.value: float = value
    
    @classmethod
    def from_response(cls, response: requests.Response):
        pure_resopnse: dict = response.json()["Realtime Currency Exchange Rate"]
        from_ = pure_resopnse["1. From_Currency Code"]
        to = pure_resopnse["3. To_Currency Code"]
        value = pure_resopnse["5. Exchange Rate"]
        
        return cls(from_ = from_, to = to, value=value)

    def as_dict(self) -> dict:
        return {
            "frrom": self.from_,
            "to": self.to,
            "value": self.value,
        }
    def __eq__(self, other: ExchangeRate)-> bool:
        return self.value == other.value


#NOTE: Global variable to store exchange rates histiry
ExchangeRates = list[ExchangeRate]

ALL_EXCHANGE_RATES: ExchangeRates = []
HISTORY: dict[str, ExchangeRates] = {"results": ALL_EXCHANGE_RATES}

def history_as_json():
    return{
        "results": [element.as_dict() for element in HISTORY["results"]]
    }

def btc_usd(request):
    API_KEY = "82I46WMYT3C7EX3J"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    response = requests.get(url)
    
    exchange_rate = ExchangeRate.from_response(response)
        
    if len(ALL_EXCHANGE_RATES) == 0:
        ALL_EXCHANGE_RATES.append(exchange_rate)
    elif exchange_rate != ALL_EXCHANGE_RATES[-1]:
        ALL_EXCHANGE_RATES.append(exchange_rate)
    
    return JsonResponse(exchange_rate.as_dict())

def history (request):
    return JsonResponse(HISTORY)

