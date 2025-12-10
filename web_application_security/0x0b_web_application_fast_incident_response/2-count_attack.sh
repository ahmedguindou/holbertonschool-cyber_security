#!/bin/bash

# Check if log file is provided
if [ $# -eq 0 ]
then
    echo "Error: Please provide a log file as argument"
    exit 1
fi

# Check if log file exists
if [ ! -f "$1" ]
then
    echo "Error: $1 file not found!"
    exit 1
fi

# Find the attacker IP (IP with most requests)
ATTACKER_IP=$(grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "$1" | awk '{print $1}' | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')

# Count requests from the attacker IP
grep -c "^$ATTACKER_IP " "$1"
