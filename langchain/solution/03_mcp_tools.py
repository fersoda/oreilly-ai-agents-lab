"""
Chapter 4 - MCP Tools (LangChain + Bedrock)

Demonstrates the Model Context Protocol (MCP) using LangChain.
Connects to a running MCP math server via SSE transport.

Start the MCP server first (in a separate terminal):
    python mcp_math_server.py

Then run this script:
    python 03_mcp_tools.py

You can also test the server with the MCP Inspector:
    npx @modelcontextprotocol/inspector
"""

import asyncio
import os

from langchain_aws import ChatBedrockConverse
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")

MCP_SERVER_URL = "http://localhost:8000/mcp"  # Streamable HTTP endpoint (default port)


async def run_agent():
    print("=" * 60)
    print("Chapter 4 - MCP Tools (LangChain + Bedrock)")
    print("=" * 60)
    print()

    llm = ChatBedrockConverse(
        model=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
        temperature=0,
        provider="anthropic",  # Required when using model ARN
    )

    # Connect to the running MCP math server via Streamable HTTP
    mcp_client = MultiServerMCPClient(
        {
            "math": {
                "url": MCP_SERVER_URL,
                "transport": "streamable_http",
            },
        }
    )

    # Discover tools exposed by the MCP server
    tools = await mcp_client.get_tools()
    print(f"Discovered {len(tools)} MCP tools:")
    for t in tools:
        print(f"  - {t.name}: {t.description}")
    print()

    # Bind MCP tools to the LLM
    llm_with_tools = llm.bind_tools(tools)

    # Ask a math question
    query = "What is 393 * 12.25? Also, what is 2 ^ 10?"
    print(f"Query: {query}\n")

    messages = [HumanMessage(query)]
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    # Execute each tool call
    tool_map = {t.name: t for t in tools}
    for tool_call in ai_msg.tool_calls:
        selected_tool = tool_map[tool_call["name"]]
        tool_msg = await selected_tool.ainvoke(tool_call)
        print(f"  Tool: {tool_call['name']} | Args: {tool_call['args']} | Result: {tool_msg.content}")
        messages.append(tool_msg)

    # Get final response
    print()
    final_response = llm_with_tools.invoke(messages)
    print(f"Final answer: {final_response.content}")


def main():
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
