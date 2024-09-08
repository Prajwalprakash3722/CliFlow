import ast
from parser.yaml_parser import CLIParser

import streamlit as st

from generator.gen import PythonGenerator


class StreamlitCLIParser(CLIParser):
    def __init__(self, cli_structure):
        self.cli_structure = cli_structure

    def parse(self):
        return self.cli_structure


def check_syntax(logic):
    try:
        ast.parse(logic)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def main():
    st.title("CLI Flow")

    cli_name = st.text_input("CLI Name", placeholder="Enter CLI name (e.g., mycli)")
    cli_version = st.text_input("Version", "1.0.0", help="Specify the CLI version.")
    cli_description = st.text_area(
        "Description",
        "A CLI tool with API call and math operations",
        help="Provide a brief description of the CLI tool.",
    )

    # Commands
    commands = []
    if "num_commands" not in st.session_state:
        st.session_state.num_commands = 0

    if st.button("Add Command"):
        st.session_state.num_commands += 1

    for i in range(st.session_state.num_commands):
        st.subheader(f"Command {i+1}")
        command_name = st.text_input(
            f"Command Name {i+1}", key=f"cmd_name_{i}", placeholder="e.g., add_user"
        )
        command_description = st.text_input(
            f"Command Description {i+1}",
            key=f"cmd_desc_{i}",
            placeholder="Brief description of the command",
        )

        # Options for the command
        options = {}
        num_options = st.number_input(
            f"Number of options for Command {i+1}",
            min_value=0,
            max_value=10,
            value=0,
            step=1,
            key=f"num_options_{i}",
        )

        for j in range(num_options):
            st.text(f"Option {j+1} for Command {i+1}")
            option_name = st.text_input(
                f"Option Name {i+1}.{j+1}",
                key=f"opt_name_{i}_{j}",
                placeholder="e.g., --user",
            )
            option_description = st.text_input(
                f"Option Description {i+1}.{j+1}",
                key=f"opt_desc_{i}_{j}",
                placeholder="Description of the option",
            )
            option_type = st.selectbox(
                f"Option Type {i+1}.{j+1}",
                ["int", "float", "str"],
                key=f"opt_type_{i}_{j}",
                help="Specify the option type.",
            )

            options[option_name] = {
                "description": option_description,
                "type": option_type,
            }

        command_logic = st.text_area(
            f"Command Logic {i+1}",
            key=f"cmd_logic_{i}",
            height=150,
            placeholder="Enter Python logic for the command",
            value='print("Hello World")',
        )
        # Check syntax of Python code
        valid_syntax, syntax_error = check_syntax(command_logic)
        if not valid_syntax:
            st.error(f"Syntax Error in Command {i+1} Logic: {syntax_error}")

        commands.append(
            {
                "name": command_name,
                "description": command_description,
                "options": options,
                "logic": command_logic
                if valid_syntax
                else "",
            }
        )

    if st.button("Generate CLI"):
        cli_structure = {
            "name": cli_name,
            "version": cli_version,
            "description": cli_description,
            "commands": commands,
        }
        if all([cmd["name"] and cmd["logic"] for cmd in commands]):
            parser = StreamlitCLIParser(cli_structure)
            parsed_structure = parser.parse()
            generator = PythonGenerator(parsed_structure)
            generator.generate()
            st.success("CLI tool generated successfully!")
        else:
            st.warning("Please ensure all commands have valid names and logic.")

        # Display the structure for review
        st.subheader("Generated CLI Structure")
        st.json(cli_structure)


if __name__ == "__main__":
    main()
