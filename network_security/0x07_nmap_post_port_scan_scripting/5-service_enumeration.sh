#!/bin/bash
nmap -A -p- --script banner,ssl-enum-ciphers,default,smb-os-discovery -oN service_enumeration_results.txt "$1"
