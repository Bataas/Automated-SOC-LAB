# Workflow Logic

## Overview

This document describes the decision logic, severity thresholds, branching conditions, and routing rules that govern how alerts flow through the SOC automation pipeline. It serves as the central reference for understanding why an alert is handled in a particular way at each stage.

## Global Decision Flow

```
Alert Received by Shuffle (from Wazuh webhook)
        |
        v
[1] Is rule.level >= minimum threshold?
        |
        +--- No  ---> Discard / log only. No further action.
        |
        +--- Yes
                |
                v
        [2] Does alert contain a source IP?
                |
                +--- No  ---> Skip enrichment. Proceed to severity classification.
                |
                +--- Yes
                        |
                        v
                [3] IP Enrichment (VirusTotal + AbuseIPDB + GreyNoise)
                        |
                        v
                [4] Classify enriched severity
                        |
                        v
                [5] Is severity >= case creation threshold?
                        |
                        +--- No  ---> Send low-priority Teams alert only. No IRIS case.
                        |
                        +--- Yes
                                |
                                v
                        [6] Create DFIR IRIS case
                                |
                                v
                        [7] Send Teams Adaptive Card with case link
```

## Threshold Definitions

### Minimum Alert Threshold

| Parameter | Value | Description |
|---|---|---|
| Minimum rule level | 7 | Alerts below this level are discarded with no action |
| Maximum rule level | 15 | Highest possible Wazuh severity |

Alerts at level 1 to 6 are considered informational and are indexed in OpenSearch for dashboarding but do not trigger any workflow action.

### Case Creation Threshold

| Parameter | Value | Description |
|---|---|---|
| Minimum level for IRIS case | 10 | Alerts at level 7 to 9 trigger Teams notification only |
| Enrichment override | Yes | An alert at level 7 to 9 is escalated to case creation if AbuseIPDB confidence >= 85% or VirusTotal malicious count >= 5 |

### Enrichment-Based Escalation Rules

These rules can override the base rule level threshold and trigger case creation even for lower-severity alerts.

| Condition | Action |
|---|---|
| AbuseIPDB confidence score >= 85% | Escalate to case creation regardless of rule level |
| VirusTotal malicious engines >= 5 | Escalate to case creation regardless of rule level |
| GreyNoise classification = malicious | Escalate to case creation regardless of rule level |
| GreyNoise RIOT = true | Suppress Teams notification (benign infrastructure) |
| All enrichment sources return clean | Downgrade severity by 1 level for routing purposes |

## Severity Classification

After enrichment, the alert is assigned a final classification used for IRIS case severity and Teams card colour.

| Final Classification | Conditions |
|---|---|
| Critical | rule.level = 15, or VT malicious >= 20, or AbuseIPDB >= 95% |
| High | rule.level 13 to 14, or VT malicious >= 10, or AbuseIPDB >= 85% |
| Medium | rule.level 10 to 12, or VT malicious >= 5, or AbuseIPDB >= 60% |
| Low | rule.level 7 to 9, enrichment below all escalation thresholds |
| Informational | rule.level 1 to 6 (no workflow action) |

## Deduplication Logic

To prevent case flooding from repeated alerts, the following deduplication check is applied before creating an IRIS case.

| Parameter | Value |
|---|---|
| Deduplication window | 30 minutes |
| Match criteria | Same rule.id AND same source IP |
| Behaviour on duplicate | Skip case creation; send a Teams update referencing the existing case ID |

## Branching Summary

| Branch | Condition | Outcome |
|---|---|---|
| Discard | rule.level < 7 | No action; alert indexed in OpenSearch only |
| Notify only | rule.level 7 to 9 AND enrichment below escalation thresholds | Teams alert sent; no IRIS case |
| Full escalation | rule.level >= 10 OR enrichment escalation rule triggered | IRIS case created AND Teams alert sent |
| Suppressed | GreyNoise RIOT = true | No Teams alert; case created at Low severity for audit purposes |
| Partial enrichment | One or more enrichment APIs unavailable | Workflow continues; missing data noted in case and card |

## Timing and Sequencing

| Step | Expected Duration |
|---|---|
| Webhook receipt to Shuffle trigger | < 1 second |
| Alert parsing | < 1 second |
| VirusTotal enrichment | 2 to 5 seconds |
| AbuseIPDB enrichment | 1 to 3 seconds |
| GreyNoise enrichment | 1 to 3 seconds |
| IRIS case creation | 2 to 4 seconds |
| Teams notification delivery | 1 to 2 seconds |
| Total end-to-end (typical) | 8 to 18 seconds |

## Configuration Variables

All thresholds listed in this document are configurable via environment variables. No values are hardcoded in the Shuffle workflow.

| Environment Variable | Default | Description |
|---|---|---|
| `MIN_ALERT_LEVEL` | 7 | Minimum Wazuh rule level to trigger workflow |
| `CASE_CREATION_LEVEL` | 10 | Minimum level to create an IRIS case |
| `ABUSEIPDB_ESCALATION_THRESHOLD` | 85 | AbuseIPDB confidence % to force case creation |
| `VIRUSTOTAL_ESCALATION_THRESHOLD` | 5 | VT malicious engine count to force case creation |
| `DEDUP_WINDOW_MINUTES` | 30 | Deduplication window in minutes |

## Related Documents

- [alert-processing-workflow.md](./alert-processing-workflow.md) - Enrichment steps where logic is applied
- [incident-management-workflow.md](./incident-management-workflow.md) - Case creation triggered by this logic
- [teams-notification-workflow.md](./teams-notification-workflow.md) - Notification conditions governed by this logic