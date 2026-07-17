from client_test import client
import server


def test_update_points_are_not_reflected(client, monkeypatch):

    monkeypatch.setattr(
        server,
        "clubs",
        [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "15"}],
    )

    monkeypatch.setattr(
        server,
        "competitions",
        [
            {
                "name": "Fall Classic",
                "date": "2028-10-22 13:30:00",
                "numberOfPlaces": "10",
            }
        ],
    )

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Fall Classic", "club": "Simply Lift", "places": "5"},
    )

    assert response.status_code == 200
    assert server.clubs[0]["points"] == "10"
