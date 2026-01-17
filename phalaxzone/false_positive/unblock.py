from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
BLOCKED_FILE = BASE_DIR / "logs" / "blocked.txt"
WHITELIST_FILE = BASE_DIR / "logs" / "allowed.txt"


def unblock_host(host: str):
    if BLOCKED_FILE.exists():
        lines = BLOCKED_FILE.read_text().splitlines()
        lines = [line for line in lines if line != host]
        BLOCKED_FILE.write_text("\n".join(lines) + "\n")

    whitelisted = WHITELIST_FILE.read_text().splitlines()
    if host not in whitelisted:
        whitelisted.append(host)
        WHITELIST_FILE.write_text("\n".join(whitelisted) + "\n")
