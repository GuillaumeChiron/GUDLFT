from client_test import client
import server


def test_dashboard_display_points(client, monkeypatch):

    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]

    monkeypatch.setattr(server, "clubs", clubs)

    response = client.get("/clubDasboard")
    response_data = response.get_data(as_text=True)

    assert response.status_code == 200
    for club in clubs:
        assert f"<td>{club["name"]}</td>" in response_data
        assert f"<td>{club["points"]}</td>" in response_data
