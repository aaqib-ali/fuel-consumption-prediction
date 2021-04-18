# Fuel Consumption prediction
This repository contains a simple fuel consumption machine learning model with an api to expose predictions
to consumer. The perpose of the repository is to demonstrate creating an api in a containerized environment
with tensorflow server.

The RESTFUL API is developed using :-
* [Fast API](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [nginx](https://nginx.org/en/)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [PyTest](https://docs.pytest.org/en/stable/)
* [Docker](https://www.docker.com/)
* [PyTest-cov](https://pypi.org/project/pytest-cov/)

## Architecture
It's a simple "prediction API" allows user to get fuel consumption predictions for a given data set. This is intentionally kept simple and basic. 

**Note:** API clients like Software System, Single Page Application and Mobile Applicaiton are not included in this code base. There are here to explain the context of predictions API as potential clients. However, the API provides documentation endpoint that include try out an api in the browser. please see "API Documentation" section below.

### System Context

<p align="center">
 <img width="600" height="500" src="./architecture/api_context.png">
</p>

### API Container

The system consists of a reverse proxy, an API and Machine Learning backend system. A reverse proxy provides load balancing of request between multiple instances of an API. An API validates user input, trasform the user input to TensorFlow backend server format and requests predictions from the server.


<p align="center">
 <img width="600" height="600" src="./architecture/api_container.png">
</p>
