from client_test import client
import server
from datetime import datetime


def test_cannot_book_post_dated_competition(client, monkeypatch):

    today = datetime.now()

    competitions = [
        {
            "name": "Spring Festival",
            "date": "2025-03-27 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    monkeypatch.setattr(server, "competitions", competitions)

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "5"},
    )

    assert response.status_code == 200
    assert datetime.strptime(competitions[0]["date"], "%Y-%m-%d %H:%M:%S") < today
    assert (
        "Booking incomplete, you cannot book a post-dated competition!"
        in response.get_data(as_text=True)
    )


def test_can_book_not_post_dated_competition(client, monkeypatch):

    today = datetime.now()

    competitions = [
        {"name": "Fall Classic", "date": "2028-10-22 13:30:00", "numberOfPlaces": "13"},
    ]

    monkeypatch.setattr(server, "competitions", competitions)

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Fall Classic", "club": "Simply Lift", "places": "5"},
    )

    assert response.status_code == 200
    assert datetime.strptime(competitions[0]["date"], "%Y-%m-%d %H:%M:%S") > today
    assert "Great-booking complete!" in response.get_data(as_text=True)
