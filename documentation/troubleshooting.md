# Troubleshooting & Challenges

This document outlines key technical issues encountered during the deployment and operation of the Automated SOC Lab environment and the troubleshooting steps taken to resolve them.

The troubleshooting process provided practical experience in infrastructure management, SIEM deployment, Docker services, integrations, and SOC operations.

---

# OpenSearch Binding Issue

## Issue

The Wazuh Indexer (OpenSearch backend) was initially inaccessible from external integrations and dashboards.

The service was bound to:

```text
127.0.0.1
```

which prevented remote connectivity from Grafana and other integrated services.

## Resolution

The OpenSearch configuration was updated to:

```text
network.host: 0.0.0.0
```

This allowed remote access from authorized SOC services and integrations.

## Outcome

* Grafana successfully connected to OpenSearch
* Dashboard visualization functionality restored
* External integrations became operational

---

# Docker Resource Constraints

## Issue

Shuffle SOAR and DFIR-IRIS services experienced instability and performance issues due to limited EC2 memory resources.

## Resolution

The AWS EC2 instance was upgraded from:

* `t3.medium`

to:

* `t3.xlarge`

Additional Docker resource allocation and service optimization were performed.

## Outcome

* Improved container stability
* Reliable SOAR workflow execution
* Reduced service interruptions

---

# Grafana Data Source Configuration

## Issue

Grafana initially failed to retrieve Wazuh alert data from OpenSearch.

## Resolution

The OpenSearch data source configuration was reviewed and corrected, including:

* Endpoint configuration
* Authentication settings
* Index pattern configuration

## Outcome

* Successful dashboard visualization
* Real-time alert monitoring enabled
* Security metrics became operational

---

# Microsoft Teams Webhook Formatting Issue

## Issue

Microsoft Teams notifications initially failed due to Adaptive Card formatting and webhook payload structure issues.

## Resolution

The notification payload structure was simplified and adjusted to align with supported Teams webhook formatting requirements.

## Outcome

* Automated Teams notifications restored
* Alert delivery successfully integrated into SOC workflows

---

# DFIR-IRIS API Integration Challenges

## Issue

Several DFIR-IRIS API endpoints initially failed during automated case creation and observable management workflows.

## Resolution

API endpoint validation and request structure testing were performed to verify:

* Supported API routes
* Authentication handling
* Payload formatting
* Observable creation methods

Validated endpoints included:

* Case creation
* Notes directory creation
* Observable management

## Outcome

* Automated incident creation operational
* Observable management functioning correctly
* SOAR integrations stabilized

---

# Wazuh Agent Monitoring Challenges

## Issue

Some endpoint agents experienced delayed log ingestion and intermittent monitoring visibility.

## Resolution

Agent configuration and connectivity validation were performed, including:

* Agent registration verification
* Firewall checks
* Connectivity testing
* Log forwarding validation

## Outcome

* Stable endpoint monitoring restored
* Improved log collection reliability
* Enhanced SOC visibility

---

# Lessons From Troubleshooting

The troubleshooting process provided practical experience in:

* SIEM deployment troubleshooting
* Docker service management
* Cloud infrastructure debugging
* API integration validation
* Threat monitoring infrastructure
* SOC operations workflows
* Security platform integration challenges

These experiences improved understanding of real-world SOC deployment and operational challenges within cybersecurity environments.
