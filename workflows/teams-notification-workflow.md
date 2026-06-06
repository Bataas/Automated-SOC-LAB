# Teams Notification Workflow

## Overview

This workflow covers how Microsoft Teams Adaptive Card alerts are constructed and delivered to the SOC analyst channel after an alert has been processed and an incident case created in DFIR IRIS.

## Flow Diagram

```
Enriched Alert + IRIS Case ID (from incident-management-workflow)
        |
        v
Adaptive Card Payload Constructed
        |
        v
Severity Colour Assigned
        |
        v
HTTP POST to Teams Incoming Webhook URL
        |
        v
Adaptive Card Rendered in SOC Analyst Channel
```

## Trigger

This workflow is triggered by Shuffle SOAR after the incident management workflow returns a DFIR IRIS case ID. It runs in parallel with or immediately after case creation depending on workflow branch configuration.

## Adaptive Card Structure

The Teams notification is delivered as a Microsoft Adaptive Card via an Incoming Webhook connector. The card is structured to give analysts all critical information at a glance without needing to open IRIS immediately.

### Card Sections

| Section | Content |
|---|---|
| Header | Alert title (rule.description) with severity colour banner |
| Alert Details | Rule ID, rule level, timestamp, agent name, agent IP |
| Source IP | Raw IP address from the alert |
| Threat Intelligence | VirusTotal malicious score, AbuseIPDB confidence %, GreyNoise classification |
| IRIS Case | Case ID and direct URL link to the case |
| Actions | Button linking directly to the IRIS case |

### Severity Colour Mapping

The card header colour changes based on alert severity to allow analysts to triage at a glance.

| Wazuh Rule Level | Colour | Label |
|---|---|---|
| 1 to 6 | Grey | Informational |
| 7 to 9 | Blue | Low |
| 10 to 12 | Yellow / Amber | Medium |
| 13 to 14 | Orange | High |
| 15 | Red | Critical |

## Sample Adaptive Card Payload

```json
{
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.4",
        "body": [
          {
            "type": "TextBlock",
            "text": "SOC ALERT - Authentication Brute Force Detected",
            "weight": "Bolder",
            "size": "Medium",
            "color": "Attention"
          },
          {
            "type": "FactSet",
            "facts": [
              { "title": "Rule ID", "value": "5763" },
              { "title": "Severity Level", "value": "12 - Medium" },
              { "title": "Agent", "value": "ubuntu-agent-01 (10.0.1.15)" },
              { "title": "Source IP", "value": "203.0.113.47" },
              { "title": "Timestamp", "value": "2025-05-01T14:32:11Z" }
            ]
          },
          {
            "type": "TextBlock",
            "text": "Threat Intelligence",
            "weight": "Bolder"
          },
          {
            "type": "FactSet",
            "facts": [
              { "title": "VirusTotal", "value": "7/94 engines flagged malicious" },
              { "title": "AbuseIPDB", "value": "87% abuse confidence - 142 reports" },
              { "title": "GreyNoise", "value": "malicious - known scanner" }
            ]
          },
          {
            "type": "TextBlock",
            "text": "IRIS Case: INC-0042",
            "weight": "Bolder"
          }
        ],
        "actions": [
          {
            "type": "Action.OpenUrl",
            "title": "Open in DFIR IRIS",
            "url": "https://<iris-host>/case?cid=42"
          }
        ]
      }
    }
  ]
}
```

## Delivery

The card is delivered via an HTTP POST request to the Microsoft Teams Incoming Webhook URL configured for the SOC analyst channel.

```
POST <TEAMS_WEBHOOK_URL>
Content-Type: application/json
Body: Adaptive Card JSON payload
```

The webhook URL is stored as an environment variable and is not hardcoded in the workflow.

## Notification Conditions

| Condition | Notification Sent |
|---|---|
| Alert level >= 7 | Yes |
| Alert level < 7 | No (logged only) |
| IRIS case creation succeeded | Yes, with case ID and link |
| IRIS case creation failed | Yes, with warning that case creation failed |
| Enrichment data unavailable | Yes, with note that enrichment is partial |

## Error Handling

| Scenario | Behaviour |
|---|---|
| Teams webhook unavailable | Shuffle retries up to 3 times with 5-second delay |
| Payload construction failure | Error logged to Shuffle execution history; no card sent |
| Card delivery confirmed (HTTP 200) | Workflow marked as successful |
| Card delivery failed (non-200) | Workflow logs failure with response code |

## Related Documents

- [alert-processing-workflow.md](./alert-processing-workflow.md) - Enrichment data used to populate the card
- [incident-management-workflow.md](./incident-management-workflow.md) - Case ID and URL included in the card
- [workflow-logic.md](./workflow-logic.md) - Conditions that determine whether a notification is sent