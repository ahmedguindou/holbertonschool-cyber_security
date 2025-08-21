# Holberton School Domain Reconnaissance Report

## Executive Summary
This report documents passive reconnaissance activities performed on the holbertonschool.com domain for educational cybersecurity purposes. The analysis reveals a mature, well-architected web infrastructure utilizing AWS services, multiple content delivery networks, and various third-party integrations.

**Target Domain:** holbertonschool.com  
**Date of Analysis:** August 21, 2025  
**Analyst:** Security Assessment  
**Methodology:** Passive reconnaissance using OSINT techniques

## 1. Domain Registration Information

### WHOIS Analysis
```bash
# Command used:
whois holbertonschool.com
```

**Key Findings:**
- **Registrar:** Gandi SAS
- **Creation Date:** July 30, 2015 (10 years old)
- **Expiration Date:** July 30, 2026
- **Name Servers:** AWS Route 53 (ns-1244.awsdns-27.org, ns-957.awsdns-55.net, ns-343.awsdns-42.com, ns-1991.awsdns-56.co.uk)
- **Organization:** Domain privacy protected
- **Status:** clientTransferProhibited

## 2. DNS Infrastructure Analysis

### Primary DNS Records

#### A Records (IPv4 Addresses)
| Hostname | IP Address | Notes |
|----------|------------|-------|
| holbertonschool.com | 99.83.190.102 | Primary domain |
| holbertonschool.com | 75.2.70.75 | Load balancing |

#### Name Servers
| NS Record | Provider |
|-----------|----------|
| ns-1244.awsdns-27.org | AWS Route 53 |
| ns-957.awsdns-55.net | AWS Route 53 |
| ns-343.awsdns-42.com | AWS Route 53 |
| ns-1991.awsdns-56.co.uk | AWS Route 53 |

#### Mail Exchange Records
| Priority | Mail Server | Provider |
|----------|-------------|----------|
| 1 | aspmx.l.google.com | Google Workspace |
| 5 | alt1.aspmx.l.google.com | Google Workspace |
| 5 | alt2.aspmx.l.google.com | Google Workspace |
| 10 | alt3.aspmx.l.google.com | Google Workspace |
| 10 | alt4.aspmx.l.google.com | Google Workspace |

#### Third-Party Service Integrations (TXT Records)
- **Stripe:** Payment processing verification
- **Google:** Site verification and SPF records
- **Brevo:** Marketing automation platform
- **Zapier:** Workflow automation
- **Intacct:** Accounting software integration
- **Loader.io:** Load testing service
- **Microsoft:** Domain verification

## 3. Subdomain Enumeration

### Methodology
```bash
# Primary tool used:
subfinder -d holbertonschool.com -all -o subdomains.txt
```

### Discovered Subdomains (28 Total)
| Subdomain | IP Address | Status | Purpose |
|-----------|------------|--------|---------|
| **Active Production Services** |
| www.holbertonschool.com | 35.152.117.67, 15.160.106.203, 15.161.34.42 | HTTP 200 | Main website (Webflow) |
| apply.holbertonschool.com | 13.36.159.193, 13.36.62.51, 15.188.218.54 | HTTP 302 | Application portal |
| blog.holbertonschool.com | 192.0.78.230, 192.0.78.131 | HTTP 200 | WordPress blog |
| help.holbertonschool.com | 75.2.70.75, 99.83.190.102 | Active | Help documentation |
| support.holbertonschool.com | 216.198.54.6, 216.198.53.6 | Active | Zendesk support |
| **Development/Staging Environments** |
| staging-apply.holbertonschool.com | 13.37.67.17, 35.181.42.84 | HTTP 401 | Protected staging |
| read.holbertonschool.com | 35.180.6.147, 13.39.186.230 | HTTP 401 | Protected read access |
| alpha.holbertonschool.com | 54.157.56.129 | Inactive | Alpha testing |
| beta.holbertonschool.com | - | Inactive | Beta testing |
| **Version Control** |
| v1.holbertonschool.com | 54.86.136.129 | Inactive | Legacy version 1 |
| v2.holbertonschool.com | 34.203.198.145 | Inactive | Legacy version 2 |
| v3.holbertonschool.com | 54.89.246.137 | Inactive | Legacy version 3 |
| **Asset Delivery** |
| assets.holbertonschool.com | 3.160.196.* (CloudFront) | HTTP 403 | CDN assets |
| rails-assets.holbertonschool.com | 216.137.52.* (CloudFront) | HTTP 301 | Rails assets |
| **Internationalization** |
| fr.holbertonschool.com | 35.152.117.67 (Webflow) | Active | French site |
| en.fr.holbertonschool.com | 104.17.201.193 (Weglot) | Active | Translation |
| fr.webflow.holbertonschool.com | 104.17.201.193 (Weglot) | Active | French Webflow |
| **Special Projects** |
| smile2021.holbertonschool.com | 35.152.117.67 (Webflow) | Inactive | 2021 campaign |
| hippokampoi.holbertonschool.com | - | Inactive | Special project |
| yriry2.holbertonschool.com | 52.47.143.83 | HTTP 403 | Unknown project |

