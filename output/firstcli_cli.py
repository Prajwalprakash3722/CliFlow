import click

@click.group()
@click.version_option("1.0.0")
def cli():
    """A CLI tool with API call and math operations"""
    pass


@cli.command()

@click.option('--name', help='name of the user', type=str)

@click.option('--age', help='Age of the user', type=int)

def add_user(name, age):
    """adds a user to database"""
    
    
    
    print("User Successfully added to the DB")
    
    print(name)
    
    print(age)
    
    



if __name__ == '__main__':
    cli()