# AWS Security Group Rules

## Overview

The SOC platform uses two security groups within the same VPC (`vpc-048936330ec076271`), each scoped to a specific server role.

| Security Group | ID | Server Role |
|---|---|---|
| SIEM-Server-SecGrp | sg-072c99179b47e0a81 | Wazuh SIEM server (Manager, Indexer, Dashboard) |
| SIEM-SOC-VPC-SecGrp | sg-094f61f9ac73752a4 | SOC tools server (Shuffle SOAR, Grafana, DFIR IRIS) |

Both security groups belong to the same VPC and are deployed in the `ap-southeast-2` (Sydney) region.

---

## SIEM-Server-SecGrp

**Security Group ID:** sg-072c99179b47e0a81  
**Description:** Access to SIEM services  
**VPC:** vpc-048936330ec076271

### Inbound Rules (8)

| Rule ID | Protocol | Port | Source | Purpose |
|---|---|---|---|---|
| sgr-0f348a2a921221ff6 | TCP | 55000 | 10.0.0.0/16 | Wazuh API — internal VPC only |
| sgr-0ae35c61c12b2bb78 | TCP | 1514 | 0.0.0.0/0 | Wazuh agent communication |
| sgr-04048233ea8655579 | TCP | 443 | 0.0.0.0/0 | Wazuh Dashboard (HTTPS) |
| sgr-0ba7802c9ccdf8250 | TCP | 9200 | 0.0.0.0/0 | OpenSearch REST API |
| sgr-0758e2ac1dd64339c | TCP | 3000 | 0.0.0.0/0 | Grafana |
| sgr-0b83a92ea68233890 | TCP | 1515 | 0.0.0.0/0 | Wazuh agent registration |
| sgr-0400832d8d5e90bce | TCP | 22 | 0.0.0.0/0 | SSH access |
| sgr-0db186b105d99c2e6 | UDP | 514 | 0.0.0.0/0 | Syslog ingestion |

### Outbound Rules

| Protocol | Port | Destination | Purpose |
|---|---|---|---|
| All traffic | All | 0.0.0.0/0 | Unrestricted outbound |

---

## SIEM-SOC-VPC-SecGrp

**Security Group ID:** sg-094f61f9ac73752a4  
**Description:** SOC tools communication  
**VPC:** vpc-048936330ec076271

### Inbound Rules (4)

| Rule ID | Protocol | Port | Source | Purpose |
|---|---|---|---|---|
| sgr-0880df6d87b6e7ea2 | TCP | 3001 | 0.0.0.0/0 | Shuffle SOAR web UI |
| sgr-0492d95f65596bc16 | TCP | 3000 | 0.0.0.0/0 | Grafana |
| sgr-007b828a582d71888 | TCP | 22 | 0.0.0.0/0 | SSH access |
| sgr-0a14c2f6f5d919d95 | TCP | 443 | 0.0.0.0/0 | DFIR IRIS (HTTPS) |

### Outbound Rules

| Protocol | Port | Destination | Purpose |
|---|---|---|---|
| All traffic | All | 0.0.0.0/0 | Unrestricted outbound |

---

## Design Notes

### Port 55000 — Wazuh API scope

The Wazuh API port (55000) is the only rule restricted to the internal VPC CIDR (`10.0.0.0/16`) rather than open to the internet. This limits API access to resources within the VPC, reducing the attack surface for direct API calls to the Wazuh manager.

### Port 9200 — OpenSearch exposure

OpenSearch (9200) is currently open to `0.0.0.0/0` to support dashboard connectivity and the GeoIP enrichment pipeline. In a production hardened deployment, this would be restricted to the VPC CIDR or a specific management IP range.

### Port 514 — Syslog ingestion

UDP 514 is open to allow external syslog sources (such as the TP-Link router and Raspberry Pi) to forward logs to the Wazuh manager via rsyslog. The `wazuh-remoted` service listens on this port after resolving the rsyslog conflict documented in the troubleshooting notes.

### SSH (Port 22)

SSH is currently open to `0.0.0.0/0` for lab access flexibility. A hardened deployment would restrict this to a specific management IP or use AWS Systems Manager Session Manager to eliminate direct SSH exposure entirely.

---

## Port Reference Summary

| Port | Protocol | Service | Server |
|---|---|---|---|
| 22 | TCP | SSH | Both |
| 443 | TCP | Wazuh Dashboard / DFIR IRIS | Both |
| 514 | UDP | Syslog | SIEM server |
| 1514 | TCP | Wazuh agent comms | SIEM server |
| 1515 | TCP | Wazuh agent registration | SIEM server |
| 3000 | TCP | Grafana | Both |
| 3001 | TCP | Shuffle SOAR | SOC tools server |
| 9200 | TCP | OpenSearch | SIEM server |
| 55000 | TCP | Wazuh API (internal) | SIEM server |