## 4. IP Range Analysis

### Identified IP Ranges by Provider

| IP Range/Provider | Purpose | Subdomain Count | Notes |
|-------------------|---------|-----------------|-------|
| **AWS EU-West-3 (Paris)** |
| 13.36.0.0/14 | Application servers | 8 | Main app infrastructure |
| 15.188.0.0/16 | Production apps | 1 | Apply portal |
| 35.180.0.0/16 | Production services | 2 | Read/staging services |
| **AWS US-East-1 (Virginia)** |
| 54.80.0.0/12 | Legacy systems | 3 | Older infrastructure |
| 34.192.0.0/12 | Production services | 1 | Version control |
| 52.0.0.0/11 | Special projects | 1 | Project servers |
| **AWS CloudFront CDN** |
| 3.160.0.0/12 | Asset delivery | 8 | Static content CDN |
| **Webflow Infrastructure** |
| 35.152.0.0/16 | Marketing sites | 4 | Webflow hosting |
| 15.160.0.0/16 | Marketing sites | 4 | Webflow hosting |
| **Main Domain Load Balancers** |
| 99.83.64.0/18 | Primary load balancer | 1 | Main domain (99.83.190.102) |
| 75.2.0.0/17 | Secondary load balancer | 1 | Main domain (75.2.70.75) |
| **Third-Party Services** |
| 192.0.78.0/24 | WordPress.com | 1 | Blog hosting |
| 216.198.0.0/16 | Zendesk | 1 | Support platform |
| 104.17.200.0/24 | Cloudflare/Weglot | 2 | Translation service |

### Precise CIDR Ranges Discovered
Based on WHOIS analysis of key IP addresses:

| IP Address | CIDR Ranges | Provider | ASN |
|------------|-------------|----------|-----|
| 99.83.190.102 | 99.83.64.0/18, 99.83.128.0/17, 99.84.0.0/16 | Amazon CloudFront | AS16509 |
| 75.2.70.75 | 75.2.0.0/17, 75.2.128.0/18 | Amazon CloudFront | AS16509 |
| 13.36.159.193 | 13.36.0.0/14 | Amazon EU-West-3 | AS16509 |

### Total IP Range Coverage
- **Primary AWS Infrastructure:** 13.36.0.0/14 (1,048,576 IPs)
- **CloudFront Global:** 99.83.64.0/18 + 75.2.0.0/17 (~180,000 IPs)  
- **Legacy/Development:** 54.0.0.0/12 + 34.192.0.0/12 (~2M IPs)

## 5. Technology Stack Analysis

### Web Technologies by Subdomain

#### Main Website (www.holbertonschool.com)
- **Hosting Platform:** Webflow (via proxy-ssl.webflow.com)
- **CDN:** Cloudflare
- **Security:** 
  - HTTPS with HSTS (max-age=31536000)
  - X-Frame-Options: SAMEORIGIN
  - Content Security Policy: frame-ancestors 'self'
