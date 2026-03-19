"""
MCP Math Server

A simple MCP server that exposes calculator operations (add, multiply, exponentiate)
via the Model Context Protocol using SSE transport.

Run this server as a standalone process:
    python mcp_math_server.py

Then test it with the MCP Inspector:
    npx @modelcontextprotocol/inspector

TODO: Implement the three math tools below using @mcp.tool()
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math Tools")


# TODO: Implement the add tool
# @mcp.tool()
# def add(x: float, y: float) -> float:
#     """Add two numbers together."""
#     ...


# TODO: Implement the multiply tool


# TODO: Implement the exponentiate tool


if __name__ == "__main__":
    mcp.run(transport="streamable-http")  # Streamable HTTP on port 8000
