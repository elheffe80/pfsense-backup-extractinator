# pfSense Backup Extractinator

A Python script that extracts static DHCP lease information from a pfSense backup XML file and generates a clean markdown table summarizing the static mappings.

## Notes
I am lazy and AI tools have come a long way so I want to be sure it is clear that these scripts are 99% LLM generated.  I give my effort a 1% because it doesn't take much to copy, paste, run, report errors, rinse and repeat until you get the solution these days. 

## Features

- Parses the entire pfSense backup XML file which will need to be renamed to`config.xml`.
- Extracts key static map entries such as MAC address, IP address, hostname, and description.
- Generates a markdown table (`dhcp_static_leases.md`) for easy review and documentation.

## Requirements

- Python 3.x
- Uses only standard Python libraries: `xml.etree.ElementTree`, `html`, and `sys`.

## Installation

1. Clone the repository:   
```
git clone https://github.com/elheffe80/pfsense-backup-extractinator.git
```
2. Move pfsense backup xml to that directory and rename to config.xml
3. ```python3 extract_staticmap.py```

Output should look like:

| MAC Address       | IP Address     | Hostname         | Notes                          |
| ----------------- | -------------- | ---------------- | ------------------------------ |
| 08:00:27:1F:2D:3E | 10.0.0.101     | server1        | Primary database server       |
| 00:16:3E:FF:AA:BB | 10.0.0.102     | server2        | Backup server                 |
| 52:54:00:12:34:56 | 10.0.0.103     | workstation1   | Design workstation            |
| 52:54:00:65:43:21 | 10.0.0.104     | workstation2   | Test workstation              |

- MAC Address - The MAC address used for the DHCP lease.
- IP Address - The IP address given in the lease.
- Hostname - this is the hostname, extracted from the hostname key.
- Notes - this is whatever information was contained within the description field.

## TODO

- [ ] Simultaneously export csv of just MAC and IP
- [ ] Create python script to export to OpnSense
- [ ] Pass XML file as a variable (allowing custom file paths)
- [ ] Create a parent script to manage multiple extract tasks
- [ ] Create a NAT extract script
- [ ] Create a WAN/LAN extract script
- [ ] Be happy
