# Attack Simulations

This directory contains screenshots from controlled attack simulations performed within the Automated SOC Lab environment.

The simulations were conducted to validate SIEM detections, SOAR automation workflows, incident response capabilities, and SOC monitoring visibility.

---

# Simulated Attack Scenarios

## SSH Brute-Force Attack

`hydra-ssh-bruteforce.png`

Demonstrates SSH brute-force activity performed using Hydra against a monitored Linux endpoint.

### Validation Goals

* Trigger Wazuh authentication alerts
* Execute automated SOAR workflows
* Generate Microsoft Teams notifications
* Create DFIR-IRIS investigation cases

### MITRE ATT&CK

* T1110 – Brute Force

---

## Network Reconnaissance

`nmap-reconnaissance.png`

Demonstrates reconnaissance and network scanning activity performed using Nmap against monitored systems.

### Validation Goals

* Simulate attacker reconnaissance behavior
* Generate network scanning visibility
* Validate monitoring and alert generation

### MITRE ATT&CK

* T1046 – Network Service Scanning

---

## File Integrity Monitoring Simulation

`file-integrity-simulation.png`

Demonstrates monitored file modification activity used to validate File Integrity Monitoring (FIM) capabilities.

### Validation Goals

* Trigger Wazuh FIM alerts
* Detect unauthorized file changes
* Validate system monitoring visibility

### MITRE ATT&CK

* T1565 – Data Manipulation

---

## SSH Lateral Movement

`ssh-lateral-movement.png`

Demonstrates SSH-based remote access and lateral movement activity between monitored systems.

### Validation Goals

* Simulate remote service abuse
* Generate authentication monitoring events
* Validate lateral movement visibility

### MITRE ATT&CK

* T1021 – Remote Services

---

# Purpose

These simulations were performed to:

* Validate detection visibility
* Test SOC monitoring workflows
* Trigger automated incident response processes
* Simulate practical attacker behavior
* Verify threat intelligence enrichment workflows
* Evaluate overall SOC operational capability

All testing activities were conducted within isolated and authorized lab environments for educational and research purposes only.
