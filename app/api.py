from fastapi import FastAPI, HTTPException
from app.model import load_model, predict
from app.logger import get_logger
from app.monitoring import prediction_counter

app = FastAPI()
logger = get_logger()
model = load_model()

@app.get('/')
def read_root():
    return {'message': 'AI Workflow API is running'}

@app.get('/predict/{country}')
def get_prediction(country: str):
    prediction_counter.inc()
    try:
        result = predict(model, country)
        logger.info(f'Prediction success for country: {country}')
        return {'country': country, 'prediction': result}
    except Exception as e:
        logger.error(f'Prediction failed: {e}')
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/predict/all')
def get_all_prediction():
    prediction_counter.inc()
    try:
        result = predict(model, 'all')
        logger.info('Prediction success for all countries')
        return {'prediction': result}
    except Exception as e:
        logger.error(f'Prediction failed: {e}')
        raise HTTPException(status_code=400, detail=str(e))
