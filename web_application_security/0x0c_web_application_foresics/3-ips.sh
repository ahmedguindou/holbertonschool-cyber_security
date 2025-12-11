#!/bin/bash
# 3-ips.sh
# Count distinct IP addresses that successfully accessed the system

# Extract IPs from successful SSH logins, remove duplicates, and count
grep "Accepted password for root" auth.log | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort -u | wc -l
