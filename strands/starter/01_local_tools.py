"""
Chapter 4 - Local Tools (Strands Agents)

Demonstrates local calculator tools (multiply, exponentiate, add) using Strands.
The agent can select and invoke these tools to answer math questions.

Equivalent to the LangChain calculator example from the book, adapted for Strands.
"""

import os

from strands import Agent, tool
from strands.models import BedrockModel
from terminal_loop import terminal_loop

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")

# --- TODO: Define local tools using the @tool decorator ---
# Hint: In Strands, you define tools with the @tool decorator.
# Each tool needs a docstring that describes what it does (the model reads this!).
#
# @tool
# def multiply(x: float, y: float) -> float:
#     """Multiply 'x' times 'y'."""
#     ...
#
# TODO: Define multiply, exponentiate, and add tools


def initialize_agent():
    bedrock_model = BedrockModel(
        model_id=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
    )

    return Agent(
        model=bedrock_model,
        # TODO: Pass your tools here as a list
        tools=[],
        system_prompt=(
            "You are a helpful calculator assistant. "
            "Use the provided tools to perform arithmetic operations. "
            "Always use tools for calculations instead of computing them yourself."
        ),
    )


def main():
    print("=" * 60)
    print("Chapter 4 - Local Tools (Strands)")
    print("=" * 60)
    print()

    agent = initialize_agent()
    print("Agent ready!")
    print("Try: 'What is 393 * 12.25? Also, what is 11 + 49?'\n")

    terminal_loop(agent)


if __name__ == "__main__":
    main()
