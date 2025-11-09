# MCP (Model Context Protocol) Project - Calculator

This project is an example of how to use the MCP (Model Context Protocol) to create a server and client that communicate via stdio (standard input/output).

## What is MCP?

MCP (Model Context Protocol) is a protocol that allows applications to communicate with servers that provide tools and resources. In this case, we create a calculator server that can perform basic mathematical operations.

## Project Structure

### `server.py` - MCP Server
The server exposes:
- **Tools**: Functions that the client can call
  - `add(a, b)`: Add two numbers
  - `subtract(a, b)`: Subtract two numbers
  - `multiply(a, b)`: Multiply two numbers
  - `divide(a, b)`: Divide two numbers
  - `greet(name)`: Greet someone by name
  - `read_text(text)`: Read and display text content

- **Resources**: Data that the client can read
  - `greeting://{name}`: Generates a personalized greeting

### `client.py` - MCP Client
The client:
1. Connects to the server using stdio
2. Lists all available tools
3. Tests calculator operations
4. Tests the greet tool
5. Tests the read_text tool
6. Lists and reads available resources

## How to Run the Project

### 1. Activate the virtual environment

In PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

If you have issues with the execution policy, run first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Run the client

The client will automatically connect to the server:
```powershell
python client.py
```

Or if you use `py`:
```powershell
py client.py
```

### 3. View the output

The client will display:
- ✅ List of available tools
- 🧮 Results of mathematical operations
- 📄 List of available resources
- 📖 Resource content

## Communication Flow

1. The client starts and creates a stdio connection with the server
2. The server runs as a child process
3. The client sends JSON-RPC requests to the server
4. The server processes the requests and returns responses
5. The client displays the results

## Example Output

```
🚀 Starting MCP Python Client...
📡 Connecting to MCP server...
✅ Connected to MCP server successfully!

📋 Listing available tools:
  - add: Add two numbers
  - subtract: Subtract two numbers
  - multiply: Multiply two numbers
  - divide: Divide two numbers
  - greet: Greet someone by name
  - read_text: Read and display text content

🧮 Testing Calculator Operations:
Add 5 + 3 = 8
Subtract 10 - 4 = 6
Multiply 6 × 7 = 42
Divide 20 ÷ 4 = 5.0

👋 Testing Greet Tool:
  ¡Hola, Juan! ¿Cómo estás?

📖 Testing Read Text Tool:
  Texto leído: Este es un texto de prueba para la herramienta read_text

📄 Listing available resources:
  No resources available

✨ Client operations completed successfully!
```

## Dependencies

Dependencies are in `requirements.txt`:
- `mcp`: Main MCP protocol library
- `fastmcp`: Framework for quickly creating MCP servers

## Notes

- The server runs automatically when the client connects
- Communication is done via stdin/stdout (stdio)
- No additional network or port configuration is required


