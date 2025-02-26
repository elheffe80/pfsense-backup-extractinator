# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module Name: dhcp_static_leases.py
Author: Ben Heffron
Created: 2025-02-25
Version: 1.0
License: Apache License, Version 2.0

This module parses an XML configuration file to extract static DHCP lease information and
generates a markdown table.  It is 99.999% generated code.  I am not this good.
"""

import xml.etree.ElementTree as ET
import html
import sys

def parse_xml(xml_file):
    """Parse the XML file, with a fallback wrapper in case of a parsing error."""
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    try:
        return ET.fromstring(xml_content)
    except ET.ParseError:
        return ET.fromstring(f"<root>{xml_content}</root>")

def parse_staticmaps(xml_file):
    """Extract staticmap entries from the XML and return a markdown table as a string."""
    root = parse_xml(xml_file)
    staticmaps = root.findall(".//staticmap") or root.findall("staticmap")
    
    # Create the markdown table header
    lines = [
        "| MAC Address | IP Address | Hostname | Notes |",
        "|------------|------------|----------|-------|"
    ]
    
    # Process each staticmap entry and add a row to the table
    for smap in staticmaps:
        mac = smap.findtext("mac", "")
        ipaddr = smap.findtext("ipaddr", "")
        hostname = smap.findtext("hostname", "")
        descr = smap.findtext("descr", "")
        if descr:
            descr = html.unescape(descr).strip()
        line = f"| {mac} | {ipaddr} | {hostname} | {descr} |"
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == "__main__":
    xml_file = "config.xml"
    try:
        markdown_table = parse_staticmaps(xml_file)
        with open("dhcp_static_leases.md", "w") as md_file:
            md_file.write(markdown_table)
    except Exception as e:
        sys.exit(1)
