<img width="800" height="300" alt="SecuToolbox-logo" src="https://raw.githubusercontent.com/marmuthandsome/SecuToolbox/8c8f9ec0caf5a7beb7e2cdd6a1fdead20f3f7886/secutoolbox-logo.svg" /><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300" width="800" height="300">


# SecuToolbox

SecuToolbox is a comprehensive security toolset designed to simplify and automate various penetration testing tasks. This tool provides a user-friendly interface to execute common security tools and commands.

## Features

### Network Scanning
- **Nmap**: Full and UDP scans.
- **RustScan**: Fast port scanner with nmap integration.

### Web Fuzzing & Discovery
- **FFUF**: Subdomain and directory fuzzing.
- **WhatWeb**: Website fingerprinting.
- **WFuzz**: Subdomain brute-forcing.
- **Gobuster**: Directory, DNS, and virtual host brute-forcing.
- **Dirsearch**: Directory search.
- **Feroxbuster**: Fast content discovery.

### Active Directory Tools
- **SMB Tools**: SMBClient, SMBMap.
- **Evil-WinRM**: Windows Remote Management.
- **CrackMapExec**: SMB and WinRM brute-forcing.
- **RPCClient**: RPC enumeration.
- **Enum4Linux**: Linux enumeration.
- **Enum4Linux-ng**: Next generation Linux/Windows enumeration.
- **SNMPWalk**: SNMP enumeration.
- **xFreeRDP**: FreeRDP client.
- **Impacket Suite**: GetNPUsers, GetADUsers, GetUserSPNs, Secretsdump, Psexec, MSSQLClient.
- **Kerbrute**: Kerberos bruteforce.
- **DNSenum**: DNS enumeration.
- **LDAP Search**: LDAP enumeration.

### Security Analysis Tools
- **JWT Tool**: JSON Web Token analysis and exploitation.
- **ExifTool**: File metadata extraction and analysis.
- **Hash Identifier**: Identify hash types.
- **MSFVenom**: Metasploit payload generation.

## Quick Installation

Run the automated setup script to install all required tools:

```bash
chmod +x setup.sh
sudo ./setup.sh
```

The setup script will:
- Detect your operating system (Linux/macOS)
- Install all required dependencies
- Set up necessary wordlists
- Configure all security tools

## Prerequisites

- Python 3.x
- pip3
- Go (for some tools)
- Ruby (for evil-winrm)
- Git

Or simply run `setup.sh` to install everything automatically!

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/marmuthandsome/SecuToolbox.git
   cd SecuToolbox
   ```

2. Run the setup script:
   ```bash
   chmod +x setup.sh
   sudo ./setup.sh
   ```

3. Check tool installation status:
   ```bash
   python3 secutoolbox.py
   # Select option 98 to check tool installation status
   ```

## Usage

Run the main script to access the menu:
```bash
python secutoolbox.py
```

## Menu Options

### Linux & Windows Tools
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
- `11. Run feroxbuster`
- `12. Run rustscan` ⭐ NEW
- `13. Run jwt_tool (JWT Analysis)` ⭐ NEW
- `14. Run exiftool (File Metadata)` ⭐ NEW
- `15. Run hash-identifier` ⭐ NEW
- `16. Run msfvenom (Payload Generation)` ⭐ NEW

### Active Directory Tools
- `20. Run smbclient (guest)`
- `21. Run smbclient (user & password)`
- `22. Run smbclient (login)`
- `23. Run smbmap`
- `24. Run smbmap (user & password)`
- `25. Run evilwinrm (password)`
- `26. Run evilwinrm (hash)`
- `27. Run crackmapexec smb (password)`
- `28. Run crackmapexec smb (hash)`
- `29. Run crackmapexec evilwinrm (password)`
- `30. Run crackmapexec evilwinrm (hash)`
- `31. Run rpcclient`
- `32. Run enum4linux`
- `33. Run snmpwalk`
- `34. Run snmpwalk extend`
- `35. Run xfreerdp`
- `36. Run dnsenum`
- `37. Run kerbrute (userenum)`
- `38. Run GetNPUsers`
- `39. Run Psexec (password)`
- `40. Run Psexec (hash)`
- `41. Run GetADUsers (optional User & Password)`
- `42. Run ldapsearch`
- `43. Run secretsdump (username & password)`
- `44. Run mssqlclient (username, password & database)`
- `45. Run getUserSPNs (username & password)`
- `46. Run GetNPUsers (BruteForce Username.txt)`
- `47. Run enum4linux-ng (Next Generation)` ⭐ NEW

### Utilities
- `98. Check Tools Installation Status` ⭐ NEW
- `99. Addhosts`
- `0. Exit`

## Example Usage

### Check Tool Installation
```bash
python3 secutoolbox.py
# Select option 98 to check all tools installation status
```

### Network Scanning
**Run RustScan (Fast Port Scanner):**
1. Select option `12` from the menu.
2. Enter the target IP or domain.
3. Enter port range (e.g., `1-65535` or `80,443,8080`).

**Run Nmap full scan:**
1. Select option `3` from the menu.
2. Enter the target IP or domain.

### Security Analysis
**Analyze JWT Token:**
1. Select option `13` from the menu.
2. Enter or paste the JWT token.

**Extract File Metadata:**
1. Select option `14` from the menu.
2. Enter the file path.

**Identify Hash Type:**
1. Select option `15` from the menu.
2. Enter the hash value.

**Generate Payload with MSFVenom:**
1. Select option `16` from the menu.
2. Choose payload type (e.g., `windows/meterpreter/reverse_tcp`).
3. Enter LHOST (your IP address).
4. Enter LPORT (listening port).
5. Enter output filename.
6. Choose format (e.g., `exe`, `elf`, `php`).

### Active Directory
**Enumerate with Enum4Linux-ng:**
1. Select option `47` from the menu.
2. Enter the target IP or domain.

### Utilities
**Add hosts entry:**
1. Select option `99` from the menu.
2. Enter the IP and host.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.

## Contact

For any inquiries or issues, please open an issue on GitHub.
