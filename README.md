# CLIFlow 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

> Generate CLI tools faster than you can say "Command Line Interface"!

Tired of manually crafting CLI tools that put you to sleep? CLIFlow is your magical solution to generate CLI tools quicker than a LLM.

## 🌟 Features

- 📝 **YAML Configuration**: Define your CLI structure with ease
- 🚀 **Automated Code Generation**: From YAML to Python in seconds
- 🔧 **Flexible Data Handling**: Seamlessly integrate API calls and custom logic
- 🖥️ **Streamlit Frontend**: For those who prefer clicking to coding

## 🚀 Quick Start

### 1. Define Your CLI in YAML

Create a `sample_cli.yaml` file:

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
      b:
        description: Second number
        type: float
    logic: |
      result = a * b
      print(f"Result: {result}")
```

### 2. Generate the CLI Tool

```bash
python3 cli.py
```

### 3. Execute Your CLI Tool

```bash
python output/mycli_cli.py fetch-users --results 5
```

## 💻 Usage

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

## 🎨 Frontend

For a more visual experience, CLIFlow offers a Streamlit-based frontend:

```bash
python3 main.py
```

This opens a web portal where you can define all the fields needed and generate CLI apps with just a few clicks!

## 🛠️ Installation

```bash
git clone https://github.com/Prajwalprakash3722/CliFlow
cd cliflow
pip install -r requirements.txt
```

## 📝 TODO
****
- [ ] Add subcommands for commands
- [x] Develop a frontend for no-code CLI tool generation

## 🤝 Contributing

This approch was coded in a whim, If anyone has better approch or have ideas to improve CLIFlow or generate CLI tools more efficiently, please don't hesitate to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by [Prajwal P]