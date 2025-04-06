A business solution (ref: https://github.com/aavail/ai-workflow-capstone), submitted to "AI Workflow: AI in Production" course (on Coursera).
Repository Structure Suggestion

ai-business-solution/
│
├── app/                      # API & Model Logic
│   ├── api.py                # FastAPI endpoints
│   ├── model.py              # Model logic, loading, inference
│   ├── logger.py             # Logging setup
│   └── monitoring.py         # Performance monitoring metrics
│
├── data/                    
│   └── ingest_data.py        # Data ingestion script
│
├── eda/                      # Exploratory Data Analysis
│   └── eda_notebook.ipynb    # EDA with visualizations
│
├── models/                   # Trained Models
│   ├── baseline_model.pkl
│   ├── best_model.pkl
│   └── model_comparison.png  # Visualization comparing models
│
├── tests/                    # Unit Tests
│   ├── test_api.py           # API unit tests
│   ├── test_model.py         # Model unit tests
│   └── test_logger.py        # Logging unit tests
│
├── requirements.txt          
├── Dockerfile               
├── docker-compose.yml        
├── run_tests.sh              # Script to run all tests
├── .env                      # Env variables
└── README.md                 

Key Features Mapping
Requirement	      Implementation
Unit Test API	    tests/test_api.py using pytest
Unit Test Model	  tests/test_model.py
Unit Test Logging	tests/test_logger.py
Run All Tests	    run_tests.sh calls pytest tests/
Monitoring	      app/monitoring.py — Use prometheus_client or log metrics manually
Isolate Tests	    Use mock models & mock log files in tests/ folder
Functional API	  GET /predict/{country} & GET /predict/all endpoints in api.py
Data Ingestion	  data/ingest_data.py as reusable function
Multiple Models	  Compare baseline & improved model in model.py
EDA Visuals	      eda/eda_notebook.ipynb with Matplotlib/Seaborn
Dockerized	      Working Dockerfile + docker-compose.yml

Example           Command to Run All Tests
chmod +x run_tests.sh
./run_tests.sh

Example API Endpoint Usage
GET /predict/{country}
GET /predict/all

Example Monitoring
from prometheus_client import Counter
prediction_counter = Counter('api_predictions_total', 'Total Predictions Made')
