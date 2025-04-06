from app.model import load_model, predict

def test_model_loading():
    model = load_model('models/baseline_model.pkl')
    assert model is not None

def test_prediction():
    model = load_model('models/baseline_model.pkl')
    result = predict(model, 'USA')
    assert result is not None
