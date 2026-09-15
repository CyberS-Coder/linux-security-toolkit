#!/bin/bash

# Ensure script is run with root/sudo privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo."
    exit 1
fi

echo "Analyzing SSH failed login attempts..."
echo "----------------------------------------"

# Run the log parsing pipeline
journalctl -u ssh|grep "Failed password"|awk '{print $(NF-3)}'|sort|uniq -c|sort -nr

echo "----------------------------------------"
echo "Analysis complete."
