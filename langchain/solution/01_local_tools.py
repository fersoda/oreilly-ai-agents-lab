"""
Chapter 4 - Local Tools (LangChain + Bedrock)

Demonstrates local calculator tools (multiply, exponentiate, add) using LangChain.
The model can select and invoke these tools to answer math questions.

This follows the book example directly, but uses AWS Bedrock instead of OpenAI.
"""

import os

from langchain_aws import ChatBedrockConverse
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")


@tool
def multiply(x: float, y: float) -> float:
    """Multiply 'x' times 'y'."""
    return x * y

@tool
def exponentiate(x: float, y: float) -> float:
    """Raise 'x' to the 'y'."""
    return x ** y

@tool
def add(x: float, y: float) -> float:
    """Add 'x' and 'y'."""
    return x + y


def main():
    print("=" * 60)
    print("Chapter 4 - Local Tools (LangChain + Bedrock)")
    print("=" * 60)
    print()

    tools = [multiply, exponentiate, add]

    # Initialize the LLM with Bedrock and bind the tools
    llm = ChatBedrockConverse(
        model=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
        temperature=0,
        provider="anthropic",  # Required when using model ARN
    )
    llm_with_tools = llm.bind_tools(tools)

    # Ask the model a question that requires tool use
    query = "What is 393 * 12.25? Also, what is 11 + 49?"
    print(f"Query: {query}\n")

    messages = [HumanMessage(query)]
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    # Execute each tool call the model made
    for tool_call in ai_msg.tool_calls:
        selected_tool = {
            "add": add,
            "multiply": multiply,
            "exponentiate": exponentiate,
        }[tool_call["name"].lower()]

        tool_msg = selected_tool.invoke(tool_call)
        print(f"  Tool: {tool_msg.name} | Args: {tool_call['args']} | Result: {tool_msg.content}")
        messages.append(tool_msg)

    # Get final response with tool results included
    print()
    final_response = llm_with_tools.invoke(messages)
    print(f"Final answer: {final_response.content}")


if __name__ == "__main__":
    main()
