# Configuration Files

This directory contains configuration files, workflow exports, dashboards, scripts, and integration components used within the Automated SOC Lab environment.

The configurations support SIEM monitoring, SOAR automation, threat intelligence enrichment, dashboard visualization, and endpoint monitoring workflows.

---

# Directory Structure

## Grafana

Contains exported Grafana dashboards used for SOC monitoring and security visualization.

Includes:

* Threat monitoring dashboards
* Alert visualization panels
* OpenSearch-integrated dashboards
* SOC operational views

---

## Shuffle

Contains Shuffle SOAR workflow exports, automation logic, enrichment scripts, and integration files.

Includes:

* Threat enrichment workflows
* DFIR-IRIS integration logic
* Microsoft Teams notification workflows
* IOC processing scripts
* Alert deduplication logic

Sensitive values and API credentials have been sanitized before publication.

---

## Wazuh

Contains Wazuh agent and monitoring configuration files used within the SOC environment.

Includes:

* Windows monitoring configurations
* Linux agent configurations
* macOS monitoring configurations
* OpenSearch index templates

---

## AWS

Contains infrastructure-related documentation and cloud security configuration references used during deployment.

Includes:

* Security group configurations
* Cloud deployment references
* Infrastructure security settings

---

# Purpose

These configuration files demonstrate practical implementation and integration of:

* SIEM engineering
* Security orchestration and automation
* Threat intelligence enrichment
* Endpoint monitoring
* Dashboard visualization
* Incident response workflows

All configurations were developed and tested within isolated lab environments for educational and research purposes only.
