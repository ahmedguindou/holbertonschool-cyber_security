#!/bin/bash
# 2-accounts.sh
# Find compromised account with failed attempts followed by success

if [ $# -eq 0 ]
then
    echo "Usage: $0 <auth.log>"
    exit 1
fi

LOG_FILE=$1

if [ ! -f "$LOG_FILE" ]
then
    echo "Error: File '$LOG_FILE' not found"
    exit 1
fi

# Analyze last 1000 lines for authentication patterns
tail -1000 "$LOG_FILE" | grep -E "Failed password|Accepted password|Invalid user" | awk '{print $9, $11}' | sort | uniq -c | sort -nr
