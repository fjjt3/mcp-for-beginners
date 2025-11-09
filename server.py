# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add calculator tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Add a greet tool
@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"¡Hola, {name}! ¿Cómo estás?"


# Add a read_text tool
@mcp.tool()
def read_text(text: str) -> str:
    """Read and display text content"""
    return f"Texto leído: {text}"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Run the server
if __name__ == "__main__":
    mcp.run()
