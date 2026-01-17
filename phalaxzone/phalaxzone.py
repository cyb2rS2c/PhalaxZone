import os
import time
from pathlib import Path
from detectors.ddos import run_detector
from mitigations.block import start_unblocker
from false_positive.unblock import unblock_host
from colorama import init, Fore, Style
from termcolor import colored
from animation.animation import call_fig, animated_banner
init(autoreset=True)

LOGS_DIR = Path("logs")
BLOCKED_FILE = LOGS_DIR / "blocked.txt"


def init_logs():
    LOGS_DIR.mkdir(exist_ok=True)
    for file in ["blocked.txt", "reason.txt", "allowed.txt"]:
        path = LOGS_DIR / file
        if not path.exists():
            path.touch()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_blocked_hosts():
    if not BLOCKED_FILE.exists():
        print(Fore.YELLOW + "[!] No blocked hosts file found")
        return

    hosts = BLOCKED_FILE.read_text().splitlines()
    if not hosts:
        print(Fore.GREEN + "[*] No hosts are currently blocked")
        return

    print(Fore.RED + "\n[Blocked Hosts]")
    for host in hosts:
        print(Fore.RED + f" - {host}")
    print(Style.RESET_ALL)


def menu():
    print(colored("""
==============================
        Main Menu
==============================
1) Start DDoS detector
2) Unblock host (false positive)
3) Show blocked hosts
4) Exit
==============================
""", "grey", attrs=['bold']))

def main():
    clear()
    text = call_fig()
    animated_banner(text)
    time.sleep(0.02)
    print(Fore.GREEN + "[*] Initializing DDoS protection system...\n")
    init_logs()
    start_unblocker()
    time.sleep(0.5)

    while True:
        menu()
        choice = input(Fore.YELLOW + "Select an option: " + Style.RESET_ALL).strip()

        if choice == "1":
            print(Fore.GREEN + "[*] Starting DDoS detector (Ctrl+C to stop)")
            try:
                iface = input("Enter your active interface or use default (default wlan0): ").strip() or "wlan0"
                run_detector(interface=iface)
                
            except KeyboardInterrupt:
                print(Fore.MAGENTA + "\n[*] Detector stopped")

        elif choice == "2":
            host = input(Fore.YELLOW + "Enter host/IP to unblock: " + Style.RESET_ALL).strip()
            if host:
                unblock_host(host)
                print(Fore.GREEN + f"[*] Host unblocked: {host}")

        elif choice == "3":
            show_blocked_hosts()
            input(Fore.CYAN + "\nPress Enter to return to menu..." + Style.RESET_ALL)

        elif choice == "4":
            print(Fore.MAGENTA + "[!] Exiting...")
            break

        else:
            print(Fore.RED + "[!] Invalid option\n")
            time.sleep(0.5)
        clear()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print(Fore.MAGENTA + "\n[!] Exiting...")
