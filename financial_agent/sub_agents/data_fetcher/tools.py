import yfinance as yf
import math
from google.adk.tools import FunctionTool

def clean_financial_dict(d: dict) -> dict:
    """
    Recursively cleans a dictionary by converting non-serializable
    values (like NaN) to strings.
    """

    if not isinstance(d, dict):
        return d
    
    clean_dict = {}
    for key, value in d.items():
        # Check if the value is a NaN (Not a Number) float
        if isinstance(value, float) and math.isnan(value):
            clean_dict[str(key)] = "N/A"
        # Check if the value is None
        elif value is None:
            clean_dict[str(key)] = "N/A"
        # If the value is another dictionary, clean it recursively
        elif isinstance(value, dict):
            clean_dict[str(key)] = clean_financial_dict(value)
        else:
            clean_dict[str(key)] = value
    return clean_dict


# --- Tool Functions ---

# financial_agent/agents/data_fetcher/tools.py
import yfinance as yf
from google.adk.tools import FunctionTool
import math

def get_stock_summary(ticker_symbol: str) -> dict:
    """
    Retrieves a concise summary of key financial data and company info for a ticker.
    This is the primary tool to get the company's full name and essential stats.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info

        # Immediately return an error if the ticker is invalid
        if not info.get("symbol"):
            return {"error": f"Invalid or delisted ticker: {ticker_symbol}"}

        # Selectively extract only the most important fields for the final report.
        # This prevents flooding the context window with hundreds of unnecessary fields.
        summary = {
            "symbol": info.get("symbol"),
            "longName": info.get("longName"),
            "currentPrice": info.get("currentPrice"),
            "marketCap": info.get("marketCap"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "dayHigh": info.get("dayHigh"),
            "dayLow": info.get("dayLow"),
            "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
            "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
            "averageVolume": info.get("averageVolume"),
            "trailingPE": info.get("trailingPE"),
            "forwardPE": info.get("forwardPE"),
            "recommendationKey": info.get("recommendationKey"),
            "shortBusinessSummary": (info.get("longBusinessSummary", "")[:300] + "...")
        }
        return summary

    except Exception as e:
        return {"error": f"An error occurred in get_stock_summary: {e}"}

get_stock_summary_tool = FunctionTool(get_stock_summary)