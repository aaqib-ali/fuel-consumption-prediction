def test_status(test_app):
    response = test_app.get("/status/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

