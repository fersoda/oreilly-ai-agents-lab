# Part 2b: Tool Use (Book Club - Chapter 4)

This module covers **Tool Use** concepts from Chapter 4, implemented with both **Strands Agents** and **LangChain** using AWS Bedrock.

## Structure

```
part-2b-tools-chapter/
├── strands/
│   ├── requirements.txt
│   ├── .env.example
│   ├── starter/           # Fill in the TODOs
│   │   ├── terminal_loop.py
│   │   ├── 01_local_tools.py
│   │   ├── 02_api_tools.py
│   │   ├── 03_mcp_tools.py
│   │   └── mcp_math_server.py
│   └── solution/          # Complete working examples
│       ├── terminal_loop.py
│       ├── 01_local_tools.py
│       ├── 02_api_tools.py
│       ├── 03_mcp_tools.py
│       └── mcp_math_server.py
├── langchain/
│   ├── requirements.txt
│   ├── .env.example
│   ├── starter/           # Fill in the TODOs
│   │   ├── 01_local_tools.py
│   │   ├── 02_api_tools.py
│   │   ├── 03_mcp_tools.py
│   │   └── mcp_math_server.py
│   └── solution/          # Complete working examples
│       ├── 01_local_tools.py
│       ├── 02_api_tools.py
│       ├── 03_mcp_tools.py
│       └── mcp_math_server.py
└── README.md
```

## Examples Covered

Each framework implements the same three examples from the chapter:

| # | Example | File | Description |
|---|---------|------|-------------|
| 1 | **Local Tools** | `01_local_tools.py` | Calculator tools (multiply, exponentiate, add) |
| 2 | **API-Based Tools** | `02_api_tools.py` | Wikipedia search + Stock price API |
| 3 | **MCP Tools** | `03_mcp_tools.py` | Math MCP server integration |

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 22.7.5+ (for MCP Inspector)
- AWS account with Bedrock access in eu-central-1 region

### 1. AWS Credentials

Configure your AWS credentials with access to Bedrock. Copy the `.env.example` file and fill in your values:

```bash
cp strands/.env.example strands/.env
cp langchain/.env.example langchain/.env
```

Then export your credentials:

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

---

## Strands Setup & Commands

### Setup

```bash
cd strands
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running Examples

```bash
# Local tools (calculator)
python solution/01_local_tools.py

# API-based tools (Wikipedia + stock price)
python solution/02_api_tools.py

# MCP tools — start the server first, then run the agent
# Terminal 1:
python solution/mcp_math_server.py

# Terminal 2:
python solution/03_mcp_tools.py
```

---

## LangChain Setup & Commands

### Setup

```bash
cd langchain
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running Examples

```bash
# Local tools (calculator)
python solution/01_local_tools.py

# API-based tools (Wikipedia + stock price)
python solution/02_api_tools.py

# MCP tools — start the server first, then run the agent
# Terminal 1:
python solution/mcp_math_server.py

# Terminal 2:
python solution/03_mcp_tools.py
```

---

## Debugging

### VS Code Debugger

1. Set a breakpoint by clicking left of any line number
2. Press `F5` and select **"Python: Current File"**

### Debug from Terminal (attach VS Code)

```bash
pip install debugpy
python -m debugpy --listen 5678 --wait-for-client solution/01_local_tools.py
```

Then in VS Code: Press `F5` → Select **"Python Debugger: Remote Attach"** → `localhost:5678`

### Python pdb (built-in)

```bash
python -m pdb solution/01_local_tools.py
```

Commands: `n` (next), `s` (step into), `c` (continue), `p variable` (print), `b 44` (breakpoint at line 44)

### Add breakpoint in code

```python
breakpoint()  # Pauses execution here
```

---

## MCP Inspector

Test and browse MCP tools interactively using the MCP Inspector.

### Connect to Running Server (Streamable HTTP)

**Terminal 1 — Start the MCP server:**
```bash
cd langchain/solution  # or strands/solution
python mcp_math_server.py
```

**Terminal 2 — Launch the inspector:**
```bash
npx --registry https://registry.npmjs.org @modelcontextprotocol/inspector
```

**In the browser UI:**
1. Select **Streamable HTTP** as transport type
2. Enter URL: `http://localhost:8000/mcp`
3. Click **Connect**

### Check Node.js Version

```bash
node -v && npm -v && npx -v
```

Requires Node.js 22.7.5+ (upgrade with `nvm install 22` or `n 22`)

---

## Key Concepts

### Local Tools
- Tools that run locally with predefined rules and logic
- Augment LLM weaknesses (arithmetic, date operations, etc.)
- Metadata (name, description, schema) is critical for the model to choose correctly

### API-Based Tools
- Enable agents to interact with external services
- Provide real-time data access (weather, stock prices, Wikipedia)
- Require error handling, rate limiting, and security considerations

### MCP Tools (Model Context Protocol)
- Open standard for connecting LLMs to external systems ("USB-C port for AI")
- MCP Server: exposes data/services via JSON-RPC 2.0
- MCP Client: agent that sends requests and receives structured responses
- Enables tool reuse across multiple agents without custom adapters
- Transport: Streamable HTTP on `http://localhost:8000/mcp`
