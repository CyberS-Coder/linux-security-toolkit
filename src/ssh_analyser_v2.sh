#!/bin/bash

# Ensure script is run with root/sudo privileges
if [ "$EUID" -ne 0 ]; then
    echo "[-] Please run this script with sudo."
    exit 1
fi

echo "Analyzing SSH failed login attempts..."
echo "----------------------------------------"

# Accept a threshold from the user, default to 1 if not provided
THRESHOLD=${1:-1}

journalctl -u ssh --no-pager |grep "Failed password"|awk '{print $(NF-3)}'|sort|uniq -c|sort -nr|awk -v t="$THRESHOLD" '$1 >= t {print "IP:", $2, "| Failed attempts:", $1}'

echo "----------------------------------------"
echo "Analysis complete."
