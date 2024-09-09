import click

@click.group()
@click.version_option("1.0.0")
def cli():
    """A CLI Tool to say hello and bye"""
    pass


@cli.command()

@click.option('--name', help='Name of the user', type=str)

def hello(name):
    """Says Hello to the user"""
    
    
    
    print(f"Hello from Amith {name}")
    
    


@cli.command()

@click.option('--name', help='Name of the user', type=str)

def bye(name):
    """Says Good bye to the user"""
    
    
    
    print(f"Bye bro, {name}")
    
    



if __name__ == '__main__':
    cli()