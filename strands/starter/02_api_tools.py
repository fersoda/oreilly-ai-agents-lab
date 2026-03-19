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


# TODO: Implement the search_wikipedia tool
# Hint: Use the `wikipedia` library to search for information.
# The tool should:
#   1. Accept a query string
#   2. Return a summary from Wikipedia
#   3. Handle DisambiguationError and PageError gracefully
#
# @tool
# def search_wikipedia(query: str) -> str:
#     """Search Wikipedia for information about a topic. ..."""
#     ...


# TODO: Implement the get_stock_price tool
# Hint: For this demo, use a dictionary of mock prices.
# The tool should:
#   1. Accept a ticker symbol string
#   2. Return the price or an error message
#
# @tool
# def get_stock_price(ticker: str) -> str:
#     """Get the current stock price for a given ticker symbol. ..."""
#     ...


def initialize_agent():
    bedrock_model = BedrockModel(
        model_id=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
    )

    return Agent(
        model=bedrock_model,
        # TODO: Pass your tools here
        tools=[],
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
