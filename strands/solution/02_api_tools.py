"""
Chapter 4 - API-Based Tools (Strands Agents)

Demonstrates API-based tools: Wikipedia search and a stock price tool.
The agent can query external services to enrich its responses.

Equivalent to the LangChain Wikipedia/stock examples from the book, adapted for Strands.
"""

import os

import wikipedia
from strands import Agent, tool
from strands.models import BedrockModel
from terminal_loop import terminal_loop

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")


@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for information about a topic. Returns a summary of the most relevant article.

    Args:
        query: The search term to look up on Wikipedia.
    """
    try:
        result = wikipedia.summary(query, sentences=3)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Ambiguous query. Options: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'."


@tool
def get_stock_price(ticker: str) -> str:
    """Get the current stock price for a given ticker symbol.

    Args:
        ticker: The stock exchange ticker symbol (e.g., AAPL, GOOGL, MSFT).
    """
    # Simulated stock prices for demo purposes
    mock_prices = {
        "AAPL": 227.50,
        "GOOGL": 178.30,
        "MSFT": 425.80,
        "AMZN": 198.60,
        "TSLA": 245.10,
    }
    ticker = ticker.upper()
    if ticker in mock_prices:
        return f"The current stock price of {ticker} is ${mock_prices[ticker]:.2f}"
    return f"Stock ticker '{ticker}' not found. Available: {', '.join(mock_prices.keys())}"


def initialize_agent():
    bedrock_model = BedrockModel(
        model_id=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
    )

    return Agent(
        model=bedrock_model,
        tools=[search_wikipedia, get_stock_price],
        system_prompt=(
            "You are a knowledgeable assistant with access to Wikipedia and stock market data. "
            "Use the search_wikipedia tool to look up factual information. "
            "Use the get_stock_price tool to check current stock prices. "
            "Always cite your sources when using Wikipedia."
        ),
    )


def main():
    print("=" * 60)
    print("Chapter 4 - API-Based Tools (Strands)")
    print("=" * 60)
    print()

    agent = initialize_agent()
    print("Agent ready!")
    print("Try: 'What was the most impressive thing about Buzz Aldrin?'")
    print("Or:  'What is the stock price of Apple?'\n")

    terminal_loop(agent)


if __name__ == "__main__":
    main()
