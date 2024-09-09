import click
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_command_details(cli_name, command_path):
    actual_command_path = []
    for arg in command_path:
        if arg.startswith('-'):
            break
        actual_command_path.append(arg)
    command_url = f"http://localhost:8080/cli/{cli_name}/{'/'.join(actual_command_path)}"
    logger.debug(f"Fetching command details from: {command_url}")
    response = requests.get(command_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
        return None

def generate_command(command_details):
    @click.command()
    @click.pass_context
    def dynamic_command(ctx, **kwargs):
        logic = command_details.get('logic', '')
        if logic:
            logger.debug(f"Executing logic: {logic}")
            exec(logic, globals(), kwargs)
        else:
            logger.warning("No logic found for this command")

    for option_name, option in command_details.get('options', {}).items():
        option_flag = f"--{option_name}"
        option_type = eval(option["type"])
        dynamic_command = click.option(
            option_flag, 
            type=option_type, 
            required=option.get('required', False),
            help=option.get('description', '')
        )(dynamic_command)

    return dynamic_command

def format_help_message(cli_name, command_structure, indent=0):
    help_message = []
    if indent == 0:
        help_message.append(f"Usage: python3 parent.py {cli_name} [COMMAND] [OPTIONS]")
        help_message.append(f"\nCLI tool: {command_structure.get('description', '')}")
        help_message.append("\nAvailable commands:")

    for command in command_structure.get('commands', []):
        help_message.append(f"{'  ' * indent}{command['name']}: {command.get('description', '')}")
        if 'subcommands' in command:
            help_message.extend(format_help_message(cli_name, command, indent + 1))

    return help_message

class CustomCommand(click.Command):
    def get_help(self, ctx):
        cli_name = ctx.params.get('cli_name')
        if cli_name:
            command_structure = fetch_command_details(cli_name, [])
            if command_structure:
                help_message = format_help_message(cli_name, command_structure)
                return '\n'.join(help_message)
        return super().get_help(ctx)

@click.command(cls=CustomCommand, context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.argument('cli_name', required=False)
@click.argument('command_path', nargs=-1)
@click.pass_context
def cli(ctx, cli_name, command_path):
    if not cli_name:
        click.echo(ctx.get_help())
        ctx.exit()

    logger.debug(f"CLI Name: {cli_name}, Command Path: {command_path}")

    command_details = fetch_command_details(cli_name, command_path)
    
    if command_details:
        dynamic_cmd = generate_command(command_details)
        
        args = list(command_path)
        for i, arg in enumerate(args):
            if arg.startswith('-'):
                args = args[i:]
                break
        else:
            args = []
        logger.debug(f"Args to be passed to dynamic command: {args}")
        
        dynamic_cmd.main(args, standalone_mode=False)
    else:
        logger.error(f"Command not found: {cli_name} {' '.join(command_path)}")

if __name__ == '__main__':
    cli()