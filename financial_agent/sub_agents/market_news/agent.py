import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv()

market_news_agent = Agent(
    model=os.getenv("SUB_AGENT_MODEL"),
    name='MarketNewsAgent',
    tools=[google_search],
    instruction="You are a market news analyst. Given a company name, use Google Search to find and summarize recent significant news and market sentiment.",
    output_key="final_market_news_output",
)