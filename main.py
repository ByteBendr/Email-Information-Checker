import re
import socket
import dns.resolver
import argparse
from validate_email_address import validate_email
from colorama import Fore, Style, init
import colorama

# Initialize colorama
colorama.init()

# Define color constants
BLUE = Fore.LIGHTCYAN_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
RED = Fore.LIGHTRED_EX + Style.BRIGHT
YELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
WHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
RESET = Style.RESET_ALL

def get_email_info(email):
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Validate the email format
    if not re.match(email_regex, email):
        return {"error": "Invalid email format"}
    
    # Split the email into user and domain parts
    user, domain = email.split('@')
    
    # Initialize the result dictionary
    result = {
        "email": email,
        "user": user,
        "domain": domain
    }
    
    try:
        # DNS resolution to get MX records
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_hosts = [str(r.exchange) for r in mx_records]
        result['mx_records'] = mx_hosts
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        result['mx_records'] = []
    
    try:
        # Get the IP address of the domain
        ip_address = socket.gethostbyname(domain)
        result['ip_address'] = ip_address
    except socket.gaierror:
        result['ip_address'] = None
    
    # Validate the email using the validate_email library
    is_valid = validate_email(email, check_mx=True, verify=True)
    result['valid'] = is_valid
    
    # Perform a detailed validation
    email_validation = validate_email(email, check_mx=True)
    result['mx_validation'] = email_validation
    smtp_check = validate_email(email, verify=True)
    result['smtp_check'] = smtp_check
    
    return result

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Get advanced information about an email address.')
    parser.add_argument('email', type=str, help='The email address to check')
    
    # Parse arguments
    args = parser.parse_args()
    email = args.email
    
    # Get email information
    info = get_email_info(email)
    
    # Print the results
    print(f'\n{WHITE}========================================================={RESET}\n')
    for key, value in info.items():
        print(f"{WHITE}[{GREEN}⁓{WHITE}] {BLUE}{key}{WHITE}: {YELLOW}{value}{RESET}\n")
    print(f'{WHITE}========================================================={RESET}')
