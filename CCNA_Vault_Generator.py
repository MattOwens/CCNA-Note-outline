import os
import re
import shutil

# --- BLUEPRINT DICTIONARY (No changes needed here) ---
blueprint = {
    "1.0 Network Fundamentals": {
        "1.1 Role and function of network components": {
            "1.1.a Routers": "V1 Ch3, Ch16",
            "1.1.b Layer 2 and Layer 3 switches": "V1 Ch2, Ch5–7",
            "1.1.c Next-generation firewalls and IPS": "V2 Ch9",
            "1.1.d Access points": "V2 Ch1–3",
            "1.1.e Controllers (Cisco DNA Center and WLC)": "V2 Ch2, Ch21–22",
            "1.1.f Endpoints": "V1 Ch1",
            "1.1.g Servers": "V2 Ch20",
            "1.1.h PoE": "V2 Ch1 (light coverage)",
        },
        "1.2 Network topology architectures": {
            "1.2.a Two-tier": "V2 Ch18",
            "1.2.b Three-tier": "V2 Ch18",
            "1.2.c Spine-leaf": "V2 Ch19",
            "1.2.d WAN": "V2 Ch20",
            "1.2.e SOHO": "V1 Ch1",
            "1.2.f On-premise and cloud": "V2 Ch20",
        },
        "1.3 Physical interface and cabling types": {
            "1.3.a Single-mode fiber, multimode fiber, copper": "V1 Ch2–3",
            "1.3.b Ethernet shared media and point-to-point": "V1 Ch2–3",
        },
        "1.4 Interface and cable issues": "V1 Ch5, Ch7",
        "1.5 Compare TCP to UDP": "V1 Ch1",
        "1.6 IPv4 addressing and subnetting": "V1 Ch11–15",
        "1.7 Private IPv4 addressing": "V1 Ch11–12",
        "1.8 IPv6 addressing and prefix": "V1 Ch25–28",
        "1.9 IPv6 address types": "V1 Ch25–26",
        "1.10 Verify IP parameters for client OS": "V1 Ch19",
        "1.11 Wireless principles": "V2 Ch1–3",
        "1.12 Virtualization fundamentals": "V2 Ch20",
        "1.13 Switching concepts": "V1 Ch5",
    },
    "2.0 Network Access": {
        "2.1 VLANs": {
            "2.1.a Access ports (data and voice)": "V1 Ch8",
            "2.1.b Default VLAN": "V1 Ch8",
            "2.1.c Inter-VLAN connectivity": "V1 Ch18",
        },
        "2.2 Interswitch connectivity": {
            "2.2.a Trunks": "V1 Ch8",
            "2.2.b 802.1Q": "V1 Ch8",
            "2.2.c Native VLAN": "V1 Ch8",
        },
        "2.3 CDP and LLDP": "V1 Ch6–7",
        "2.4 EtherChannel (LACP)": "V1 Ch10",
        "2.5 Rapid PVST+": "V1 Ch9–10",
        "2.6 Wireless architectures and AP modes": "V2 Ch2",
        "2.7 WLAN physical connections": "V2 Ch1–4",
        "2.8 Device management access": "V1 Ch4, V2 Ch10",
        "2.9 WLAN GUI interpretation": "V2 Ch3–4",
    },
    "3.0 IP Connectivity": {
        "3.1 Routing table components": "V1 Ch16–17",
        "3.2 Forwarding decisions": "V1 Ch16–17",
        "3.3 IPv4 and IPv6 static routing": "V1 Ch17, Ch29",
        "3.4 Single-area OSPFv2": "V1 Ch21–24",
        "3.5 First-hop redundancy (HSRP, VRRP, GLBP)": "V2 Ch16",
    },
    "4.0 IP Services": {
        "4.1 NAT (static, pools)": "V2 Ch14",
        "4.2 NTP client and server": "V2 Ch13",
        "4.3 DHCP and DNS roles": "V1 Ch19; V2 Ch13",
        "4.4 SNMP": "V2 Ch17",
        "4.5 Syslog": "V2 Ch13",
        "4.6 DHCP client and relay": "V1 Ch19; V2 Ch12",
        "4.7 QoS PHB": "V2 Ch15",
        "4.8 SSH remote access": "V2 Ch10",
        "4.9 TFTP and FTP": "V2 Ch17",
    },
    "5.0 Security Fundamentals": {
        "5.1 Security concepts": "V2 Ch9",
        "5.2 Security program elements": "V2 Ch9",
        "5.3 Local device access control": "V2 Ch10",
        "5.4 Password policies": "V2 Ch10",
        "5.5 IPsec VPNs": "V2 Ch9",
        "5.6 ACLs": "V2 Ch6–8",
        "5.7 L2 security (DHCP snooping, DAI, port security)": "V2 Ch11–12",
        "5.8 AAA concepts": "V2 Ch9–10",
        "5.9 Wireless security": "V2 Ch3",
        "5.10 WLAN GUI WPA2 PSK": "V2 Ch3–4",
    },
    "6.0 Automation and Programmability": {
        "6.1 Automation impact": "V2 Ch21",
        "6.2 Traditional vs controller-based": "V2 Ch21",
        "6.3 SDN architecture": "V2 Ch21–22",
        "6.4 AI and ML in networking": "V2 Ch21–22",
        "6.5 REST APIs": "V2 Ch23",
        "6.6 Ansible and Terraform": "V2 Ch24",
        "6.7 JSON data": "V2 Ch23",
    }
}

