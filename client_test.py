import pytest
import server


@pytest.fixture
def client():
    server.app.config["TESTING"] = True
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def reset_data():
    yield
    server.clubs[:] = server.loadClubs()
    server.competitions[:] = server.loadCompetitions()
