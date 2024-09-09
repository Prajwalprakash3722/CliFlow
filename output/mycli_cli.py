import click
import sys

@click.group(help="A CLI tool with commands and subcommands")
@click.version_option("1.0.0")
def cli():
    """A CLI tool with commands and subcommands"""
    pass



# Command with subcommands
@cli.group()
def user():
    """User-related operations"""
    pass


@user.command()

@click.option('-u', '--username', help='Username of the new user', type=str, required=True)

def add(username):
    """Add a new user"""
    
    
    
    print(f"Adding user: {username}")
    
    

@user.command()

@click.option('-u', '--username', help='Username of the user to delete', type=str, required=True)

def delete(username):
    """Delete an existing user"""
    
    
    
    print(f"Deleting user: {username}")
    
    





# Command without subcommands
@cli.command()

@click.option('-v', '--verbose', help='Enable verbose output', type=bool, required=True)

def status(verbose):
    """Check system status"""
    
    
    
    if verbose:
    
        print("System status: verbose mode")
    
    else:
    
        print("System status: normal")
    
    



if __name__ == '__main__':
    cli()