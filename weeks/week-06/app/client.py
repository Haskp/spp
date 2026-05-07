# Реализуйте здесь клиент для GraphQL.
from __future__ import annotations

import json
from pprint import pprint
from urllib import request
from urllib.error import HTTPError, URLError
from typing import Any

PROJECT_CODE = "bookings-s01"
GRAPHQL_URL = "http://localhost:8000/graphql"


def build_payload(query: str, variables: dict) -> dict:
    """
    Формирует словарь для отправки GraphQL запроса.

    :param query: Текст запроса (query или mutation).
    :param variables: Словарь с переменными.
    :return: Словарь с ключами "query" и "variables".
    """
    return {"query": query, "variables": variables}


def send_graphql_request(url: str, query: str, variables: dict) -> dict[str, Any]:
    """Отправляет GraphQL-запрос и возвращает JSON-ответ."""
    payload = build_payload(query, variables)
    raw_payload = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url=url,
        data=raw_payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def print_graphql_response(result: dict[str, Any]) -> None:
    """Печатает errors и/или data из GraphQL-ответа."""
    if result.get("errors"):
        print("Ошибки GraphQL:")
        pprint(result["errors"])

    if result.get("data") is not None:
        print("Данные GraphQL:")
        pprint(result["data"])


def main() -> None:
    query = """
    query GetBookings {
      bookings {
        id
        date
      }
    }
    """
    mutation = """
    mutation CreateBooking($date: String!) {
      createBooking(date: $date) {
        id
        date
      }
    }
    """

    try:
        query_result = send_graphql_request(GRAPHQL_URL, query, {})
        print_graphql_response(query_result)

        mutation_result = send_graphql_request(
            GRAPHQL_URL,
            mutation,
            {"date": "2026-05-07"},
        )
        print_graphql_response(mutation_result)
    except (HTTPError, URLError) as exc:
        print(f"Сетевая ошибка: {exc}")
    except ValueError as exc:
        print(f"Некорректный JSON в ответе: {exc}")


if __name__ == "__main__":
    main()
