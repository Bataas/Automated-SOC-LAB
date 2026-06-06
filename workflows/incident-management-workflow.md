# Incident Management Workflow

## Overview

This workflow covers how enriched alerts are escalated into DFIR IRIS as structured incident cases. It handles case creation, field population, asset tagging, and status assignment based on alert severity.

## Flow Diagram

```
Enriched Alert Object (from alert-processing-workflow)
        |
        v
Severity Check (workflow-logic.md thresholds)
        |
        +--- Below threshold ---> Logged only, no case created
        |
        +--- Meets threshold
                |
                v
        DFIR IRIS API (POST /manage/cases/add)
                |
                v
        Case Fields Populated
                |
                v
        IOC Added (POST /manage/ioc/add)
                |
                v
        Asset Tagged (POST /manage/assets/add)
                |
                v
        Case ID returned --> passed to Teams Notification Workflow
```

## Trigger

This workflow is triggered by Shuffle SOAR after the alert processing and enrichment steps are complete. It receives the enriched alert object and proceeds only if the alert meets the minimum severity threshold defined in workflow-logic.md.

## DFIR IRIS Case Creation

Cases are created via the DFIR IRIS REST API using a Bearer token for authentication. SSL verification is disabled for the self-signed certificate used in the lab environment.

### API Endpoint

```
POST /manage/cases/add
Authorization: Bearer <IRIS_API_KEY>
```

### Case Fields

| Field | Value Source | Description |
|---|---|---|
| `case_name` | Wazuh rule.description + timestamp | Human-readable case title |
| `case_description` | Enriched alert summary | Full alert details including enrichment data |
| `case_severity_id` | Mapped from rule.level | IRIS severity (1 = Informational, 4 = Critical) |
| `case_classification_id` | Mapped from rule.groups | IRIS classification category |
| `case_customer_id` | Static (lab environment) | Customer identifier |
| `soc_id` | Wazuh rule.id | Reference back to the originating Wazuh rule |

### Severity Mapping

| Wazuh Rule Level | DFIR IRIS Severity |
|---|---|
| 1 to 6 | Informational (1) |
| 7 to 9 | Low (2) |
| 10 to 12 | Medium (3) |
| 13 to 14 | High (4) |
| 15 | Critical (5) |

## IOC Population

After case creation, Indicators of Compromise are added to the case using the case ID returned from the creation step.

### API Endpoint

```
POST /manage/ioc/add
Authorization: Bearer <IRIS_API_KEY>
```

### IOC Fields

| Field | Value |
|---|---|
| `ioc_value` | Source IP address from the alert |
| `ioc_type_id` | IP address type |
| `ioc_description` | Enrichment summary (VT score, AbuseIPDB confidence, GreyNoise classification) |
| `ioc_tags` | Comma-separated rule groups from Wazuh |

## Asset Tagging

The affected agent is recorded as an asset linked to the case.

### API Endpoint

```
POST /manage/assets/add
Authorization: Bearer <IRIS_API_KEY>
```

### Asset Fields

| Field | Value |
|---|---|
| `asset_name` | Wazuh agent.name |
| `asset_ip` | Wazuh agent.ip |
| `asset_type_id` | Server or Workstation depending on agent type |
| `asset_description` | Agent metadata from Wazuh |

## Case Status Lifecycle

| Status | Description |
|---|---|
| Open | Newly created case, awaiting analyst review |
| In Progress | Analyst has acknowledged and is investigating |
| On Hold | Awaiting additional information or escalation |
| Closed | Investigation complete, outcome documented |

## Output

On successful case creation, the workflow returns:

- `case_id` - Unique DFIR IRIS case identifier (passed to Teams notification)
- `case_url` - Direct link to the case in the IRIS web interface

## Error Handling

| Scenario | Behaviour |
|---|---|
| IRIS API unavailable | Shuffle retries 3 times with 10-second delay; alert logged if all retries fail |
| Duplicate alert received | Checked against open cases; new case created only if no matching case exists within 30 minutes |
| Missing required fields | Case created with available fields; missing data flagged in case description |
| Authentication failure | Workflow halted; error logged to Shuffle execution history |

## Related Documents

- [alert-processing-workflow.md](./alert-processing-workflow.md) - Upstream enrichment that feeds this workflow
- [workflow-logic.md](./workflow-logic.md) - Thresholds and branching logic determining when a case is created
- [teams-notification-workflow.md](./teams-notification-workflow.md) - Notification sent after case creation