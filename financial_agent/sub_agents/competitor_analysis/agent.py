import os
from google.adk import Agent
from google.adk.tools import google_search

competitor_analysis_agent = Agent(
    model=os.getenv("SUB_AGENT_MODEL", "gemini-2.0-flash"),
    name='CompetitorAnalysisAgent',
    tools=[google_search],
    instruction="You are a market intelligence analyst. Given a company name, use Google Search to identify its top 2-3 direct competitors and their stock tickers.",
    output_key="final_competitor_assessment_output",
)