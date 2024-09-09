import click
import sys

@click.group(help="A CLI tool with API call and math operations")
@click.version_option("1.0.0")
def cli():
    """A CLI tool with API call and math operations"""
    pass



# Command with subcommands
@cli.group()
def calc():
    """Calc"""
    pass


@calc.command()

@click.option('-a', '--a', help='a', type=float, required=True)

@click.option('-b', '--b', help='b', type=float, required=True)

def add(a, b):
    """add"""
    
    
    
    print(a+b)
    
    





if __name__ == '__main__':
    cli()