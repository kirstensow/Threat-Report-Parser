
import json
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', default= 'ThreatReport.txt' , help='input file')
parser.add_argument('--output', default= 'threat_report_iocs.json' , help='output file')
args = parser.parse_args()

def defang_cleaner(contents):
    return contents.replace('[.]', '.') #Removes square brackets

def hashes (contents):
    hash_pattern = re.compile(r'[0-9a-fA-F]{64}|[0-9a-fA-F]{32}') #Looks for MD5 Hashes and SHA256
    hash_match = hash_pattern.findall(contents)
    print(hash_match)
    return hash_match

def ip (contents):
    ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    ip_match = ip_pattern.findall(contents)
    print(ip_match)
    return ip_match

def domain (contents):
    domain_pattern = re.compile(r'\b[\w\-]+\.(?:com|net|org|io|gov|edu|ru|ge|info)\b')
    domain_match = domain_pattern.findall(contents)
    print(domain_match)
    return domain_match

def email (contents):
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    email_match = email_pattern.findall(contents)
    print(email_match)
    return email_match

def cve(contents):
    cve_pattern = re.compile(r'CVE-\d{4}-\d{4,5}')
    cve_match = cve_pattern.findall(contents)
    print(cve_match)
    return cve_match


def json_converter(hash_match, ip_match, domain_match, email_match, cve_match):
        iocs = { #convert to dictionary and deduplicates
            'hashes': list(set(hash_match)),
            'ip_addresses': list(set(ip_match)),
            'emails': list(set(email_match)),
            'cves': list(set(cve_match)),
            'domains': list(set(domain_match))
        }
        with open('threat_report_iocs.json', 'w') as file: #create json file
            json.dump(iocs, file, indent=2) #convert dictionary to json
        print(json.dumps(iocs, indent=2))


with open (args.input, 'r') as file:
    contents = defang_cleaner(file.read())
    hash_match = hashes(contents)
    ip_match = ip(contents)
    domain_match = domain(contents)
    email_match = email(contents)
    cve_match = cve(contents)
    json_converter(hash_match, ip_match, domain_match, email_match, cve_match)



