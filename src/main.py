from fastapi import FastAPI, status
import logging
from logging.config import dictConfig
from log_config import log_config # this is your local file
from transformers import pipeline
from pydantic import BaseModel

app= FastAPI(debug=True)

@app.on_event("startup")
def load_model():
        global sentiment_model
        sentiment_model = pipeline("sentiment-analysis")

@app.get('/')
def index():
        return {'message': 'this is the homepage of the API'}

dictConfig(log_config)
sentence=""

class PredictionRequest(BaseModel):
  query_string: str

logger = logging.getLogger("my-project-logger") # should be this name unless you change it in log_config.py
logger.info("start to run app")


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perofrm_healthcheck():
        logger.info("health check")
        return {'healthcheck': 'Everthing OK!'}


@app.post("/predict")
def get_sentiment(data:PredictionRequest):
  # YOUR CODE GOES HERE
  sentiment=sentiment_model(data.query_string)
  return{'sentiment': sentiment}