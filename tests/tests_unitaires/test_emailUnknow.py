from client_test import client
import server
import pytest


def test_unknow_email(client, monkeypatch):

    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]

    emails = ["john@lift.co", "test@irontemple.com", "kate@co.uk"]

    monkeypatch.setattr(
        server,
        "clubs",
        clubs,
    )

    for email in emails:

        response = client.post("/showSummary", data={"email": email})
        assert "Please enter a valid email!" in response.get_data(as_text=True)


def test_valid_email(client, monkeypatch):

    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]

    emails = ["john@simplylift.co", "admin@irontemple.com", "kate@shelifts.co.uk"]

    monkeypatch.setattr(
        server,
        "clubs",
        clubs,
    )

    for email in emails:

        response = client.post("/showSummary", data={"email": email})
        assert email in response.get_data(as_text=True)