- **Caching:** Surrogate caching (max-age=432000)
- **Performance:** HTTP/2, H3 support

#### Application Portal (apply.holbertonschool.com)
- **Infrastructure:** AWS Elastic Beanstalk (eu-west-3)
- **Web Server:** Nginx 1.20.0
- **Framework:** Ruby on Rails (based on subdomain naming)
- **Security Headers:**
  - X-Frame-Options: SAMEORIGIN
  - X-XSS-Protection: 1; mode=block
  - X-Content-Type-Options: nosniff
  - Referrer-Policy: strict-origin-when-cross-origin
- **Geographic Routing:** Automatic country/locale detection (redirects to tn/fr)

#### Blog (blog.holbertonschool.com)
- **Platform:** WordPress.com hosted
- **Web Server:** Nginx
- **CDN:** Automattic (WordPress.com infrastructure)
- **Caching:** Batcache system
- **Security:** HSTS enabled

#### Staging Environment (staging-apply.holbertonschool.com)
- **Infrastructure:** AWS Elastic Beanstalk (eu-west-3)
- **Web Server:** Nginx 1.20.0
- **Authentication:** HTTP Basic Authentication
- **Same security headers as production**

### Content Delivery Networks
1. **AWS CloudFront:** For application assets
2. **Cloudflare:** For main website and performance
3. **Webflow CDN:** For marketing pages
4. **WordPress.com CDN:** For blog content

## 6. Security Analysis

### Security Headers Implementation
| Subdomain | HTTPS | HSTS | CSP | X-Frame-Options | XSS Protection |
|-----------|-------|------|-----|-----------------|----------------|
| www.holbertonschool.com | ✅ | ✅ | ✅ | ✅ | ❌ |
| apply.holbertonschool.com | ✅ | ❌ | ⚠️ (empty) | ✅ | ✅ |
| blog.holbertonschool.com | ✅ | ✅ | ❌ | ❌ | ❌ |
| staging-apply.holbertonschool.com | ✅ | ❌ | ⚠️ (empty) | ✅ | ✅ |

### Authentication & Access Control
- **Staging environments:** Protected with HTTP Basic Authentication
- **Asset delivery:** CloudFront distributions return 403 for direct access
- **Geographic routing:** Automatic country detection and localization

### Notable Security Findings
- **Positive:** Most services implement HTTPS and basic security headers
- **Concern:** Some services have empty CSP headers
- **Concern:** Blog platform lacks comprehensive security headers
- **Good Practice:** Staging environments properly protected

## 7. Infrastructure Summary

### Architecture Overview
```
holbertonschool.com Infrastructure
├── Production (AWS EU-West-3)
│   ├── Main Application (Elastic Beanstalk)
│   ├── Apply Portal (Elastic Beanstalk) 
│   └── Read Services (Elastic Beanstalk)
├── Content Delivery
│   ├── CloudFront (Assets)
│   ├── Cloudflare (Main site)
│   └── Webflow CDN (Marketing)
├── External Services
│   ├── WordPress.com (Blog)
│   ├── Zendesk (Support)
│   ├── Google Workspace (Email)
│   └── Weglot (Translation)
└── Development/Legacy (AWS US-East-1)
    ├── Alpha/Beta environments
    ├── Version archives (v1, v2, v3)
    └── Special projects
```

### Key Observations
- **Total Subdomains:** 28 discovered
- **Active Services:** 10 responding
- **Primary Infrastructure:** AWS (EU-West-3 for production, US-East-1 for legacy)
- **CDN Strategy:** Multi-provider approach for performance and redundancy
- **Development Practices:** Clear separation of staging/production environments

## 8. Business Intelligence

### Third-Party Service Integrations
Based on DNS TXT records and subdomain analysis:

1. **Payment Processing:** Stripe integration
2. **Marketing Automation:** Brevo (formerly Sendinblue)
3. **Workflow Automation:** Zapier
4. **Accounting:** Intacct/Sage integration
5. **Customer Support:** Zendesk
6. **Email Services:** Google Workspace
7. **Translation:** Weglot for internationalization
8. **Content Management:** Webflow for marketing, WordPress for blog
9. **Load Testing:** Loader.io for performance testing

