import click

@click.group()
@click.version_option("1.0.0")
def cli():
    """A CLI tool with API call and math operations"""
    pass


@cli.command()

@click.option('--a', help='First Number', type=float)

@click.option('--b', help='Second Number', type=float)

def add(a, b):
    """Adds 2 numbers"""
    
    
    
    print(a+b)
    
    



if __name__ == '__main__':
    cli()