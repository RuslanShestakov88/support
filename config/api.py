from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from typing import List

import requests
from django.http import JsonResponse

PREFIX = "./config.logs/"
# LOG_FILE = PREFIX + "history.json"
LOG_FILE = "history.json"


def home(request):
    data = {"message": "hello from json response", "num": 12.2}
    return JsonResponse(data)


@dataclass
class ExchangeRate:
    from_: str
    to: str
    value: float

    @classmethod
    def from_response(cls, response: requests.Response) -> ExchangeRate:
        pure_resopnse: dict = response.json()["Realtime Currency Exchange Rate"]
        from_ = pure_resopnse["1. From_Currency Code"]
        to = pure_resopnse["3. To_Currency Code"]
        value = pure_resopnse["5. Exchange Rate"]

        return cls(from_=from_, to=to, value=value)

    def __eq__(self, other: ExchangeRate) -> bool:
        return self.value == other.value


ExchangeRates = List[ExchangeRate]


class ExchangeRatesHistory:
    _history: ExchangeRates = []
    fiel_for_w: str = os.path.join(PREFIX, LOG_FILE)

    @classmethod
    def add(cls, instance: ExchangeRate) -> None:
        if not cls._history:
            cls._history.append(instance)
        elif cls._history[-1] != instance:
            cls._history.append(instance)

    @classmethod
    def as_dict(cls) -> dict:
        return {"results": [asdict(er) for er in cls._history]}

    # trying to write
    @classmethod
    def write(cls, instance: dict) -> None:
        with open("LOG_FILE", "w") as outfile:
            json.dump(instance, outfile)
            # outfile.write(instance)

    # read form file
    @classmethod
    def read(cls):
        with open("LOG_FILE", "r") as outfile:
            return json.load(outfile)


def btc_usd(request):
    API_KEY = "82I46WMYT3C7EX3J"
    url = (
        "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    )
    response = requests.get(url)

    exchange_rate = ExchangeRate.from_response(response)
    ExchangeRatesHistory.add(exchange_rate)

    return JsonResponse(asdict(exchange_rate))


def history(request):
    return JsonResponse(ExchangeRatesHistory.as_dict())