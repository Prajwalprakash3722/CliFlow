import click

@click.group()
@click.version_option("1.0.0")
def cli():
    """A CLI tool with API call and math operations"""
    pass


@cli.command()

@click.option('--results', help='Number of users to fetch', type=int)

def fetch_users(results):
    """Fetch user data from API"""
    
    
    
    import requests
    
    response = requests.get("https://randomuser.me/api/", params={"results": results})
    
    data = response.json()
    
    for user in data["results"]:
    
        print(f"Name: {user['name']['first']} {user['name']['last']}")
    
        print(f"Email: {user['email']}")
    
        print(f"Country: {user['location']['country']}")
    
    


@cli.command()

@click.option('--a', help='First number', type=float)

@click.option('--b', help='Second number', type=float)

def add(a, b):
    """Add two numbers"""
    
    
    
    result = a + b
    
    print(f"Result: {result}")
    
    


@cli.command()

@click.option('--a', help='First number', type=float)

@click.option('--b', help='Second number', type=float)

def multiply(a, b):
    """Multiply two numbers"""
    
    
    
    result = a * b
    
    print(f"Result: {result}")
    
    



if __name__ == '__main__':
    cli()