from client_test import client, reset_data
import server


def test_view_dashboard(client, reset_data):

    club = next(club for club in server.clubs if club["name"] == "Simply Lift")
    clubs = server.clubs

    # 1. Test page de connexion
    response = client.get("/")
    assert response.status_code == 200

    # 2. Test tentative de connexion
    response = client.post("/showSummary", data={"email": club["email"]})
    assert response.status_code == 200
    assert club["email"] in response.get_data(as_text=True)

    # 3. Test pour accèder au dashhboard des clubs

    response = client.get("/clubDasboard")
    assert response.status_code == 200
    for c in clubs:
        assert f"<td>{c["name"]}</td>" in response.get_data(as_text=True)
        assert f"<td>{c["points"]}</td>" in response.get_data(as_text=True)
