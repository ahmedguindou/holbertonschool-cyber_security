#!/bin/bash

# Check if log file exists
if [ ! -f "logs.txt" ]
then
    echo "Error: logs.txt file not found!"
    exit 1
fi

# Use awk to filter lines starting with IP pattern and count occurrences
# Prints IP with highest count
awk '/^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ {count[$1]++} END {max=0; ip=""; for (i in count) if (count[i] > max) {max=count[i]; ip=i} print ip}' logs.txt
