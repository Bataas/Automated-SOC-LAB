# Deployment Overview

This document provides an overview of the deployment architecture, infrastructure components, and technologies used to build the Automated SOC Lab environment.

The project was deployed as a cloud-based SOC platform designed to simulate real-world security monitoring, detection engineering, incident response, and security automation workflows.

---

# Deployment Objectives

The deployment was designed to:

* Build a centralized SOC monitoring environment
* Simulate enterprise security operations workflows
* Integrate SIEM, SOAR, and DFIR technologies
* Automate incident response processes
* Support threat intelligence enrichment
* Monitor multiple operating systems and endpoints
* Validate security detections through attack simulations

---

# Cloud Infrastructure

The environment was deployed within AWS cloud infrastructure using EC2 instances hosted in the Sydney region (`ap-southeast-2`).

## AWS Components

* AWS EC2 Instances
* Virtual Private Cloud (VPC)
* Security Groups
* Cloud-based networking infrastructure

The deployment architecture was separated into dedicated SOC infrastructure components to improve scalability and operational organization.

---

# Infrastructure Architecture

The environment consists of two primary servers:

## 1. SIEM Server

The SIEM server hosts:

* Wazuh Manager
* Wazuh Indexer
* Wazuh Dashboard

### Responsibilities

* Log collection
* Event correlation
* Threat detection
* Alert generation
* Security monitoring
* Agent management

---

## 2. SOC Tools Server

The SOC tools server hosts:

* Shuffle SOAR
* DFIR-IRIS
* Grafana

### Responsibilities

* Security orchestration and automation
* Incident response workflows
* Threat intelligence enrichment
* Dashboard visualization
* Investigation management
* SOC alerting workflows

---

# Endpoint Monitoring

The environment monitors multiple endpoint types including:

* Windows systems
* Linux systems
* macOS systems
* Network-related services
* Syslog-enabled devices

Wazuh agents and Syslog integrations were used for centralized log collection and security monitoring.

---

# Integrated Security Technologies

## SIEM

* Wazuh

## SOAR

* Shuffle

## DFIR Platform

* DFIR-IRIS

## Visualization

* Grafana

## Threat Intelligence

* VirusTotal
* AbuseIPDB

## Alerting

* Microsoft Teams Webhooks

---

# Deployment Workflow

The deployment process included:

1. AWS infrastructure provisioning
2. Linux server configuration
3. Wazuh deployment and configuration
4. Endpoint agent onboarding
5. Grafana dashboard integration
6. Shuffle SOAR deployment
7. DFIR-IRIS deployment
8. Threat intelligence integration
9. Teams webhook integration
10. Attack simulation validation

---

# Containerization & Services

Several SOC components were deployed using Docker-based services to improve:

* Scalability
* Service isolation
* Deployment consistency
* Infrastructure management

Dockerized services included:

* Shuffle SOAR
* DFIR-IRIS
* Grafana

---

# Security Monitoring Workflow

The deployed SOC environment supports:

* Real-time alert monitoring
* Threat intelligence enrichment
* Automated incident creation
* SOC analyst notifications
* MITRE ATT&CK aligned detections
* Security dashboard visualization
* Incident response automation

---

# Operational Outcomes

The deployment successfully demonstrated:

* Cloud-based SOC operations
* Practical SIEM engineering
* SOAR workflow automation
* Threat detection and monitoring
* Incident response orchestration
* Threat intelligence integration
* Detection engineering workflows

---

# Purpose

This deployment was implemented for educational, research, and cybersecurity training purposes to simulate practical SOC operations within a controlled and authorized lab environment.
