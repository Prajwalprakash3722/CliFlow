import click

@click.group()
@click.version_option("1.0.0")
def cli():
    """A CLI tool with API call and math operations"""
    pass


@cli.command()

def mode():
    """adds a user to database"""
    
    
    
    print("hello world")
    
    



if __name__ == '__main__':
    cli()