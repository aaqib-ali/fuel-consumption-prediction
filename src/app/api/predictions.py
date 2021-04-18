from fastapi import APIRouter
from typing import List
import json
import requests

from app.api.models import Features
from app.api.config import config

router = APIRouter()

def transform_input_data(features: List[Features]):
    return json.dumps({"signature_name": "serving_default", "instances": features})


def request_predictions(features: List[Features]):
    data = transform_input_data(features)

    ml_server_url = config['api']['url']
    request_headers = {"content-type": "application/json"}
    json_response = requests.post(ml_server_url, data=data, headers=request_headers)
    prediction = json.loads(json_response.text)['predictions']

    return prediction

@router.post("/")
async def predict(data: Features):
    data = data.dict()
    features = data.values()
    return request_predictions(list(features))
    
    

@router.post("/bulk/")
async def predict_bulk(data: List[Features]):
    features = []
    for feature in data:
        features.append(list(dict(feature).values()))

    return request_predictions(features)
