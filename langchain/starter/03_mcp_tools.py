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

You need to implement the MCP server first (mcp_math_server.py),
then connect to it from this script.
"""

import asyncio
import os

from langchain_aws import ChatBedrockConverse
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient

BEDROCK_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")


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

    server_script = os.path.join(os.path.dirname(__file__), "mcp_math_server.py")

    # TODO: Connect to the MCP math server via stdio (launches it as subprocess)
    # Hint:
    # mcp_client = MultiServerMCPClient(
    #     {
    #         "math": {
    #             "command": "python3",
    #             "args": [server_script],
    #             "transport": "stdio",
    #         },
    #     }
    # )
    # tools = await mcp_client.get_tools()
    # llm_with_tools = llm.bind_tools(tools)
    #
    # # Invoke the model with a math question
    # query = "What is 393 * 12.25? Also, what is 2 ^ 10?"
    # messages = [HumanMessage(query)]
    # ai_msg = llm_with_tools.invoke(messages)
    # messages.append(ai_msg)
    #
    # # Execute tool calls
    # tool_map = {t.name: t for t in tools}
    # for tool_call in ai_msg.tool_calls:
    #     selected_tool = tool_map[tool_call["name"]]
    #     tool_msg = await selected_tool.ainvoke(tool_call)
    #     messages.append(tool_msg)
    #
    # final_response = llm_with_tools.invoke(messages)
    # print(f"Final answer: {final_response.content}")

    print("Implement the MCP client setup above, then run this script again.")


def main():
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
