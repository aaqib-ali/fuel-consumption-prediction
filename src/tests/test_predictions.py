import json

import pytest

def test_post_returns_prediction_with_valid_data(test_app):
    test_data = {
        "Cylinders": 8, 
        "Displacement": 390.0, 
        "Horsepower": 190.0, 
        "Weight": 3850.0, 
        "Acceleration": 8.5,        
        "Model_Year": 70, 
        "Europe": 0, 
        "Japan": 0, 
        "USA": 1
    }
    response = test_app.post("/predict/", json.dumps(test_data))
    assert response.status_code == 200

def test_post_bulk_returns_multiple_prediction_with_valid_data(test_app):
    test_data_bulk = [
        {"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1},
        { "Cylinders": 8, "Displacement": 360,"Horsepower": 215, "Weight": 4615,"Acceleration": 14, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1}
        ]
    response = test_app.post("/predict/bulk/", json.dumps(test_data_bulk))
    assert response.status_code == 200

@pytest.mark.parametrize(
    "payload, status_code",
    [
        [{}, 422],
        [{"Cylinders": "", "Displacement": "foo", "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5,"Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": "", "Weight": "foo", "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": "", "Model_Year": "foo", "Europe": 0, "Japan": 0, "USA": 1}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": "", "Japan": "foo", "USA": 1}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": ""}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": "foo", "Japan": 0, "USA": 1}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": "foo"}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": -1, "USA": 0}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 2, "USA": 0}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": -1, "Japan": 0, "USA": 0}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe":2, "Japan": 0, "USA": 0}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe":2, "Japan": 0, "USA": -1}, 422],
        [{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe":2, "Japan": 0, "USA": 2}, 422],
    ]
)
def test_post_prediction_with_invalid_data(test_app, payload, status_code):
    response = test_app.post("/predict/", json.dumps(payload))
    assert response.status_code == status_code

@pytest.mark.parametrize(
    "payload, status_code",
    [
        [[{}], 422],
        [[{"Cylinders": "", "Displacement": "foo", "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5,"Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1},
          {"Cylinders": "", "Displacement": "foo", "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1}], 422],
        [[{"Cylinders": 8, "Displacement": 390.0, "Horsepower": "", "Weight": "foo", "Acceleration": 8.5,
          "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1},
          {"Cylinders": 8, "Displacement": 390.0, "Horsepower": "", "Weight": "foo", "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": 1}], 422],
        [[{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": "", "Model_Year": "foo", "Europe": 0, "Japan": 0, "USA": 1},
          {"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": "", "Model_Year": "foo", "Europe": 0, "Japan": 0, "USA": 1}], 422],
        [[{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5,"Model_Year": 70, "Europe": "", "Japan": "foo", "USA": 1},
          {"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5,"Model_Year": 70, "Europe": "", "Japan": "foo", "USA": 1}], 422],
        [[{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": ""},
          {"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": ""}], 422],
        [[{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": "foo", "Japan": 0, "USA": 1},
          {"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": "foo", "Japan": 0, "USA": 1}], 422],
        [[{"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": "foo"},
          {"Cylinders": 8, "Displacement": 390.0, "Horsepower": 190.0, "Weight": 3850.0, "Acceleration": 8.5, "Model_Year": 70, "Europe": 0, "Japan": 0, "USA": "foo"}], 422],
    ]
)
def test_post_prediction_bulk_with_invalid_data(test_app, payload, status_code):
    response = test_app.post("/predict/bulk/", json.dumps(payload))
    assert response.status_code == status_code

