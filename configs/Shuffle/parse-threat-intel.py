import json

vt = json.loads(r'''$virustotal_ip_check''')
abuse = json.loads(r'''$abuseipdb_ip_check''')

summary = {
    "enriched": True,
    "virustotal": {
        "status": vt.get("status"),
        "malicious": None,
        "suspicious": None,
        "harmless": None
    },
    "abuseipdb": {
        "status": abuse.get("status"),
        "abuse_confidence_score": None,
        "country": None,
        "isp": None,
        "usage_type": None
    },
    "verdict": "unknown"
}

try:
    stats = vt["body"]["data"]["attributes"]["last_analysis_stats"]
    summary["virustotal"]["malicious"] = stats.get("malicious")
    summary["virustotal"]["suspicious"] = stats.get("suspicious")
    summary["virustotal"]["harmless"] = stats.get("harmless")
except Exception:
    pass

try:
    data = abuse["body"]["data"]
    summary["abuseipdb"]["abuse_confidence_score"] = data.get("abuseConfidenceScore")
    summary["abuseipdb"]["country"] = data.get("countryCode")
    summary["abuseipdb"]["isp"] = data.get("isp")
    summary["abuseipdb"]["usage_type"] = data.get("usageType")
except Exception:
    pass

vt_malicious = summary["virustotal"]["malicious"] or 0
abuse_score = summary["abuseipdb"]["abuse_confidence_score"] or 0

if vt_malicious >= 5 or abuse_score >= 75:
    summary["verdict"] = "malicious"
elif vt_malicious >= 1 or abuse_score >= 25:
    summary["verdict"] = "suspicious"
else:
    summary["verdict"] = "clean_or_unknown"

summary["note"] = (
    f"Threat Intelligence Enrichment\n"
    f"Verdict: {summary['verdict']}\n"
    f"VirusTotal malicious: {vt_malicious}\n"
    f"VirusTotal suspicious: {summary['virustotal']['suspicious']}\n"
    f"AbuseIPDB score: {abuse_score}\n"
    f"Country: {summary['abuseipdb']['country']}\n"
    f"ISP: {summary['abuseipdb']['isp']}"
)

print(json.dumps(summary))
