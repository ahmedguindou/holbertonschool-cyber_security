#!/bin/bash
# 4-firewall.sh
# Count firewall rules added

# Look for firewall rule additions in auth.log
grep -c "firewall\|iptables\|ufw.*rule" auth.log
