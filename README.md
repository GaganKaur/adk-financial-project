This project demonstrates a financial analysis agent built with the Google Agent Development Kit (ADK). It uses a supervisor-subagent architecture to perform a multi-step analysis on a given stock ticker.

## Features

- **Supervisor Agent:** Orchestrates the entire workflow autonomously.
- **Data Fetcher Agent:** Retrieves a concise summary of stock data using `yfinance`.
- **Market News Agent:** Scans the web for recent news and sentiment using Google Search.
- **Competitor Analysis Agent:** Identifies a company's main competitors.


/adk-financial-project/
    financial_agent/            
        ├── sub_agents/
        │   ├── __init__.py
        │   ├── data_fetcher/
        │   │   ├── __init__.py
        │   │   ├── agent.py
        │   │   └── tools.py
        │   ├── market_news.py
        │   └── competitor_analysis.py
        ├── __init__.py
        ├── agent.py                # The Supervisor Agent
        └── .env
    └── requirements.txt

## Setup and Local Testing

1.  **Clone & Install:**
    ```bash
    git clone https://github.com/GaganKaur/adk-financial-project.git
    cd financial_agent_project
    python -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Configure `.env`:**
    Create a `.env` file and fill it with your credentials:
    ```
    GOOGLE_API_KEY="AIza..."
    #VERTEX_PROJECT_ID="your-gcp-project-id" 
    #VERTEX_LOCATION="us-central1" 
    #VERTEX_STAGING_BUCKET="gs://your-gcp-staging-bucket"
    ```

3.  **Run Locally using CLI:**
    ```bash
    adk run
    ```

    **Run on a web interface:**
    ```bash
    adk web
    ```

