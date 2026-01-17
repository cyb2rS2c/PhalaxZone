# detectors/ddos.py
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time
from pathlib import Path
from mitigations.block import block_host

TIME_WINDOW = 5
PACKET_THRESHOLD = 20

packet_count = defaultdict(int)
start_time = time.time()
blocked_ips = set()

WHITELIST_FILE = Path("logs/allowed.txt")
BLOCKED_FILE = Path("logs/blocked.txt")


def load_file_set(path: Path) -> set:
    if not path.exists():
        return set()
    return set(path.read_text().splitlines())


def is_whitelisted(ip: str) -> bool:
    return ip in load_file_set(WHITELIST_FILE)


def is_blocked(ip: str) -> bool:
    return ip in load_file_set(BLOCKED_FILE) or ip in blocked_ips


def detect_ddos(packet):
    global start_time

    if not (packet.haslayer(IP) and packet.haslayer(TCP)):
        return

    if not (packet[TCP].flags & 0x02):
        return

    src_ip = packet[IP].src

    if is_whitelisted(src_ip):
        return

    if is_blocked(src_ip):
        return
    packet_count[src_ip] += 1

    current_time = time.time()

    if current_time - start_time >= TIME_WINDOW:
        print("\n--- DDoS Analysis ---")

        for ip, count in list(packet_count.items()):
            if is_whitelisted(ip) or is_blocked(ip):
                continue

            if count >= PACKET_THRESHOLD:
                print(f"[DDoS ALERT] {ip} sent {count} SYN packets")
                block_host(ip, "SYN flood detected")
                blocked_ips.add(ip)
            else:
                print(f"[OK] {ip}: {count} packets")

        packet_count.clear()
        start_time = current_time


def run_detector(interface):
    print(f"[*] Starting SYN flood detection on {interface}")
    sniff(iface=interface, filter="tcp", prn=detect_ddos, store=False)
