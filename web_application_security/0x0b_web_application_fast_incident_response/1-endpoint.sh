#!/bin/bash

# Check if log file exists
if [ ! -f "logs.txt" ]
then
    echo "Error: logs.txt file not found!"
    exit 1
fi

# Extract URLs from web access log lines
# Look for lines that have HTTP methods (GET, POST, etc.) and extract the URL
# Pattern matches: IP - - [timestamp] "METHOD /path HTTP/version"
awk '/^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ {print $7}' logs.txt | sort | uniq -c | sort -nr | head -1 | awk '{print $2}'
