# Automated SOC Lab

## Overview
This lab is Cloud-based cybersecurity monitoring and incident response platform designed to simulate real-world SOC workflows.
This project integrates SIEM, SOAR, DFIR-IRSI, threat intelligence, and automated alerting technologies to detect, analyze, and respond to security events across multiple endpoints and operating systems.
The lab was built using AWS cloud infrastructure and combines Wazuh SIEM, Shuffle SOAR, DFIR-IRIS, Grafana, VirusTotal, AbuseIPDB, and Microsoft Teams integrations to create an end-to-end security monitoring environment.
The platform supports:
1. Centralized log collection and monitoring
2. Automated incident response workflows
3. Threat intelligence enrichment
4. MITRE ATT&CK aligned detections
5. Security event visualization and dashboards
6. Simulated attack detection and investigation

The objective of this project is to develop practical SOC engineering, detection engineering, and incident response skills through hands-on cybersecurity operations and automation.

## Objectives
The primary objectives of this project were:

1. Build a practical cloud-based SOC environment for security monitoring and incident response
2. Centralize logs and security events from multiple operating systems and devices
3. Implement automated alert triage and incident response workflows using SOAR technologies
4. Simulate real-world cyberattacks to test detection and response capabilities
5. Integrate threat intelligence platforms for IOC enrichment and analysis
6. Visualize security data and operational metrics using custom dashboards
7. Develop custom detection rules aligned with the MITRE ATT&CK framework
8. Improve hands-on skills in SIEM engineering, DFIR processes, and SOC operations
9. Gain practical experience with cloud infrastructure, security automation, and threat monitoring

## Technologies Used

| Category                         | Technologies                       |
| -------------------------------- | ---------------------------------- |
| SIEM                             | Wazuh                              |
| SOAR                             | Shuffle                            |
| DFIR & Case Management           | DFIR-IRIS                          |
| Visualization & Dashboards       | Grafana                            |
| Threat Intelligence              | VirusTotal, AbuseIPDB              |
| Cloud Infrastructure             | AWS EC2                            |
| Operating Systems                | Ubuntu Linux, Windows 10/11, macOS |
| Log Sources                      | Syslog, Wazuh Agents               |
| Communication & Alerting         | Microsoft Teams Webhooks           |
| Security Frameworks              | MITRE ATT&CK                       |
| Attack Simulation Tools          | Hydra, Nmap                        |
| Virtualization & Lab Environment | Docker, Proxmox                    |
| Scripting & Automation           | Python, JSON APIs                  |


## Lab Architecture
## Lab Architecture

The Automated SOC Lab was designed using a centralized security monitoring architecture hosted on AWS cloud infrastructure.

The environment consists of two primary servers:

### SIEM Server

The SIEM server hosts:

* Wazuh Manager
* Wazuh Indexer
* Wazuh Dashboard

This server is responsible for:

* Log collection
* Event correlation
* Threat detection
* Security monitoring
* Alert generation

### SOC Tools Server

The SOC tools server hosts:

* Shuffle SOAR
* DFIR-IRIS
* Grafana

This server is responsible for:

* Security orchestration and automation
* Incident response case management
* Threat intelligence enrichment
* Dashboard visualization and reporting

### Endpoint Monitoring

The platform monitors multiple endpoint types including:

* Windows systems
* Linux systems
* macOS systems
* Network devices
* Syslog-enabled services

### Threat Detection Workflow

1. Security events are generated from monitored endpoints
2. Wazuh collects and analyzes logs
3. Detection rules trigger alerts based on suspicious activity
4. Shuffle SOAR automates incident response workflows
5. Threat intelligence APIs enrich indicators of compromise (IOCs)
6. DFIR-IRIS creates and manages investigation cases
7. Microsoft Teams receives real-time security notifications
8. Grafana visualizes security metrics and alerts

## Features

## Detection & Response Workflows

## Attack Simulations

## Threat Intelligence Integrations

## SIEM Dashboards

## SOAR Automation

## DFIR & Incident Management

## MITRE ATT&CK Mapping

## Project Outcomes

## Screenshots

## Future Improvements

## Disclaimer

## Author
