#!/bin/bash

# Default threshold to 3 if omitted
THRESHOLD=${1:-3}

# Check for root/sudo privileges first
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo."
    exit 1
fi

> blacklisted_ips.txt

echo "Analyzing SSH logs for threshold >= $THRESHOLD..."

# Execute pipeline and save clean IPs directly to file
journalctl -u ssh|grep "Failed password"|awk '{print $(NF-3)}'|sort|uniq -c|sort -nr|awk -v t="$THRESHOLD" '$1 >= t {print $2}' > blacklisted_ips.txt

# Count lines directly into a variable
IP_COUNT=$(wc -l < blacklisted_ips.txt)

echo "Found $IP_COUNT IP(s) meeting the threshold."
echo "--------------------------------------------------"
cat blacklisted_ips.txt
