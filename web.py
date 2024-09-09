from aiohttp import web
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CLI_DB = {
    "maths": {
        "version": "1.0.0",
        "description": "A CLI tool with API call and math operations",
        "commands": [
            {
                "name": "calc",
                "description": "Calc",
                "options": {},
                "logic": 'print("Hello World")',
                "subcommands": [
                    {
                        "name": "add",
                        "description": "add",
                        "options": {
                            "a": {"description": "a", "type": "float"},
                            "b": {"description": "b", "type": "float"},
                        },
                        "logic": "print(a+b)",
                    }
                ],
            }
        ],
    },
    "mathutil": {
        "name": "mathutil",
        "version": "2.0.0",
        "description": "A CLI tool for mathematical and utility operations",
        "commands": [
            {
                "name": "math",
                "description": "Perform mathematical operations",
                "subcommands": [
                    {
                        "name": "basic",
                        "description": "Basic math operations",
                        "subcommands": [
                            {
                                "name": "add",
                                "description": "Add two numbers",
                                "options": {
                                    "a": {
                                        "description": "First number",
                                        "type": "float",
                                        "required": True,
                                    },
                                    "b": {
                                        "description": "Second number",
                                        "type": "float",
                                        "required": True,
                                    },
                                },
                                "logic": "print(f'{a} + {b} = {a + b}')",
                            },
                            {
                                "name": "subtract",
                                "description": "Subtract two numbers",
                                "options": {
                                    "a": {
                                        "description": "First number",
                                        "type": "float",
                                        "required": True,
                                    },
                                    "b": {
                                        "description": "Second number",
                                        "type": "float",
                                        "required": True,
                                    },
                                },
                                "logic": "print(f'{a} - {b} = {a - b}')",
                            },
                        ],
                    },
                    {
                        "name": "advanced",
                        "description": "Advanced math operations",
                        "subcommands": [
                            {
                                "name": "power",
                                "description": "Calculate power of a number",
                                "options": {
                                    "base": {
                                        "description": "Base number",
                                        "type": "float",
                                        "required": True,
                                    },
                                    "exponent": {
                                        "description": "Exponent",
                                        "type": "float",
                                        "required": True,
                                    },
                                },
                                "logic": "print(f'{base}^{exponent} = {base ** exponent}')",
                            },
                            {
                                "name": "sqrt",
                                "description": "Calculate square root",
                                "options": {
                                    "number": {
                                        "description": "Number to find square root of",
                                        "type": "float",
                                        "required": True,
                                    },
                                },
                                "logic": "import math\nprint(f'√{number} = {math.sqrt(number)}')",
                            },
                        ],
                    },
                ],
            },
            {
                "name": "util",
                "description": "Utility operations",
                "subcommands": [
                    {
                        "name": "string",
                        "description": "String operations",
                        "subcommands": [
                            {
                                "name": "reverse",
                                "description": "Reverse a string",
                                "options": {
                                    "text": {
                                        "description": "Text to reverse",
                                        "type": "str",
                                        "required": True,
                                    },
                                },
                                "logic": "print(f'Reversed: {text[::-1]}')",
                            },
                            {
                                "name": "count",
                                "description": "Count characters in a string",
                                "options": {
                                    "text": {
                                        "description": "Text to count characters",
                                        "type": "str",
                                        "required": True,
                                    },
                                },
                                "logic": "print(f'Character count: {len(text)}')",
                            },
                        ],
                    },
                    {
                        "name": "convert",
                        "description": "Conversion operations",
                        "subcommands": [
                            {
                                "name": "celsius_to_fahrenheit",
                                "description": "Convert Celsius to Fahrenheit",
                                "options": {
                                    "celsius": {
                                        "description": "Temperature in Celsius",
                                        "type": "float",
                                        "required": True,
                                    },
                                },
                                "logic": "fahrenheit = (celsius * 9/5) + 32\nprint(f'{celsius}°C = {fahrenheit}°F')",
                            },
                            {
                                "name": "kilometers_to_miles",
                                "description": "Convert Kilometers to Miles",
                                "options": {
                                    "km": {
                                        "description": "Distance in kilometers",
                                        "type": "float",
                                        "required": True,
                                    },
                                },
                                "logic": "miles = km * 0.621371\nprint(f'{km} km = {miles} miles')",
                            },
                        ],
                    },
                ],
            },
        ],
    },
}


def find_command(cli_data, command_path):
    logger.info(f"Searching for command: {command_path}")
    current_level = cli_data
    for i, path_part in enumerate(command_path):
        found = False
        if i == 0:
            for command in current_level.get("commands", []):
                if command["name"] == path_part:
                    current_level = command
                    found = True
                    break
        else:
            for subcommand in current_level.get("subcommands", []):
                if subcommand["name"] == path_part:
                    current_level = subcommand
                    found = True
                    break
        if not found:
            logger.error(f"Command not found at level {i}: {path_part}")
            return None
    return current_level


async def get_command_details(request):
    cli_name = request.match_info.get("cli_name")
    command_path = request.match_info.get("command_path", "").split("/")

    logger.info(f"Received request for CLI: {cli_name}, Command Path: {command_path}")

    cli_data = CLI_DB.get(cli_name)
    if not cli_data:
        logger.error(f"CLI not found: {cli_name}")
        return web.json_response({"error": "CLI not found"}, status=404)

    command = find_command(cli_data, command_path)

    if command:
        logger.info(f"Command found: {command['name']}")
        return web.json_response(command)
    else:
        logger.error(f"Command not found: {' '.join(command_path)}")
        return web.json_response({"error": "Command not found"}, status=404)


app = web.Application()
app.add_routes([web.get("/cli/{cli_name}/{command_path:.*}", get_command_details)])

if __name__ == "__main__":
    logger.info("Starting server on port 8080")
    web.run_app(app, port=8080)
