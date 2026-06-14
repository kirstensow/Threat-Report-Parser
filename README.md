# Threat Report Parser

A Python tool that parses threat intelligence reports and extracts 
Indicators of Compromise (IOCs) into structured JSON output.

## Features
- Handles defanged IOCs (e.g. 192.168.1[.]1 → 192.168.1.1)
- Extracts:
  - IP addresses
  - Domains
  - File hashes (MD5 and SHA-256)
  - Email addresses
  - CVEs
- Deduplicates all extracted IOCs
- Exports structured output to threat_report_iocs.json
  
## How to Use
Run with default files (iocs.csv and results.csv):
python3 Report-Parser.py

Or specify custom input/output files:
python3 main.py --input ThreatReport.txt --output threat_report_iocs.json

For help:
python3 Report-Parser.py --help


## Example Output
```json
{
  "hashes": ["6bb160ebdc59395882ff322e67e000a22a5c54ac..."],
  "ip_addresses": ["194.87.82.7", "195.123.246.20"],
  "domains": ["windowcsupdates.com", "anydeskupdate.com"],
  "emails": ["decrypt.support@privyonline.com"],
  "cves": ["CVE-2023-27350"]
}
```

## Known Limitations
- Domain extraction may include legitimate domains referenced 
  in the report (e.g. vendor URLs). Manual review recommended.

## Built With
- Python 3
- re (built-in)
- json (built-in)
