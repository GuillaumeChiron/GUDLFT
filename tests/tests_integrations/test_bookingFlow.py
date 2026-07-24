from client_test import client, reset_data
import server


def test_booking_flow(client, reset_data):

    club = next(club for club in server.clubs if club["name"] == "Simply Lift")
    competition = next(c for c in server.competitions if c["name"] == "Muscle up")

    pointsBefore = club["points"]
    PlacesBefore = competition["numberOfPlaces"]

    # 1. Test page de connexion
    response = client.get("/")
    assert response.status_code == 200

    # 2. Test tentative de connexion
    response = client.post("/showSummary", data={"email": club["email"]})
    assert response.status_code == 200
    assert club["email"] in response.get_data(as_text=True)

    # 3. Test page de booking
    response = client.get(f"/book/{competition["name"]}/{club["name"]}")
    assert response.status_code == 200
    assert competition["name"] in response.get_data(as_text=True)

    # 4. Test book des places de la competition
    data = {"competition": competition["name"], "club": club["name"], "places": "3"}

    response = client.post(
        "/purchasePlaces",
        data=data,
    )
    assert response.status_code == 200
    assert "Great-booking complete!" in response.get_data(as_text=True)
    assert int(pointsBefore) - int(data["places"]) == int(club["points"])
    assert int(PlacesBefore) - int(data["places"]) == int(competition["numberOfPlaces"])
