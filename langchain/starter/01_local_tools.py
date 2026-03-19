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


# TODO: Define your tools using the @tool decorator
# Hint: In LangChain, you define tools exactly like this:
#
# @tool
# def multiply(x: float, y: float) -> float:
#     """Multiply 'x' times 'y'."""
#     return x * y
#
# TODO: Define multiply, exponentiate, and add tools


def main():
    print("=" * 60)
    print("Chapter 4 - Local Tools (LangChain + Bedrock)")
    print("=" * 60)
    print()

    # TODO: Create a list of your tools
    tools = []

    # Initialize the LLM with Bedrock and bind the tools
    llm = ChatBedrockConverse(
        model=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
        temperature=0,
        provider="anthropic",  # Required when using model ARN
    )

    # TODO: Bind the tools to the LLM
    # Hint: llm_with_tools = llm.bind_tools(tools)

    # TODO: Create a query and invoke the model
    # query = "What is 393 * 12.25? Also, what is 11 + 49?"
    # messages = [HumanMessage(query)]
    # ai_msg = llm_with_tools.invoke(messages)

    # TODO: Loop over ai_msg.tool_calls, invoke each tool, and append results
    # Hint: Look at the book example for the pattern:
    #   for tool_call in ai_msg.tool_calls:
    #       selected_tool = {"add": add, ...}[tool_call["name"].lower()]
    #       tool_msg = selected_tool.invoke(tool_call)
    #       messages.append(tool_msg)

    # TODO: Get the final response
    # final_response = llm_with_tools.invoke(messages)
    # print(f"Final answer: {final_response.content}")

    print("Implement the TODOs above, then run this script again.")


if __name__ == "__main__":
    main()
