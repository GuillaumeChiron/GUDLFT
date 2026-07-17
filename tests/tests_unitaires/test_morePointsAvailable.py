from client_test import client
import server


def test_cant_use_more_points_than_available(client, monkeypatch):

    competitions = [
        {
            "name": "Spring Festival",
            "date": "2028-03-27 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    clubs = [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "5"}]

    monkeypatch.setattr(server, "competitions", competitions)
    monkeypatch.setattr(server, "clubs", clubs)
    data = {"competition": "Spring Festival", "club": "Simply Lift", "places": "6"}

    response = client.post("/purchasePlaces", data=data)

    assert response.status_code == 200
    assert (
        "Booking incomplete, you cannot use more points than available!"
        in response.get_data(as_text=True)
    )


def test_use_less_points_than_available(client, monkeypatch):
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2028-03-27 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    clubs = [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "5"}]

    monkeypatch.setattr(server, "competitions", competitions)
    monkeypatch.setattr(server, "clubs", clubs)
    data = {"competition": "Spring Festival", "club": "Simply Lift", "places": "4"}

    response = client.post("/purchasePlaces", data=data)

    assert response.status_code == 200
    assert "Great-booking complete!" in response.get_data(as_text=True)
