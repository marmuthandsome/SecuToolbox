# Changelog

## [2.0.0] - 2026-02-23

### Added - New Tools

#### Network Scanning
- **RustScan**: Fast port scanner with nmap integration
  - Menu option: `12. Run rustscan`
  - Supports custom port ranges
  - Automatically integrates with nmap for detailed scanning

#### Security Analysis Tools
- **JWT Tool**: JSON Web Token analysis and exploitation
  - Menu option: `13. Run jwt_tool (JWT Analysis)`
  - Analyze, decode, and test JWT tokens
  
- **ExifTool**: File metadata extraction and analysis
  - Menu option: `14. Run exiftool (File Metadata)`
  - Extract metadata from images and files
  
- **Hash Identifier**: Identify hash types
  - Menu option: `15. Run hash-identifier`
  - Automatically identify hash algorithms
  
- **MSFVenom**: Metasploit payload generation
  - Menu option: `16. Run msfvenom (Payload Generation)`
  - Interactive payload creation
  - Supports multiple payload types and formats
  - Common formats: exe, elf, php, raw, war, aspx

#### Active Directory Tools
- **Enum4Linux-ng**: Next generation Linux/Windows enumeration
  - Menu option: `47. Run enum4linux-ng (Next Generation)`
  - Enhanced enumeration capabilities
  - More efficient than classic enum4linux

### Added - Utilities

#### Tool Installation Checker
- **Check Tools Installation Status**
  - Menu option: `98. Check Tools Installation Status`
  - Automatically checks all required tools
  - Shows installation status with ✓/✗ indicators
  - Displays missing tools count
  - Prompts to run setup.sh if tools are missing

#### Automated Setup Script
- **setup.sh**: Comprehensive installation script
  - Auto-detects operating system (Linux/macOS/Windows)
  - Supports multiple package managers (apt, brew, yum, pacman)
  - Installs all required tools automatically
  - Features:
    - Colored output for better readability
    - Error handling and reporting
    - Installs Python pip packages
    - Installs Go packages
    - Downloads and configures tools from GitHub
    - Sets up wordlists and SecLists
    - Provides installation summary
  - Tools installed:
    - Network: nmap, rustscan
    - Web fuzzing: ffuf, gobuster, feroxbuster, dirsearch, wfuzz, whatweb
    - Active Directory: impacket suite, enum4linux, enum4linux-ng, crackmapexec, evil-winrm, smbclient, smbmap, rpcclient, snmpwalk, xfreerdp, dnsenum, kerbrute, ldapsearch
    - Security Analysis: jwt_tool, exiftool, hash-identifier, msfvenom
    - Dependencies: python3, pip3, golang, git, ruby

### Changed
- Updated README.md with comprehensive documentation
  - Added quick installation guide
  - Updated feature list with categorization
  - Added example usage for new tools
  - Marked new features with ⭐ NEW indicator
  - Added detailed menu options list

### Fixed
- Fixed syntax warnings in ASCII art (menu.py)
  - Properly escaped backslashes in banner
  - Eliminated Python SyntaxWarning messages

### Enhanced
- Added shutil import for tool checking functionality
- Added color constants for tool checker (GREEN, BOLD)
- Improved error handling across all new functions
- Added comprehensive function documentation

## Tool Count
- **Before**: ~30 tools
- **After**: ~36 tools
- **New additions**: 6 tools + automated setup + tool checker

## Installation Methods
1. **Automated** (Recommended): Run `./setup.sh`
2. **Manual**: Install individual tools as needed
3. **Verification**: Use menu option 98 to check status

## Compatibility
- Linux (Debian/Ubuntu, RedHat/CentOS, Arch)
- macOS (via Homebrew)
- Kali Linux (native support for most tools)

## Notes
- Some tools require sudo privileges for installation
- Go tools will be installed in `~/go/bin` (add to PATH)
- Ruby required for evil-winrm
- Full installation may take 15-30 minutes depending on connection speed

