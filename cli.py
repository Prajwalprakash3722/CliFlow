from parser.yaml_parser import CLIParser
from generator.gen import PythonGenerator

def main():
    parser = CLIParser('examples/sample_cli.yaml')
    cli_structure = parser.parse()

    generator = PythonGenerator(cli_structure)
    generator.generate()
    print("CLI tool generated successfully!")

if __name__ == "__main__":
    main()