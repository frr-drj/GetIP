import socket
import pyfiglet
from termcolor import colored

def extract_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Could not resolve the domain."

def main():
    while True:
        # Create a big "GetIP" banner with the banner font
        banner = pyfiglet.figlet_format("GetIP", font="banner")

        # Print the "GetIP" banner in red
        print(colored(banner, "red"))

        website = input("Enter a website URL: ")
        ip = extract_ip_address(website)

        # Print the IP address in green
        print(colored(f"IP Address for {website}: {ip}", "green"))

        # Ask the user if they want to restart or exit
        choice = input("Do you want to restart (R) or exit (E)? ").strip().lower()

        if choice != 'r':
            break

if __name__ == "__main__":
    main()
