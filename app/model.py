import pickle
import pandas as pd

def load_model(path='models/best_model.pkl'):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, country):
    if country == 'all':
        countries = ['USA', 'CAN', 'FRA', 'VNM']  # Sample
        return {c: model.predict([[1]])[0] for c in countries}
    else:
        if not isinstance(country, str):
            raise ValueError('Country must be a string')
        return model.predict([[1]])[0]  # Dummy input for demo
