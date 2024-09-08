import click

@click.group()
@click.version_option("1.0.0")
def cli():
    """A CLI tool to parse and analyze Nginx access and error logs"""
    pass


@cli.command()

@click.option('--log_file', help='Path to the Nginx access log file', type=str)

@click.option('--elog_file', help='Path to the Nginx error log file', type=str)

@click.option('--mode', help='Mode of operation (before or after applying the config update)', type=str)

@click.option('--duration', help='Duration to listen to the logs in seconds', type=int)

@click.option('--meta_file', help='Path to the meta file for storing results', type=str)

@click.option('--vhost', help='Comma-separated list of vhosts to filter logs by', type=str)

@click.option('--deviation_threshold', help='Threshold percentage for printing deviations', type=float)

@click.option('--monitor_codes', help='Comma-separated list of status codes or regex patterns to monitor for deviations', type=str)

@click.option('--log_level', help='Logging level (DEBUG, INFO)', type=str)

@click.option('--full', help='If set, the script will parse the entire Nginx access/error logs', type=bool)

def parse_logs(log_file, elog_file, mode, duration, meta_file, vhost, deviation_threshold, monitor_codes, log_level, full):
    """Parse Nginx access and error logs"""
    
    
    
    import os
    
    import re
    
    import json
    
    import logging
    
    import threading
    
    from collections import defaultdict
    
    from datetime import datetime
    
    
    
    # Set up logger
    
    logger = logging.getLogger(__name__)
    
    log_level_value = getattr(logging, log_level.upper(), logging.INFO)
    
    logger.setLevel(log_level_value)
    
    
    
    if full:
    
        # Function to read the entire log file and parse lines
    
        def read_file(file_path, parse_function):
    
            with open(file_path, "r") as f:
    
                for line in f:
    
                    parse_function(line)
    
    
    
        # Launch threads for access and error logs
    
        threading.Thread(target=read_file, args=(log_file, lambda x: print(f"Parsed: {x}"))).start()
    
        threading.Thread(target=read_file, args=(elog_file, lambda x: print(f"Error Parsed: {x}"))).start()
    
    else:
    
        # Function to monitor logs for a specific duration
    
        def monitor_logs(file_path, parse_function):
    
            start_time = time.time()
    
            current_position = os.path.getsize(file_path)
    
    
    
            while time.time() - start_time < duration:
    
                with open(file_path, "r") as f:
    
                    f.seek(current_position)
    
                    for line in f:
    
                        parse_function(line)
    
                    current_position = f.tell()
    
    
    
                time.sleep(1)
    
    
    
        # Start log monitoring for the specified duration
    
        threading.Thread(target=monitor_logs, args=(log_file, lambda x: print(f"Parsed: {x}"))).start()
    
        threading.Thread(target=monitor_logs, args=(elog_file, lambda x: print(f"Error Parsed: {x}"))).start()
    
    
    
    def display_results():
    
        # Assuming you have the data in the format:
    
        status_code_counts = defaultdict(int)
    
        status_code_counts.update({"200": 100, "404": 50})
    
        
    
        print("\nStatus Code Summary:")
    
        print("Status Code | Total Requests")
    
        print("---------------------------")
    
        for code, count in status_code_counts.items():
    
            print(f"{code}         | {count}")
    
        
    
        if mode == "after":
    
            print("\nDeviation Table:")
    
            print("Status Code | Before | After | Deviation (%)")
    
            print("-------------------------------------------")
    
            print("200         | 100    | 110   | 10%")
    
            print("404         | 50     | 55    | 10%")
    
    
    
    display_results()
    
    



if __name__ == '__main__':
    cli()