# --- TEMPLATE FOR THE NEW MASTER REFERENCE DOCUMENT ---
master_reference_content = """
# MASTER REFERENCE DOCUMENT

This is your central "cheat sheet" for critical information that needs to be memorized or referenced frequently.

---

## Common Port Numbers

| Protocol | Port # | Purpose |
| :--- | :--- | :--- |
| FTP | 20, 21 | File Transfer Protocol |
| SSH | 22 | Secure Shell |
| Telnet | 23 | |
| SMTP | 25 | |
| DNS | 53 | |
| DHCP | 67, 68 | |
| TFTP | 69 | |
| HTTP | 80 | |
| POP3 | 110 | |
| NTP | 123 | |
| IMAP | 143 | |
| SNMP | 161, 162 | |
| HTTPS | 443 | |
| Syslog | 514 | |

---

## Default Administrative Distances (AD)

| Route Source | AD |
| :--- | :--- |
| Connected | 0 |
| Static | 1 |
| EIGRP (Internal) | 90 |
| OSPF | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EIGRP (External) | 170 |
| iBGP | 200 |
| eBGP | 20 |

---

## Private IPv4 Address Ranges (RFC 1918)

| Class | Range | CIDR |
| :--- | :--- | :--- |
| Class A | 10.0.0.0 - 10.255.255.255 | /8 |
| Class B | 172.16.0.0 - 172.31.255.255 | /12 |
| Class C | 192.168.0.0 - 192.168.255.255 | /16 |

---

## IPv6 Address Types

| Type | Prefix | Description |
| :--- | :--- | :--- |
| Global Unicast | 2000::/3 | Publicly routable addresses. |
| Unique Local | FC00::/7 | Private, non-routable (like RFC 1918). |
| Link-Local | FE80::/10 | Required on every IPv6 interface, for local segment communication only. |
| Multicast | FF00::/8 | Used to send packets to a group of devices. |

"""

