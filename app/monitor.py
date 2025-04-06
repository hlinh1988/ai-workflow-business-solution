from prometheus_client import Counter

prediction_counter = Counter('api_predictions_total', 'Total Predictions Made')
