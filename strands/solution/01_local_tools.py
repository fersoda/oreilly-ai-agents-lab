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

# --- Define local tools using @tool decorator ---

@tool
def multiply(x: float, y: float) -> float:
    """Multiply 'x' times 'y'."""
    return x * y

@tool
def exponentiate(x: float, y: float) -> float:
    """Raise 'x' to the power of 'y'."""
    return x ** y

@tool
def add(x: float, y: float) -> float:
    """Add 'x' and 'y'."""
    return x + y


def initialize_agent():
    bedrock_model = BedrockModel(
        model_id=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
    )

    return Agent(
        model=bedrock_model,
        tools=[multiply, exponentiate, add],
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
