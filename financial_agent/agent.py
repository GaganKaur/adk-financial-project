# financial_agent/agent.py
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from .prompts import get_supervisor_instructions
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents import LlmAgent


load_dotenv()

# This import now works because agents/__init__.py aggregates everything.
from .sub_agents import data_fetcher_agent, market_news_agent, competitor_analysis_agent


root_agent = LlmAgent(
    model=os.getenv("SUPERVISOR_MODEL"),
    name="FinancialAnalystSupervisor",
    instruction=get_supervisor_instructions(),
    tools=[
        AgentTool(agent=data_fetcher_agent),
        AgentTool(agent=market_news_agent),
        AgentTool(competitor_analysis_agent),
    ],
)