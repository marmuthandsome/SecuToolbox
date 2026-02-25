#!/bin/bash

# SecuToolbox - Setup Script
# This script installs all required tools for SecuToolbox

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[*]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}$1${NC}"
}

# Check if running as root (for some operations)
check_root() {
    if [ "$EUID" -eq 0 ]; then 
        print_warning "Running as root"
    fi
}

# Detect OS and package manager
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
            PKG_MANAGER="apt"
        elif [ -f /etc/redhat-release ]; then
            OS="redhat"
            PKG_MANAGER="yum"
        elif [ -f /etc/arch-release ]; then
            OS="arch"
            PKG_MANAGER="pacman"
        else
            OS="linux"
            PKG_MANAGER="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PKG_MANAGER="brew"
    else
        OS="unknown"
        PKG_MANAGER="unknown"
    fi
}

# Check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install package based on OS
install_package() {
    local package=$1
    local alt_name=$2
    
    if [ -n "$alt_name" ]; then
        package=$alt_name
    fi
    
    print_info "Installing $package..."
    
    case $PKG_MANAGER in
        apt)
            sudo apt-get install -y "$package" 2>/dev/null || print_error "Failed to install $package"
            ;;
        brew)
            brew install "$package" 2>/dev/null || print_error "Failed to install $package"
            ;;
        yum)
            sudo yum install -y "$package" 2>/dev/null || print_error "Failed to install $package"
            ;;
        pacman)
            sudo pacman -S --noconfirm "$package" 2>/dev/null || print_error "Failed to install $package"
            ;;
        *)
            print_error "Unknown package manager. Please install $package manually."
            ;;
    esac
}

# Install pip package
install_pip_package() {
    local package=$1
    print_info "Installing Python package: $package..."
    
    if command_exists pip3; then
        pip3 install "$package" --break-system-packages 2>/dev/null || pip3 install "$package" 2>/dev/null || print_error "Failed to install $package"
    elif command_exists pip; then
        pip install "$package" --break-system-packages 2>/dev/null || pip install "$package" 2>/dev/null || print_error "Failed to install $package"
    else
        print_error "pip not found. Please install Python pip first."
    fi
}

# Install Go package
install_go_package() {
    local package=$1
    print_info "Installing Go package: $package..."
    
    if command_exists go; then
        go install "$package" || print_error "Failed to install $package"
    else
        print_error "Go not found. Please install Go first."
    fi
}

