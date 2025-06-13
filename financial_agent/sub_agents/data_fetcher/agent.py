# financial_agent/sub_agents/data_fetcher/agent.py
import os
from google.adk.agents import Agent

from .tools import ( 
    get_stock_summary_tool
)

data_fetcher_agent = Agent(
    model=os.getenv("SUB_AGENT_MODEL", "gemini-2.0-flash"),
    name="DataFetcherAgent",
    tools=[get_stock_summary_tool],
    instruction="You are a data fetching service. Execute the provided financial tools and return only the raw JSON output.",
    output_key="final_rfinancial_data_output"
)
