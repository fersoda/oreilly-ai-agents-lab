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


@tool
def get_stock_price(ticker: str) -> str:
    """Get the current stock price for a given stock exchange ticker symbol.

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


def run_wikipedia_example(llm_with_tools, wiki_tool):
    """Run the Wikipedia search example from the book."""
    print("-" * 40)
    print("Example 1: Wikipedia Search")
    print("-" * 40)

    query = "What was the most impressive thing about Ferran Adria?"
    print(f"Query: {query}\n")

    messages = [HumanMessage(query)]
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    for tool_call in ai_msg.tool_calls:
        tool_msg = wiki_tool.invoke(tool_call)
        print(f"  Tool: {tool_msg.name}")
        print(f"  Args: {tool_call['args']}")
        print(f"  Content: {tool_msg.content[:200]}...")
        messages.append(tool_msg)

    print()
    final_response = llm_with_tools.invoke(messages)
    print(f"Final answer: {final_response.content}\n")


def run_stock_example(llm_with_tools, stock_tool):
    """Run the stock price example from the book."""
    print("-" * 40)
    print("Example 2: Stock Price")
    print("-" * 40)

    query = "What is the stock price of Apple?"
    print(f"Query: {query}\n")

    messages = [HumanMessage(query)]
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    for tool_call in ai_msg.tool_calls:
        tool_msg = stock_tool.invoke(tool_call)
        print(f"  Tool: {tool_msg.name}")
        print(f"  Args: {tool_call['args']}")
        print(f"  Content: {tool_msg.content}")
        messages.append(tool_msg)

    print()
    final_response = llm_with_tools.invoke(messages)
    print(f"Final answer: {final_response.content}\n")


def main():
    print("=" * 60)
    print("Chapter 4 - API-Based Tools (LangChain + Bedrock)")
    print("=" * 60)
    print()

    # Set up Wikipedia tool (from LangChain community)
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
    wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

    # Initialize the LLM with Bedrock
    llm = ChatBedrockConverse(
        model=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
        temperature=0,
        provider="anthropic",  # Required when using model ARN
    )

    # Example 1: Wikipedia (bind wiki tool)
    llm_with_wiki = llm.bind_tools([wiki_tool])
    run_wikipedia_example(llm_with_wiki, wiki_tool)

    # Example 2: Stock price (bind stock tool)
    llm_with_stock = llm.bind_tools([get_stock_price])
    run_stock_example(llm_with_stock, get_stock_price)


if __name__ == "__main__":
    main()
