import json, hashlib, ipaddress
from datetime import datetime, timezone

raw = json.loads(r'''$exec''')

# New Wazuh webhook format support
alert = raw.get("all_fields", raw)

rule = alert.get("rule", {})
agent = alert.get("agent", {})
data = alert.get("data", {})
decoder = alert.get("decoder", {})
manager = alert.get("manager", {})

rule_id = str(rule.get("id") or raw.get("rule_id") or "")
rule_name = rule.get("description") or raw.get("title") or "Unknown Wazuh Alert"
wazuh_level = int(rule.get("level") or raw.get("severity") or 0)

src_ip = data.get("srcip") or data.get("src_ip") or data.get("sourceIp")
dst_ip = data.get("dstip") or data.get("dst_ip") or data.get("destinationIp")
username = data.get("srcuser") or data.get("dstuser") or data.get("user") or data.get("username")

hostname = agent.get("name") or alert.get("predecoder", {}).get("hostname")
agent_ip = agent.get("ip")
alert_id = alert.get("id") or raw.get("id")
timestamp = alert.get("timestamp") or raw.get("timestamp") or datetime.now(timezone.utc).isoformat()

def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_global
    except Exception:
        return False

is_public_ioc = is_public_ip(src_ip) if src_ip else False

# Severity mapping
if wazuh_level >= 13:
    severity = "Critical"
    iris_severity = 4
elif wazuh_level >= 10:
    severity = "High"
    iris_severity = 3
elif wazuh_level >= 7:
    severity = "Medium"
    iris_severity = 2
else:
    severity = "Low"
    iris_severity = 1

# Force important brute force alerts to proceed even if wrapper severity is low
title_text = f"{rule_name} {raw.get('title', '')} {raw.get('text', '')}".lower()
is_bruteforce = (
    "brute force" in title_text
    or rule_id in ["5710", "5712"]
)

proceed = False
reason = "low_severity"

if wazuh_level >= 7:
    proceed = True
    reason = "severity_threshold_met"

if is_bruteforce and src_ip:
    proceed = True
    severity = "Medium"
    iris_severity = 2
    reason = "bruteforce_alert"

if not alert_id or not rule_name:
    proceed = False
    reason = "missing_alert_id_or_rule"

dedup_seed = f"{rule_id}|{rule_name}|{hostname}|{src_ip}|{username}"
dedup_key = hashlib.sha256(dedup_seed.encode()).hexdigest()
dedup_tag = f"dedup:{dedup_key}"

observables = []

if src_ip:
    observables.append({
        "type": "ip",
        "value": src_ip,
        "tags": ["wazuh", "source_ip"]
    })

if dst_ip:
    observables.append({
        "type": "ip",
        "value": dst_ip,
        "tags": ["wazuh", "destination_ip"]
    })

if hostname:
    observables.append({
        "type": "hostname",
        "value": hostname,
        "tags": ["wazuh", "host"]
    })

case_title = f"[{severity}] {rule_name} - {hostname or 'Unknown Host'}"

case_description = (
    f"Wazuh alert received by Shuffle SOAR and normalized for SOC triage. "
    f"Rule ID: {rule_id}. Rule Name: {rule_name}. "
    f"Host: {hostname}. Source IP: {src_ip}. User: {username}."
)

result = {
    "proceed": proceed,
    "reason": reason,
    "dedup_key": dedup_key,
    "dedup_tag": dedup_tag,
    "dedup_seed": dedup_seed,
    "case_title": case_title,
    "case_description": case_description,
    "severity": severity,
    "iris_severity": iris_severity,
    "tags": [
        "wazuh",
        "shuffle",
        severity.lower(),
        dedup_tag
    ],
    "observables": observables,
    "alert_meta": {
        "source": "wazuh",
        "alert_id": alert_id,
        "rule_id": rule_id,
        "rule_name": rule_name,
        "wazuh_level": wazuh_level,
        "iris_severity": iris_severity,
        "alert_type": "bruteforce" if is_bruteforce else "generic",
        "mitre_id": rule.get("mitre", {}).get("id"),
        "mitre_tactic": rule.get("mitre", {}).get("tactic"),
        "timestamp": timestamp,
        "location": alert.get("location"),
        "decoder": decoder.get("name"),
        "manager": manager.get("name")
    },
    "host_context": {
        "hostname": hostname,
        "agent_id": agent.get("id"),
        "agent_name": agent.get("name"),
        "agent_ip": agent_ip
    },
    "user_context": {
        "username": username,
        "domain": data.get("domain"),
        "identity": username
    },
    "network_iocs": {
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "src_port": data.get("srcport"),
        "dst_port": data.get("dstport"),
        "is_public_ioc": is_public_ioc
    },
    "iris": {
        "search_value": dedup_tag,
        "case_create_payload": {
            "case_name": case_title,
            "case_description": f"DEDUP_TAG: {dedup_tag}",
            "case_soc_id": f"WAZUH-{alert_id}",
            "case_severity_id": iris_severity,
            "case_tags": ["wazuh", "shuffle", severity.lower(), dedup_tag]
        },
        "duplicate_note": {
            "title": "Duplicate Wazuh Alert Received",
            "content": f"Repeated alert matched this case. Rule: {rule_name}. Source IP: {src_ip}. User: {username}."
        }
    },
    "_raw": alert,
    "_pipeline": {
        "node": "Build_SOC_Context",
        "status": "ok",
        "processed_at": datetime.now(timezone.utc).isoformat()
    }
}

print(json.dumps(result))