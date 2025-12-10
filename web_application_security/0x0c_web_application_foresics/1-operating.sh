#!/bin/bash
# 1-operating.sh
# Extract operating system version from dmesg

# Check if file is provided
if [ $# -eq 0 ]
then
    echo "Usage: $0 <dmesg_file>"
    exit 1
fi

DMESG_FILE=$1

# Check if file exists
if [ ! -f "$DMESG_FILE" ]
then
    echo "Error: File '$DMESG_FILE' not found"
    exit 1
fi

# Extract Linux version line
grep "Linux version" "$DMESG_FILE" | head -1
