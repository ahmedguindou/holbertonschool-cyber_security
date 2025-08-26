🛡️ Active Reconnaissance Guide
Table of Contents
Learning Objectives

Tools Explained

Reconnaissance Chain

Usage Examples

Learning Objectives
1. What is Active Reconnaissance?
Definition: Direct interaction with target systems to gather information.

Examples:

Pinging a host

Port scanning with nmap

SQL injection testing with sqlmap

Considerations: Leaves traces in logs and can be detected by security systems.

2. Importance in Cybersecurity
Blue Team: Identify vulnerabilities before attackers

Red Team: Map targets and discover entry points

Penetration Testers: Essential security audit step

👉 Reveals the attack surface of an organization

3. Wappalyzer for Reconnaissance
Identifies web technologies to tailor attacks:

WordPress → WordPress-specific exploits

React + Node.js → Different attack surface

Example Output: Nginx + WordPress + PHP

4. DNS Enumeration
Gathering DNS records to discover infrastructure:

Record Types:

A → IP address

MX → Mail servers

NS → Name servers

TXT → Metadata/SPF/DKIM

CNAME → Aliases

Tools: dig, nslookup, dnsenum

5. SMTP Enumeration
Testing mail servers (port 25) for vulnerabilities and user enumeration.

Tools & Methods:

bash
telnet mail.example.com 25
nc mail.example.com 25
nmap --script smtp-enum-users -p 25 mail.example.com
6. OS Fingerprinting
Identifying target operating systems:

Methods:

Active: nmap -O target.com

Passive: Traffic analysis with tools like p0f

7. SQL Injection with SQLmap
Automated SQL injection detection and exploitation:

Basic Commands:

bash
# Test URL
sqlmap -u "http://example.com/page.php?id=1"

# List databases
sqlmap -u "http://example.com/page.php?id=1" --dbs

# Dump data
sqlmap -u "http://example.com/page.php?id=1" -D testdb -T users --dump
Tools Explained
🖥️ ping
bash
ping example.com
Checks host availability using ICMP

🖥️ traceroute/tracert
bash
traceroute example.com   # Linux
tracert example.com      # Windows
Maps network path and hops

🖥️ telnet
bash
telnet mail.example.com 25
Manual service connection and testing

🖥️ netcat (nc)
bash
# Connect to port
nc example.com 80

# Port scanning
nc -zv example.com 20-100
Versatile networking utility

🖥️ Wappalyzer
bash
wappalyzer https://example.com
Web technology detection

🖥️ nmap
bash
# Basic scan
nmap example.com

# Service detection
nmap -sV example.com

# OS detection
nmap -O example.com
Comprehensive network scanning

🖥️ sqlmap
bash
sqlmap -u "http://example.com/page.php?id=1" --dbs
Automated SQL injection testing

Reconnaissance Chain
Host Discovery → ping target.com

Path Mapping → traceroute target.com

DNS Recon → dig target.com

Port Scanning → nmap target.com

Service Testing → telnet/nc

Tech Analysis → Wappalyzer

Vulnerability Testing → sqlmap

Usage Examples
Basic Network Reconnaissance
bash
# Check if target is online
ping target.com

# Discover network path
traceroute target.com

# Comprehensive port scan
nmap -sV -O target.com
Web Application Testing
bash
# Identify technologies
wappalyzer https://target.com

# Test for SQL injection
sqlmap -u "https://target.com/page?id=1" --risk=3 --level=5
DNS Investigation
bash
# Get all DNS records
dig target.com ANY

# Check mail servers
dig target.com MX

# Find subdomains
dnsenum target.com
