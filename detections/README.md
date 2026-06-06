# Detection Engineering

This directory contains detection evidence, MITRE ATT&CK mappings, and alert validation results implemented within the Automated SOC Lab environment.

The detections demonstrate the ability of the SOC platform to identify suspicious activity, generate actionable security alerts, enrich incidents with threat intelligence, and trigger automated response workflows.

---

# Detection Capabilities

The implemented detections include:

* SSH brute-force attack detection
* Privilege escalation monitoring
* File integrity monitoring (FIM)
* SSH lateral movement detection
* Authentication anomaly monitoring
* Threat intelligence-enriched alerting
* Automated Teams alert notifications

---

# Detection Sources

The lab environment primarily utilizes:

* Built-in Wazuh detection capabilities
* SOCFortress Wazuh rule library
* MITRE ATT&CK aligned detections

The project focused on validating, operationalizing, monitoring, and enriching detections within a practical SOC environment rather than developing entirely custom rule sets from scratch.

---

# Detection Workflow

When suspicious activity is detected:

1. Wazuh analyzes incoming logs and security events
2. Detection rules generate security alerts
3. Shuffle SOAR processes the alerts automatically
4. Threat intelligence enrichment is performed
5. DFIR-IRIS incidents are created or updated
6. Microsoft Teams notifications are sent to analysts
7. Security events are visualized within Grafana dashboards

---

# Included Detection Evidence

## SSH Brute-Force Detection

`bruteforce-detection.png`

Demonstrates detection of repeated SSH authentication failures and brute-force attack activity against monitored systems.

### Detection Highlights

* Multiple failed authentication attempts detected
* High-severity Wazuh alert generated
* Automated SOAR workflow triggered
* Threat intelligence enrichment performed
* DFIR-IRIS case creation initiated

### MITRE ATT&CK

* T1110 – Brute Force

---

## Teams Alert Notification

`bruteforce-teams-notification.png`

Demonstrates automated Microsoft Teams notifications generated from detected brute-force activity through the Shuffle SOAR workflow.

### Notification Workflow

* Alert severity included
* Source IP information enriched
* Detection context provided
* SOC alert delivery automated

---

## Privilege Escalation Detection

`privilege-escalation-alert.png`

Shows monitoring and detection of suspicious privilege escalation attempts and elevated administrative activity.

### Detection Highlights

* Suspicious sudo activity detected
* Elevated command execution monitored
* High-severity alert generated
* Incident workflows triggered automatically

### MITRE ATT&CK

* T1548 – Abuse Elevation Control Mechanism

---

## File Integrity Monitoring

`file-integrity-monitoring.png`

Demonstrates Wazuh File Integrity Monitoring (FIM) detecting unauthorized modifications to monitored system files.

### Detection Highlights

* Critical file modification monitoring
* Unauthorized system file changes detected
* FIM alerts generated and visualized
* Security monitoring validation performed

### MITRE ATT&CK

* T1565 – Data Manipulation

---

## Lateral Movement Detection

`lateral-movement-alert.png`

Shows detection of suspicious SSH remote access and lateral movement activity between monitored systems.

### Detection Highlights

* Remote authentication monitoring
* Cross-system SSH activity detection
* Suspicious access pattern visibility
* Automated incident workflows triggered

### MITRE ATT&CK

* T1021 – Remote Services

---

## MITRE ATT&CK Mapping

`mitre-mapping.png`
`mitre-mapping.md`

Contains mappings between implemented detections and associated MITRE ATT&CK techniques.

### Implemented ATT&CK Techniques

| Technique ID | Technique Name                    | Detection Scenario        |
| ------------ | --------------------------------- | ------------------------- |
| T1110        | Brute Force                       | SSH brute-force attacks   |
| T1548        | Abuse Elevation Control Mechanism | Privilege escalation      |
| T1565        | Data Manipulation                 | File integrity monitoring |
| T1021        | Remote Services                   | SSH lateral movement      |

---

# Detection Summary

The implemented detection workflows successfully demonstrated the capability of the Automated SOC Lab environment to:

* Detect suspicious authentication activity
* Monitor privilege escalation attempts
* Identify unauthorized system modifications
* Detect lateral movement behavior
* Trigger automated incident response workflows
* Generate real-time security notifications
* Enrich alerts using threat intelligence platforms
* Map detections to MITRE ATT&CK techniques

The detection pipeline integrates SIEM monitoring, SOAR automation, DFIR case management, and threat intelligence enrichment to simulate practical SOC operations and incident response processes.

---

# Purpose

These detections were implemented and validated to:

* Improve SOC visibility
* Support threat monitoring
* Trigger automated response workflows
* Validate attack simulation scenarios
* Enhance incident investigation capabilities
* Demonstrate practical detection engineering concepts
* Simulate real-world SOC operations

All detections and testing activities were performed within authorized and isolated lab environments for educational and research purposes only.
