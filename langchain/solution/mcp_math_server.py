"""
MCP Math Server

A simple MCP server that exposes calculator operations (add, multiply, exponentiate)
via the Model Context Protocol using SSE transport.

Run this server as a standalone process:
    python mcp_math_server.py

Then test it with the MCP Inspector:
    npx @modelcontextprotocol/inspector

Or connect the agent to it:
    python 03_mcp_tools.py
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math Tools")


@mcp.tool()
def add(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


@mcp.tool()
def multiply(x: float, y: float) -> float:
    """Multiply two numbers together."""
    return x * y


@mcp.tool()
def exponentiate(x: float, y: float) -> float:
    """Raise x to the power of y."""
    return x ** y


if __name__ == "__main__":
    mcp.run(transport="streamable-http")  # Streamable HTTP on port 8000
