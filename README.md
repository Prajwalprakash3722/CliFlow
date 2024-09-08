# ClIFlow

Tired of manually writing CLI tools that make you yawn with boredom? Do you wish for a magical solution to generate CLI tools faster than a caffeine-fueled coder can type? Well, wish no more! a powerful tool designed to streamline the creation of CLI tools using Click. With CLIFlow , you can efficiently define, generate, and manage CLI tools through a simple YAML configuration, reducing manual coding and enhancing productivity.

## Features
- YAML Configuration: Define your CLI commands, options, and data processing logic in a straightforward YAML file.
- Automated Code Generation: Convert your YAML definitions into a Python script using Jinja2 and Click.
- Flexible Data Handling: Integrate data processing, including API calls and custom logic, seamlessly with your CLI tool.

## Getting Started

1. Define Your CLI in YAML
Create a YAML file (e.g., sample_cli.yaml) to outline your CLI’s structure and functionality.

Example YAML configuration:
```yaml
name: mycli
version: "1.0.0"
description: A CLI tool with API call and math operations
commands:
  - name: fetch_users
    description: Fetch user data from API
    options:
      results:
        description: Number of users to fetch
        type: int
    logic: |
      import requests
      response = requests.get("https://randomuser.me/api/", params={"results": results})
      data = response.json()
      for user in data["results"]:
          print(f"Name: {user['name']['first']} {user['name']['last']}")
          print(f"Email: {user['email']}")
          print(f"Country: {user['location']['country']}")

  - name: add
    description: Add two numbers
    options:
      a:
        description: First number
        type: float
      b:
        description: Second number
        type: float
    logic: |
      result = a + b
      print(f"Result: {result}")

  - name: multiply
    description: Multiply two numbers
    options:
      a:
        description: First number
        type: float
      b:****
        description: Second number
        type: float
    logic: |
      result = a * b
      print(f"Result: {result}")

```

2. Generate the CLI Tool
Run the python scripts to generate your CLI tool based on the YAML configuration.

```python3
python3 main.py
```

3. Execute Your CLI Tool
Use the generated CLI tool as follows:
```pytthon3
python output/mycli_cli.py fetch-users --results 5
```

Output: 
```bash
 python3 output/mycli_cli.py --help
 Usage: mycli_cli.py [OPTIONS] COMMAND [ARGS]...

 A CLI tool with API call and math operations

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  add          Add two numbers
  fetch-users  Fetch user data from API
  multiply     Multiply two numbers
```

## TODO:
- add subcommands for commands
- develop a frontend where one can completely generate a no-code cli tools, just by adding a few details.

## Suggestions
This logic was coded in a whim, if anyone has better idea to generate the cli tools, please don't hesistate to make a PR.
