from app import create_app  # or app instance, depending on your project structure


def test_increment_number():
    from app import increment_number
    assert increment_number(3) == 4
    assert increment_number(-1) == 0
    assert increment_number(0) == 1

def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"