### Geographic Presence
- **Primary Infrastructure:** Europe (Paris region)
- **Legacy Systems:** United States (Virginia)
- **Internationalization:** French language support
- **User Routing:** Geographic detection for localization

## 9. Recommendations

### Security Improvements
1. **Implement comprehensive CSP headers** on application portals
2. **Add missing security headers** to blog platform
3. **Consider HSTS preloading** for enhanced security
4. **Review direct asset access policies** on CDN distributions

### Infrastructure Observations
1. **Well-architected multi-region setup** with proper separation of concerns
2. **Good use of staging environments** with appropriate access controls
3. **Effective CDN strategy** for performance optimization
4. **Mature development practices** with version control and environment separation

## 10. Methodology and Tools Used

### Passive Reconnaissance Tools
1. **WHOIS** - Domain registration information
2. **DIG** - DNS record enumeration  
3. **SUBFINDER** - Subdomain discovery using multiple sources
4. **CURL** - HTTP header analysis and service detection

### Commands Executed
```bash
# Domain intelligence
whois holbertonschool.com
dig holbertonschool.com ANY
dig holbertonschool.com NS
dig holbertonschool.com MX

# Subdomain discovery
subfinder -d holbertonschool.com -all -o subdomains.txt

# IP address enumeration
while read subdomain; do
    dig $subdomain A +short
done < subdomains.txt

# Service detection
while read subdomain; do
    curl -I -s --connect-timeout 5 https://$subdomain
done < subdomains.txt

# Technology stack analysis
curl -I -s https://www.holbertonschool.com
curl -I -s https://apply.holbertonschool.com
curl -I -s https://blog.holbertonschool.com
```

## 11. Appendices

### Appendix A: Complete Subdomain List
```
rails-assets-apply-staging.holbertonschool.com
www.holbertonschool.com
apply.holbertonschool.com
beta.holbertonschool.com
staging-apply.holbertonschool.com
apply-staging.holbertonschool.com
lvl2-discourse-staging.holbertonschool.com
smile2021.holbertonschool.com
support.holbertonschool.com
read.holbertonschool.com
v3.holbertonschool.com
rails-assets.holbertonschool.com
alpha.holbertonschool.com
help.holbertonschool.com
fr.webflow.holbertonschool.com
blog-new.holbertonschool.com
staging-rails-assets-apply.holbertonschool.com
blog.holbertonschool.com
staging-apply-forum.holbertonschool.com
webflow.holbertonschool.com
fr.holbertonschool.com
hippokampoi.holbertonschool.com
holbertonschool.com
v1.holbertonschool.com
yriry2.holbertonschool.com
assets.holbertonschool.com
en.fr.holbertonschool.com
v2.holbertonschool.com
```

### Appendix B: All Discovered IP Addresses
```
99.83.190.102, 75.2.70.75 (Main domain)
35.152.117.67, 15.160.106.203, 15.161.34.42 (Webflow)
13.36.159.193, 13.36.62.51, 15.188.218.54 (Apply portal)
13.37.67.17, 35.181.42.84 (Staging)
13.38.216.13, 13.38.122.220 (Forums)
13.39.186.230, 35.180.6.147 (Read services)
192.0.78.230, 192.0.78.131 (WordPress blog)
216.198.54.6, 216.198.53.6 (Zendesk)
216.137.52.* (CloudFront assets)
3.160.196.*, 3.164.182.* (CloudFront)
54.89.246.137, 54.157.56.129, 54.86.136.129 (Legacy)
34.203.198.145, 52.47.143.83 (Legacy/Special)
104.17.201.193 (Weglot/Cloudflare)
```

---
**Report Generated:** August 21, 2025  
**Methodology:** Passive OSINT Reconnaissance  
**Target:** holbertonschool.com  
**Tools:** whois, dig, subfinder, curl
