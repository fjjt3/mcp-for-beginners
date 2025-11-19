# MCP (Model Context Protocol) Project - Calculator

This project is an example of how to use the MCP (Model Context Protocol) to create a server and client that communicate via stdio (standard input/output).

## What is MCP?

MCP (Model Context Protocol) is a protocol that allows applications to communicate with servers that provide tools and resources. In this case, we create a calculator server that can perform basic mathematical operations.

## Project Structure

### `server.py` - MCP Server
The server uses **FastMCP** to expose:
- **Tools**: Functions that the client can call
  - `add(a, b)`: Add two numbers
  - `subtract(a, b)`: Subtract two numbers
  - `multiply(a, b)`: Multiply two numbers
  - `divide(a, b)`: Divide two numbers
  - `greet(name)`: Greet someone by name
  - `read_text(text)`: Read and display text content

- **Resources**: Data that the client can read
  - `greeting://{name}`: Generates a personalized greeting

### `client.py` - MCP Client with LLM
The client:
1. Connects to `server.py` using stdio.
2. Lists available tools and converts them to an LLM-compatible schema.
3. Connects to **Azure AI Inference** (using GitHub Models).
4. Sends a prompt ("Add 2 to 20") to the LLM.
5. Receives the tool call instruction from the LLM.
6. Executes the tool on the MCP server and displays the result.

## How to Run the Project

### 1. Activate the virtual environment

On macOS/Linux:
```bash
source venv/bin/activate
```

On Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

If you have issues with the execution policy on Windows, run first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Set up your GitHub Token

You need a GitHub Personal Access Token to use the LLM models.

On macOS/Linux:
```bash
export GITHUB_TOKEN="your_github_token_here"
```

On Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

### 3. Run the client

The client will automatically connect to the server:
```bash
python client.py
# or
python3 client.py
```

On Windows you can also use:
```powershell
py client.py
```

### 4. View the output

The client will display:
- ✅ List of available tools
- 🔄 Converted tool schemas
- 🤖 Calling LLM...
- 🛠️ Tool execution result (e.g., "22")

## Dependencies

Dependencies are in `requirements.txt`:
- `mcp`: Main MCP protocol library
- `fastmcp`: Framework for quickly creating MCP servers
- `azure-ai-inference`: Client library for Azure AI Inference (GitHub Models)

## Notes

- The server (`server.py`) runs automatically as a subprocess when the client (`client.py`) connects.
- Communication is done via stdin/stdout (stdio).
- Requires Python 3.10+ due to `fastmcp` dependencies.


