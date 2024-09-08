import os
from jinja2 import Environment, FileSystemLoader

class PythonGenerator:
    def __init__(self, cli_structure):
        self.cli_structure = cli_structure
        self.env = Environment(loader=FileSystemLoader('templates'))

    def generate(self):

        template = self.env.get_template("cli_template.py.jinja2")
        rendered_code = template.render(**self.cli_structure)
        
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        
        with open(os.path.join(output_dir, f"{self.cli_structure['name']}_cli.py"), 'w') as file:
            file.write(rendered_code)

    # TODO
    def _sanitize_operations(self, operations):
        return operations