# --- TEMPLATE FOR THE NEW GENERAL OVERVIEW DOCUMENT ---
general_overview_content = """
# GENERAL OVERVIEW & OUTLINE

This document is your high-level dashboard and table of contents for the entire CCNA vault. Use it to track your overall progress and quickly navigate to the main exam domains.

---

## Exam Blueprint Domains

*   [1.0 Network Fundamentals](1.0%20Network%20Fundamentals)
*   [2.0 Network Access](2.0%20Network%20Access)
*   [3.0 IP Connectivity](3.0%20IP%20Connectivity)
*   [4.0 IP Services](4.0%20IP%20Services)
*   [5.0 Security Fundamentals](5.0%20Security%20Fundamentals)
*   [6.0 Automation and Programmability](6.0%20Automation%20and%20Programmability)

---

## Study Workflow

1.  **Read:** Review the relevant chapter(s) in the Official Cert Guide.
2.  **Note:** Fill out the `Key Concepts & Definitions` in your own words in the corresponding Obsidian note.
3.  **Link:** Actively create `[[links]]` to related concepts as you write.
4.  **Lab:** Perform the practical exercises. Document your steps and verification in the note.
5.  **Test:** Use Boson ExSim to test your knowledge.
6.  **Refine:** Add any "gotchas" or insights from Boson back into your Obsidian notes to close knowledge gaps.

"""

def sanitize_filename(name):
    """Removes invalid characters for filenames."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

def create_note_content(objective_code_and_title, book_chapters):
    """Creates the markdown content for a note, with the new sections."""
    parts = objective_code_and_title.split(' ', 1)
    objective_code = parts[0]
    title_words = re.findall(r'[A-Za-z0-9]+', objective_code_and_title)
    # Generate cleaner tags by excluding common small words
    excluded_words = {"and", "or", "to", "a", "the", "with", "of", "in", "vs", "v2", "v3", "for", "from", "on", "is"}
    clean_tags = [f"#{word.lower()}" for word in title_words if word.lower() not in excluded_words and not word.isdigit()]
    suggested_tags = f"#ccna {' '.join(clean_tags)}"

    content_lines = [
        f"# {objective_code_and_title}",
        "",
        f"**Objective Code:** {objective_code}",
        f"**Book Chapters:** {book_chapters}",
        f"**Tags:** {suggested_tags}",
        "",
        "## Progress",
        "- [ ] Read",
        "- [ ] Labbed",
        "- [ ] Tested",
        "",
        "## What You Need to Know",
        "",
        "### Key Concepts & Definitions",
        "- ",
        "",
        "## How to Lab It",
        "",
        "### Configuration Steps",
        "- ",
        "",
        "### Verification Commands",
        "- ",
        "",
        "## Related Concepts",
        "- [[ ]]",
        "- [[ ]]",
    ]
    return "\n".join(content_lines).strip() + "\n"

def create_vault(base_path, data):
    """Recursively creates folders and files."""
    os.makedirs(base_path, exist_ok=True)
    print(f"Created folder: {base_path}")
    for name, content in sorted(data.items()):
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            create_vault(current_path, content)
        else:
            file_name = sanitize_filename(name) + ".md"
            file_path = os.path.join(base_path, file_name)
            note_content = create_note_content(name, content) 
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(note_content)
            print(f"  - Created file: {file_path}")

if __name__ == "__main__":
    vault_name = "CCNA 200-301"
    print(f"Starting vault creation for '{vault_name}'...")
    
    if os.path.exists(vault_name):
        shutil.rmtree(vault_name)
        print(f"Removed existing '{vault_name}' folder for a clean rebuild.")

    # Create the main blueprint structure
    create_vault(vault_name, blueprint)
    
    # --- CREATE THE TWO NEW MASTER FILES ---
    # Create MASTER REFERENCE.md
    with open(os.path.join(vault_name, "MASTER REFERENCE.md"), 'w', encoding='utf-8') as f:
        f.write(master_reference_content)
    print(f"\n- Created top-level file: {os.path.join(vault_name, 'MASTER REFERENCE.md')}")

    # Create GENERAL OVERVIEW & OUTLINE.md
    with open(os.path.join(vault_name, "GENERAL OVERVIEW & OUTLINE.md"), 'w', encoding='utf-8') as f:
        f.write(general_overview_content)
    print(f"- Created top-level file: {os.path.join(vault_name, 'GENERAL OVERVIEW & OUTLINE.md')}")
    
    print("\nVault creation complete!")
    print(f"You can now open the '{vault_name}' folder in Obsidian.")

