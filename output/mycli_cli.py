import click
import sys

@click.group()
@click.version_option("1.0.0")

def cli():
    """A CLI tool with API call and math operations"""
    pass


@cli.command()

@click.option('-r', '--results', help='Number of users to fetch', type=int, required=True)

def fetch_users(results):
    """Fetch user data from API"""
    if not all([results]):
        print(f"Error: Missing required arguments for command 'fetch_users'.")
        print(f"Usage: python script_name.py fetch_users [OPTIONS]")
        print(f"Try 'python script_name.py fetch_users --help' for more information.")
        sys.exit(1)
    
    
    
    
    import requests
    
    response = requests.get("https://randomuser.me/api/", params={"results": results})
    
    data = response.json()
    
    for user in data["results"]:
    
        print(f"Name: {user['name']['first']} {user['name']['last']}")
    
        print(f"Email: {user['email']}")
    
        print(f"Country: {user['location']['country']}")
    
    

@cli.command()

@click.option('-a', '--a', help='First number', type=float, required=True)

@click.option('-b', '--b', help='Second number', type=float, required=True)

def add(a, b):
    """Add two numbers"""
    if not all([a, b]):
        print(f"Error: Missing required arguments for command 'add'.")
        print(f"Usage: python script_name.py add [OPTIONS]")
        print(f"Try 'python script_name.py add --help' for more information.")
        sys.exit(1)
    
    
    
    
    result = a + b
    
    print(f"Result: {result}")
    
    

@cli.command()

@click.option('-a', '--a', help='First number', type=float, required=True)

@click.option('-b', '--b', help='Second number', type=float, required=True)

def multiply(a, b):
    """Multiply two numbers"""
    if not all([a, b]):
        print(f"Error: Missing required arguments for command 'multiply'.")
        print(f"Usage: python script_name.py multiply [OPTIONS]")
        print(f"Try 'python script_name.py multiply --help' for more information.")
        sys.exit(1)
    
    
    
    
    result = a * b
    
    print(f"Result: {result}")
    
    


if __name__ == '__main__':
    cli()