from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app=app)


def test_section_list():
	response = client.get("/forum/sections")
	assert response.status_code == 200
