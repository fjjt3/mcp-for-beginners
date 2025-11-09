"""
Complete Python MCP Client Example

This client demonstrates how to:
1. Connect to an MCP server using stdio transport
2. List available tools and resources
3. Call calculator tools (add, subtract, multiply, divide)
4. Call greet tool
5. Call read_text tool
6. Handle responses from the server
"""

import asyncio
import json
import sys
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client


class MCPCalculatorClient:
    def __init__(self):
        # Create server parameters for stdio connection
        self.server_params = StdioServerParameters(
            command=sys.executable,  # Use the current Python interpreter
            args=["server.py"],  # Server script in the current directory
            env=None,  # Optional environment variables
        )

    async def run(self):
        """Main client execution function"""
        print("🚀 Starting MCP Python Client...")

        try:
            async with stdio_client(self.server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    print("📡 Connecting to MCP server...")
                    
                    # Initialize the connection
                    await session.initialize()
                    print("✅ Connected to MCP server successfully!")

                    # List available tools
                    await self.list_tools(session)
                    
                    # Test calculator operations
                    await self.test_calculator_operations(session)
                    
                    # Test greet tool
                    await self.test_greet_tool(session)
                    
                    # Test read_text tool
                    await self.test_read_text_tool(session)
                    
                    # List and test resources
                    await self.list_and_test_resources(session)
                    
                    print("\n✨ Client operations completed successfully!")

        except Exception as e:
            print(f"❌ Error running MCP client: {e}")
            raise

    async def list_tools(self, session: ClientSession):
        """List all available tools on the server"""
        print("\n📋 Listing available tools:")
        try:
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
        except Exception as e:
            print(f"  Error listing tools: {e}")

    async def test_calculator_operations(self, session: ClientSession):
        """Test various calculator operations"""
        print("\n🧮 Testing Calculator Operations:")

        operations = [
            ("add", {"a": 5, "b": 3}, "Add 5 + 3"),
            ("subtract", {"a": 10, "b": 4}, "Subtract 10 - 4"),
            ("multiply", {"a": 6, "b": 7}, "Multiply 6 × 7"),
            ("divide", {"a": 20, "b": 4}, "Divide 20 ÷ 4"),
        ]

        for tool_name, arguments, description in operations:
            try:
                result = await session.call_tool(tool_name, arguments=arguments)
                result_text = self.extract_text_result(result)
                
                if tool_name == "help":
                    print(f"\n📖 {description}:")
                    print(result_text)
                else:
                    print(f"{description} = {result_text}")
                    
            except Exception as e:
                print(f"  Error calling {tool_name}: {e}")

    async def test_greet_tool(self, session: ClientSession):
        """Test the greet tool"""
        print("\n👋 Testing Greet Tool:")
        try:
            result = await session.call_tool("greet", arguments={"name": "Juan"})
            result_text = self.extract_text_result(result)
            print(f"  {result_text}")
        except Exception as e:
            print(f"  Error calling greet: {e}")

    async def test_read_text_tool(self, session: ClientSession):
        """Test the read_text tool"""
        print("\n📖 Testing Read Text Tool:")
        try:
            test_text = "Este es un texto de prueba para la herramienta read_text"
            result = await session.call_tool("read_text", arguments={"text": test_text})
            result_text = self.extract_text_result(result)
            print(f"  {result_text}")
        except Exception as e:
            print(f"  Error calling read_text: {e}")

    async def list_and_test_resources(self, session: ClientSession):
        """List and test reading resources"""
        print("\n📄 Listing available resources:")
        try:
            resources = await session.list_resources()
            for resource in resources.resources:
                print(f"  - {resource.name}: {resource.description}")
                print(f"    URI: {resource.uri}")

            # Test reading a resource if available
            if resources.resources:
                first_resource = resources.resources[0]
                print(f"\n📖 Reading resource: {first_resource.name}")
                try:
                    content = await session.read_resource(first_resource.uri)
                    print(f"Resource content: {content}")
                except Exception as e:
                    print(f"  Error reading resource: {e}")
            else:
                print("  No resources available")
                
        except Exception as e:
            print(f"  Error listing resources: {e}")

    def extract_text_result(self, result) -> str:
        """
        Extract text content from a tool result object.

        This method attempts to extract the text content from the `content` attribute
        of the result object. If no text content is found, it falls back to converting
        the result to a string. If an error occurs during extraction, it returns "No result".

        Args:
            result: The result object returned by a tool, which may contain a `content` attribute
                    with text or other types of data.

        Returns:
            A string representing the extracted text content, or a fallback string if no text is found.
        """
        try:
            if hasattr(result, 'content') and result.content:
                for content_item in result.content:
                    if hasattr(content_item, 'text') and content_item.text:
                        return content_item.text
                    elif hasattr(content_item, 'type') and content_item.type == "text":
                        return getattr(content_item, 'text', str(content_item))
            
            # Fallback: try to convert to string
            return str(result)
        except Exception:
            return "No result"


async def main():
    """Entry point for the client"""
    client = MCPCalculatorClient()
    await client.run()


if __name__ == "__main__":
    asyncio.run(main())