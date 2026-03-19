"""
Chapter 4 - API-Based Tools (LangChain + Bedrock)

Demonstrates API-based tools: Wikipedia search and a stock price tool.
The model can query external services to enrich its responses.

This follows the book example directly, but uses AWS Bedrock instead of OpenAI.
"""

import os

from langchain_aws import ChatBedrockConverse
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")


# TODO: Define the get_stock_price tool
# Hint: Use mock data for the demo (see the book example).
#
# @tool
# def get_stock_price(ticker: str) -> str:
#     """Get the current stock price for a given stock exchange ticker symbol."""
#     mock_prices = {"AAPL": 227.50, "GOOGL": 178.30, ...}
#     ...


def main():
    print("=" * 60)
    print("Chapter 4 - API-Based Tools (LangChain + Bedrock)")
    print("=" * 60)
    print()

    # TODO: Set up the Wikipedia tool from LangChain community
    # Hint:
    #   api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
    #   wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

    # Initialize the LLM with Bedrock
    llm = ChatBedrockConverse(
        model=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
        temperature=0,
        provider="anthropic",  # Required when using model ARN
    )

    # TODO: Example 1 - Wikipedia search
    # 1. Bind wiki_tool to the LLM: llm.bind_tools([wiki_tool])
    # 2. Invoke with: "What was the most impressive thing about Buzz Aldrin?"
    # 3. Execute tool calls and get final response

    # TODO: Example 2 - Stock price
    # 1. Bind get_stock_price to the LLM: llm.bind_tools([get_stock_price])
    # 2. Invoke with: "What is the stock price of Apple?"
    # 3. Execute tool calls and get final response

    print("Implement the TODOs above, then run this script again.")


if __name__ == "__main__":
    main()
