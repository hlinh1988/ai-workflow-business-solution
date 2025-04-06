# AI Workflow Business Solution
# A project which create to submit Assignment of "AI Workflow: AI in Production" course (on Coursera)
## Project Features
- FastAPI for serving model
- Model comparison (Baseline vs Best)
- Automated Data Ingestion
- Monitoring with Prometheus
- Logger with log file
- Automated Unit Tests
- Dockerized App

## Usage
```bash
docker-compose up --build

##Key Features Mapping
Requirement         Implementation
Unit Test API	      tests/test_api.py using pytest
Unit Test Model	    tests/test_model.py
Unit Test Logging	  tests/test_logger.py
Run All Tests	      run_tests.sh calls pytest tests/
Monitoring	        app/monitor.py — Use prometheus_client or log metrics manually
Isolate Tests	      Use mock models & mock log files in tests/ folder
Functional API	    GET /predict/{country} & GET /predict/all endpoints in api.py
Data Ingestion	    data/ingest_data.py as reusable function
Multiple Models	    Compare baseline & improved model in model.py
EDA Visuals	        eda/eda_notebook.ipynb with Matplotlib/Seaborn
Dockerized	        Working Dockerfile + docker-compose.yml

Example Command to Run All Tests
chmod +x run_tests.sh
./run_tests.sh

Example API Endpoint Usage
GET /predict/{country}
GET /predict/all

Example Monitoring
from prometheus_client import Counter
prediction_counter = Counter('api_predictions_total', 'Total Predictions Made')
