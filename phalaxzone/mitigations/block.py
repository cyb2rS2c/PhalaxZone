from datetime import datetime
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = BASE_DIR / "logs"
BLOCKED_FILE = LOG_DIR / "blocked.txt"
REASON_FILE = LOG_DIR / "reason.txt"
BLOCK_DURATION = None


def _iptables_rule_exists(ip: str) -> bool:
    """Check if iptables rule already exists for this IP."""
    return subprocess.call(
        ["iptables", "-C", "INPUT", "-s", ip, "-j", "DROP"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ) == 0


def block_host(ip: str, reason: str):
    """Block an IP permanently (or until manually removed)."""
    if is_blocked(ip):
        return

    if not _iptables_rule_exists(ip):
        subprocess.run(
            ["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    with open(BLOCKED_FILE, "a") as bf:
        bf.write(f"{ip}\n")

    with open(REASON_FILE, "a") as rf:
        rf.write(f"{datetime.utcnow().isoformat()} | {ip} | {reason}\n")

    print(f"[MITIGATION] Permanently blocked {ip}")


def is_blocked(ip: str) -> bool:
    """Check if an IP is already blocked."""
    if not BLOCKED_FILE.exists():
        return False

    blocked_ips = [line.strip() for line in BLOCKED_FILE.read_text().splitlines()]
    return ip in blocked_ips


def restore_blocks():
    """Restore blocks after restart."""
    if not BLOCKED_FILE.exists():
        return

    blocked_ips = [line.strip() for line in BLOCKED_FILE.read_text().splitlines()]

    for ip in blocked_ips:
        if not _iptables_rule_exists(ip):
            subprocess.run(
                ["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    if blocked_ips:
        print(f"[MITIGATION] Restored {len(blocked_ips)} active blocks since the last scan")


def unblock_host(ip: str):
    """Manually unblock an IP."""
    if _iptables_rule_exists(ip):
        subprocess.run(
            ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"[MITIGATION] Unblocked {ip}")

    if BLOCKED_FILE.exists():
        lines = [line.strip() for line in BLOCKED_FILE.read_text().splitlines()]
        lines = [line for line in lines if line != ip]
        BLOCKED_FILE.write_text("\n".join(lines) + ("\n" if lines else ""))


def start_unblocker():
    """
    Restore blocks on startup.
    No automatic unblocking thread needed for permanent blocks.
    """
    restore_blocks()