# Main installation function
main() {
    print_header "╔══════════════════════════════════════════════════════════╗"
    print_header "║          SecuToolbox - Installation Script              ║"
    print_header "╚══════════════════════════════════════════════════════════╝"
    echo ""
    
    # Detect OS
    detect_os
    print_info "Detected OS: $OS"
    print_info "Package Manager: $PKG_MANAGER"
    echo ""
    
    # Update package lists
    print_header "Updating package lists..."
    case $PKG_MANAGER in
        apt)
            sudo apt-get update
            ;;
        brew)
            brew update
            ;;
        yum)
            sudo yum update
            ;;
    esac
    echo ""
    
    # Install core dependencies
    print_header "Installing core dependencies..."
    
    if [ "$PKG_MANAGER" == "apt" ]; then
        install_package "python3-pip"
        install_package "golang-go" "golang"
        install_package "git"
        install_package "wget"
        install_package "curl"
    elif [ "$PKG_MANAGER" == "brew" ]; then
        install_package "python3"
        install_package "go"
        install_package "git"
        install_package "wget"
    fi
    echo ""
    
    # Install scanning tools
    print_header "Installing Network Scanning Tools..."
    
    # Nmap
    if ! command_exists nmap; then
        install_package "nmap"
    else
        print_success "nmap already installed"
    fi
    
    # RustScan
    if ! command_exists rustscan; then
        print_info "Installing RustScan..."
        if [ "$OS" == "debian" ]; then
            wget https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb -O /tmp/rustscan.deb
            sudo dpkg -i /tmp/rustscan.deb || sudo apt-get install -f -y
            rm /tmp/rustscan.deb
        elif [ "$OS" == "macos" ]; then
            brew install rustscan
        else
            print_warning "RustScan: Please install manually from https://github.com/RustScan/RustScan"
        fi
    else
        print_success "rustscan already installed"
    fi
    echo ""
    
    # Install web fuzzing tools
    print_header "Installing Web Fuzzing Tools..."
    
    # ffuf
    if ! command_exists ffuf; then
        if command_exists go; then
            go install github.com/ffuf/ffuf@latest
        else
            install_package "ffuf"
        fi
    else
        print_success "ffuf already installed"
    fi
    
    # gobuster
    if ! command_exists gobuster; then
        if command_exists go; then
            go install github.com/OJ/gobuster/v3@latest
        else
            install_package "gobuster"
        fi
    else
        print_success "gobuster already installed"
    fi
    
    # feroxbuster
    if ! command_exists feroxbuster; then
        print_info "Installing feroxbuster..."
        if [ "$OS" == "debian" ]; then
            wget https://github.com/epi052/feroxbuster/releases/download/v2.10.1/feroxbuster_2.10.1_amd64.deb -O /tmp/feroxbuster.deb
            sudo dpkg -i /tmp/feroxbuster.deb || sudo apt-get install -f -y
            rm /tmp/feroxbuster.deb
        elif [ "$OS" == "macos" ]; then
            brew install feroxbuster
        else
            print_warning "feroxbuster: Please install manually"
        fi
    else
        print_success "feroxbuster already installed"
    fi
    
    # dirsearch
    if ! command_exists dirsearch; then
        install_pip_package "dirsearch"
    else
        print_success "dirsearch already installed"
    fi
    
    # wfuzz
    if ! command_exists wfuzz; then
        install_pip_package "wfuzz"
    else
        print_success "wfuzz already installed"
    fi
    
    # whatweb
    if ! command_exists whatweb; then
        install_package "whatweb"
    else
        print_success "whatweb already installed"
    fi
    echo ""
    
    # Install Active Directory tools
    print_header "Installing Active Directory Tools..."
    
    # Impacket
    if ! command_exists impacket-GetNPUsers; then
        print_info "Installing Impacket..."
        install_pip_package "impacket"
    else
        print_success "impacket already installed"
    fi
    
    # enum4linux
    if ! command_exists enum4linux; then
        install_package "enum4linux"
    else
        print_success "enum4linux already installed"
    fi
    
    # enum4linux-ng
    if ! command_exists enum4linux-ng; then
        print_info "Installing enum4linux-ng..."
        if [ "$OS" == "debian" ] || [ "$OS" == "redhat" ]; then
            git clone https://github.com/cddmp/enum4linux-ng.git /tmp/enum4linux-ng
            cd /tmp/enum4linux-ng
            pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt
            sudo cp enum4linux-ng.py /usr/local/bin/enum4linux-ng
            sudo chmod +x /usr/local/bin/enum4linux-ng
            cd -
            rm -rf /tmp/enum4linux-ng
        elif [ "$OS" == "macos" ]; then
            brew install enum4linux-ng
        fi
    else
        print_success "enum4linux-ng already installed"
    fi
    
    # CrackMapExec
    if ! command_exists crackmapexec; then
        print_info "Installing CrackMapExec..."
        install_pip_package "crackmapexec"
    else
        print_success "crackmapexec already installed"
    fi
    
    # evil-winrm
    if ! command_exists evil-winrm; then
        print_info "Installing evil-winrm..."
        if [ "$PKG_MANAGER" == "apt" ]; then
            sudo apt-get install -y evil-winrm
        else
            sudo gem install evil-winrm 2>/dev/null || print_warning "evil-winrm: Please install Ruby and run: gem install evil-winrm"
        fi
    else
        print_success "evil-winrm already installed"
    fi
    
    # smbclient
    if ! command_exists smbclient; then
        if [ "$PKG_MANAGER" == "apt" ]; then
            install_package "smbclient"
        elif [ "$PKG_MANAGER" == "brew" ]; then
            install_package "samba"
        fi
    else
        print_success "smbclient already installed"
    fi
    
    # smbmap
    if ! command_exists smbmap; then
        install_pip_package "smbmap"
    else
        print_success "smbmap already installed"
    fi
    
    # rpcclient (part of samba)
    if ! command_exists rpcclient; then
        if [ "$PKG_MANAGER" == "apt" ]; then
            install_package "samba-common-bin"
        elif [ "$PKG_MANAGER" == "brew" ]; then
            install_package "samba"
        fi
    else
        print_success "rpcclient already installed"
    fi
    
    # snmpwalk
    if ! command_exists snmpwalk; then
        if [ "$PKG_MANAGER" == "apt" ]; then
            install_package "snmp"
        elif [ "$PKG_MANAGER" == "brew" ]; then
            install_package "net-snmp"
        fi
    else
        print_success "snmpwalk already installed"
    fi
    
    # xfreerdp
    if ! command_exists xfreerdp; then
        if [ "$PKG_MANAGER" == "apt" ]; then
            install_package "freerdp2-x11"
        elif [ "$PKG_MANAGER" == "brew" ]; then
            install_package "freerdp"
        fi
    else
        print_success "xfreerdp already installed"
    fi
    
    # dnsenum
    if ! command_exists dnsenum; then
        install_package "dnsenum"
    else
        print_success "dnsenum already installed"
    fi
    
    # kerbrute
    if ! command_exists kerbrute; then
        print_info "Installing kerbrute..."
        if command_exists go; then
            go install github.com/ropnop/kerbrute@latest
            sudo cp ~/go/bin/kerbrute /usr/local/bin/ 2>/dev/null || print_warning "kerbrute: Please add ~/go/bin to your PATH"
        else
            print_warning "kerbrute: Please install Go first"
        fi
    else
        print_success "kerbrute already installed"
    fi
    
    # ldapsearch
    if ! command_exists ldapsearch; then
        if [ "$PKG_MANAGER" == "apt" ]; then
            install_package "ldap-utils"
        elif [ "$PKG_MANAGER" == "brew" ]; then
            install_package "openldap"
        fi
    else
        print_success "ldapsearch already installed"
    fi
    echo ""
    
    # Install security analysis tools
    print_header "Installing Security Analysis Tools..."
    
    # JWT Tool
    if ! command_exists jwt_tool; then
        print_info "Installing jwt_tool..."
        git clone https://github.com/ticarpi/jwt_tool /tmp/jwt_tool
        cd /tmp/jwt_tool
        pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt
        sudo cp jwt_tool.py /usr/local/bin/jwt_tool
        sudo chmod +x /usr/local/bin/jwt_tool
        cd -
        rm -rf /tmp/jwt_tool
    else
        print_success "jwt_tool already installed"
    fi
    
    # ExifTool
    if ! command_exists exiftool; then
        if [ "$PKG_MANAGER" == "apt" ]; then
            install_package "libimage-exiftool-perl"
        elif [ "$PKG_MANAGER" == "brew" ]; then
            install_package "exiftool"
        fi
    else
        print_success "exiftool already installed"
    fi
    
    # Hash Identifier
    if ! command_exists hash-identifier; then
        print_info "Installing hash-identifier..."
        sudo wget https://raw.githubusercontent.com/blackploit/hash-identifier/master/hash-id.py -O /usr/local/bin/hash-identifier
        sudo chmod +x /usr/local/bin/hash-identifier
    else
        print_success "hash-identifier already installed"
    fi
    
    # Metasploit Framework (for msfvenom)
    if ! command_exists msfvenom; then
        print_info "Installing Metasploit Framework..."
        if [ "$OS" == "debian" ]; then
            curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > /tmp/msfinstall
            chmod 755 /tmp/msfinstall
            sudo /tmp/msfinstall
            rm /tmp/msfinstall
        elif [ "$OS" == "macos" ]; then
            brew install metasploit
        else
            print_warning "Metasploit: Please install manually from https://metasploit.com"
        fi
    else
        print_success "msfvenom already installed"
    fi
    echo ""
    
    # Ensure wordlists directory exists
    print_header "Setting up wordlists directory..."
    if [ ! -d "/usr/share/wordlists" ]; then
        sudo mkdir -p /usr/share/wordlists
        print_info "Created /usr/share/wordlists directory"
    fi
    
    # Install SecLists if not present
    if [ ! -d "/usr/share/seclists" ]; then
        print_info "Installing SecLists..."
        sudo git clone https://github.com/danielmiessler/SecLists.git /usr/share/seclists
    else
        print_success "SecLists already installed"
    fi
    echo ""
    
    # Final summary
    print_header "╔══════════════════════════════════════════════════════════╗"
    print_header "║              Installation Complete!                      ║"
    print_header "╚══════════════════════════════════════════════════════════╝"
    echo ""
    print_info "Please run 'python3 secutoolbox.py' to start the application"
    print_info "You can check tool installation status from the menu (option 98)"
    echo ""
    print_warning "Note: Some tools may require you to add ~/go/bin to your PATH"
    print_warning "Add this line to your ~/.bashrc or ~/.zshrc:"
    echo ""
    echo "    export PATH=\$PATH:~/go/bin"
    echo ""
    print_info "If any installation failed, please install those tools manually."
    echo ""
}

# Run main function
main
