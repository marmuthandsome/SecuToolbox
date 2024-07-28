# SecuToolbox

SecuToolbox is a comprehensive security toolset designed to simplify and automate various penetration testing tasks. This tool provides a user-friendly interface to execute common security tools and commands.

## Features

- **FFUF**: Subdomain and directory fuzzing.
- **Nmap**: Full and UDP scans.
- **WhatWeb**: Website fingerprinting.
- **WFuzz**: Subdomain brute-forcing.
- **Gobuster**: Directory, DNS, and virtual host brute-forcing.
- **Dirsearch**: Directory search.
- **SMB Tools**: SMBClient, SMBMap.
- **Evil-WinRM**: Windows Remote Management.
- **CrackMapExec**: SMB and WinRM brute-forcing.
- **RPCClient**: RPC enumeration.
- **Enum4Linux**: Linux enumeration.
- **SNMPWalk**: SNMP enumeration.
- **xFreeRDP**: FreeRDP client.

## Prerequisites

Ensure you have the following tools installed:
- Python 3.x
- FFUF
- Nmap
- WhatWeb
- WFuzz
- Gobuster
- Dirsearch
- SMBClient
- SMBMap
- Evil-WinRM
- CrackMapExec
- RPCClient
- Enum4Linux
- SNMPWalk
- xFreeRDP

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/marmuthandsome/SecuToolbox.git
   cd SecuToolbox

2. Ensure all required tools are installed and available in your PATH.

## Usage

Run the main script to access the menu:
```bash
python secutoolbox.py
```

## Menu Options

- **Linux & Windows**
  - `1. Run ffuf (subdomain)`
  - `2. Run ffuf (directory)`
  - `3. Run nmap (full)`
  - `4. Run nmap (udp)`
  - `5. Run whatweb`
  - `6. Run wfuzz (subdomain)`
  - `7. Run gobuster (directory)`
  - `8. Run gobuster (dns)`
  - `9. Run gobuster (vhost)`
  - `10. Run dirsearch`
- **Active Directory**
  - `11. Run smbclient`
  - `12. Run smbmap`
  - `13. Run evilwinrm (password)`
  - `14. Run evilwinrm (hash)`
  - `15. Run crackmapexec smb (password)`
  - `16. Run crackmapexec smb (hash)`
  - `17. Run crackmapexec evilwinrm (password)`
  - `18. Run crackmapexec evilwinrm (hash)`
  - `19. Run rpcclient`
  - `20. Run enum4linux`
  - `21. Run snmpwalk`
  - `22. Run snmpwalk extend`
  - `23. Run xfreerdp`
- **Other**
  - `99. Addhosts`
  - `0. Exit`

## Example Usage

To run an Nmap full scan:
1. Select option `3` from the menu.
2. Enter the target IP or domain.

To add a host entry:
1. Select option `99` from the menu.
2. Enter the IP and host.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.

## Contact

For any inquiries or issues, please open an issue on GitHub.
