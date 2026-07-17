from client_test import client
import server


def test_cannot_book_more_than_12_places(client, monkeypatch):

    competitions = [
        {
            "name": "Spring Festival",
            "date": "2028-03-27 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    clubs = [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "20"}]

    monkeypatch.setattr(server, "competitions", competitions)
    monkeypatch.setattr(server, "clubs", clubs)
    data = {"competition": "Spring Festival", "club": "Simply Lift", "places": "15"}

    response = client.post(
        "/purchasePlaces",
        data=data,
    )

    assert response.status_code == 200
    assert (
        "Booking incomplete, you cannot book more than 12 places!"
        in response.get_data(as_text=True)
    )


def test_can_book_exactly_12_places(client, monkeypatch):
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2028-03-27 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    clubs = [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "20"}]

    monkeypatch.setattr(server, "competitions", competitions)
    monkeypatch.setattr(server, "clubs", clubs)
    data = {"competition": "Spring Festival", "club": "Simply Lift", "places": "12"}

    response = client.post(
        "/purchasePlaces",
        data=data,
    )

    assert response.status_code == 200
    assert "Great-booking complete!" in response.get_data(as_text=True)
