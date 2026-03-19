"""
Chapter 4 - MCP Tools (Strands Agents)

Demonstrates the Model Context Protocol (MCP) using Strands.
Connects to a running MCP math server via Streamable HTTP transport.

Start the MCP server first (in a separate terminal):
    python mcp_math_server.py

Then run this script:
    python 03_mcp_tools.py

You can also test the server with the MCP Inspector:
    npx @modelcontextprotocol/inspector

You need to implement the MCP server first (mcp_math_server.py),
then connect to it from this script.
"""

import os

from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from terminal_loop import terminal_loop

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")

MCP_SERVER_URL = "http://localhost:8000/mcp"  # Streamable HTTP endpoint


def main():
    print("=" * 60)
    print("Chapter 4 - MCP Tools (Strands)")
    print("=" * 60)
    print()

    bedrock_model = BedrockModel(
        model_id=BEDROCK_MODEL_ID,
        region_name="eu-central-1",
    )

    # TODO: Connect to the running MCP math server via Streamable HTTP
    # Hint: Use MCPClient with streamablehttp_client
    #
    # mcp_client = MCPClient(
    #     lambda: streamablehttp_client(MCP_SERVER_URL)
    # )
    #
    # with mcp_client:
    #     tools = mcp_client.list_tools_sync()
    #     agent = Agent(model=bedrock_model, tools=tools, ...)
    #     terminal_loop(agent)

    print("Implement the MCP client setup above, then run this script again.")


if __name__ == "__main__":
    main()
