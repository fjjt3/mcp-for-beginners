# Proyecto MCP (Model Context Protocol) - Calculadora

Este proyecto es un ejemplo de cómo usar el protocolo MCP (Model Context Protocol) para crear un servidor y cliente que se comunican mediante stdio (entrada/salida estándar).

## ¿Qué es MCP?

MCP (Model Context Protocol) es un protocolo que permite a las aplicaciones comunicarse con servidores que proporcionan herramientas (tools) y recursos (resources). En este caso, creamos un servidor de calculadora que puede realizar operaciones matemáticas básicas.

## Estructura del Proyecto

### `server.py` - Servidor MCP
El servidor expone:
- **Herramientas (Tools)**: Funciones que el cliente puede llamar
  - `add(a, b)`: Suma dos números
  - `subtract(a, b)`: Resta dos números
  - `multiply(a, b)`: Multiplica dos números
  - `divide(a, b)`: Divide dos números
  - `greet(name)`: Saluda a alguien por nombre
  - `read_text(text)`: Lee y muestra contenido de texto

- **Recursos (Resources)**: Datos que el cliente puede leer
  - `greeting://{name}`: Genera un saludo personalizado

### `client.py` - Cliente MCP
El cliente:
1. Se conecta al servidor usando stdio
2. Lista todas las herramientas disponibles
3. Prueba las operaciones de calculadora
4. Prueba la herramienta de saludo (greet)
5. Prueba la herramienta de lectura de texto (read_text)
6. Lista y lee los recursos disponibles

## Cómo Ejecutar el Proyecto

### 1. Activar el entorno virtual

En PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

Si tienes problemas con la política de ejecución, ejecuta primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Ejecutar el cliente

El cliente se conectará automáticamente al servidor:
```powershell
python client.py
```

O si usas `py`:
```powershell
py client.py
```

### 3. Ver la salida

El cliente mostrará:
- ✅ Lista de herramientas disponibles
- 🧮 Resultados de las operaciones matemáticas
- 📄 Lista de recursos disponibles
- 📖 Contenido de los recursos

## Flujo de Comunicación

1. El cliente inicia y crea una conexión stdio con el servidor
2. El servidor se ejecuta como un proceso hijo
3. El cliente envía solicitudes JSON-RPC al servidor
4. El servidor procesa las solicitudes y devuelve respuestas
5. El cliente muestra los resultados

## Ejemplo de Salida

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

## Dependencias

Las dependencias están en `requirements.txt`:
- `mcp`: Librería principal del protocolo MCP
- `fastmcp`: Framework para crear servidores MCP rápidamente

## Notas

- El servidor se ejecuta automáticamente cuando el cliente se conecta
- La comunicación se realiza mediante stdin/stdout (stdio)
- No se requiere configuración adicional de red o puertos


