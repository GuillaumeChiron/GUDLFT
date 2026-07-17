from client_test import client
import server


def test_cannot_book_more_places_than_available(client, monkeypatch):

    monkeypatch.setattr(
        server,
        "clubs",
        [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}],
    )

    monkeypatch.setattr(
        server,
        "competitions",
        [
            {
                "name": "Fall Classic",
                "date": "2028-10-22 13:30:00",
                "numberOfPlaces": "2",
            }
        ],
    )

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Fall Classic", "club": "Simply Lift", "places": "5"},
    )

    assert response.status_code == 200
    assert (
        "Booking incomplete, you cannot book more places than available!"
        in response.get_data(as_text=True)
    )
    assert server.competitions[0]["numberOfPlaces"] == "2"
