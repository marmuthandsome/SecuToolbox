# commands.py
import subprocess
from constants import RESET, RED

def run_addhosts(host, ip):
    try:
        command = f"sudo -- sh -c -e \"echo '{ip} {host}' >> /etc/hosts\";"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running addhost: {e}{RESET}")

def run_ffuf_subdomain(url, wordlist, word):
    try:
        command = f"ffuf -u 'http://{url}' -H 'Host: FUZZ.{url}' -w {wordlist} -c -t 100 -fw {word}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running ffuf: {e}{RESET}")

def run_ffuf(url, wordlist):
    try:
        command = f"ffuf -u {url}/FUZZ -w {wordlist} -t 100"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running ffuf: {e}{RESET}")

def run_nmap_full(target):
    try:
        command = f"sudo nmap -sC -sV -O --open -p- {target} -Pn"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running nmap: {e}{RESET}")

def run_nmap_udp(target):
    try:
        command = f"sudo nmap -Pn -sU -sV -sC --top-ports=20 {target}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running nmap: {e}{RESET}")

def run_whatweb(url):
    try:
        command = f"whatweb {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running whatweb: {e}{RESET}")

def run_wfuzz(url, wordlist, word):
    try:
        command = f"wfuzz -c -t 100 -w {wordlist} -u http://{url} -H 'Host: FUZZ.{url}' --hw {word}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running wfuzz: {e}{RESET}")

def run_gobuster_dir(url, wordlist):
    try:
        command = f"gobuster dir -u {url} -w {wordlist} -t 100"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running gobuster: {e}{RESET}")

def run_gobuster_dns(url, wordlist, need):
    try:
        command = f"gobuster dns -d {url} -t 50 -w {wordlist} {need}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running gobuster: {e}{RESET}")

def run_gobuster_vhost(url, wordlist):
    try:
        command = f"gobuster vhost -u {url} -t 50 -w {wordlist} --append-domain"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running gobuster: {e}{RESET}")

def run_dirsearch(url, wordlist):
    try:
        command = f"dirsearch -u {url} -e txt,bak,php,html,js,asp,aspx -x 403,404 -w {wordlist}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running dirsearch: {e}{RESET}")

def run_feroxbuster(url, wordlist):
    try:
        command = f"feroxbuster -u {url} -w {wordlist} -k -x txt,bak,php,html,js,asp,aspx -C 503"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running feroxbuster: {e}{RESET}")

def run_smbclient(url):
    try:
        command = f"smbclient -L \\\\{url} -N"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running smbclient: {e}{RESET}")

def run_smbclient_user(url, user, password):
    try:
        command = f"smbclient -U {user}%{password} -L //{url}/"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running smbclient: {e}{RESET}")

def run_smbclient_login(url, user, share):
    try:
        command = f"smbclient -U {user} //{url}/{share}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running smbclient: {e}{RESET}")

def run_smbmap(url):
    try:
        command = f"smbmap -u '' -p '' -H {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running smbmap: {e}{RESET}")

def run_smbmap_user(url, user, password):
    try:
        command = f"smbmap -u {user} -p {password} -H {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running smbmap: {e}{RESET}")

def run_evilwinrm_password(url, username, password):
    try:
        command = f"evil-winrm -i {url} -u {username} -p '{password}'"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running evilwinrm: {e}{RESET}")

def run_evilwinrm_hash(url, username, hash):
    try:
        command = f"evil-winrm -i {url} -u {username} -H {hash}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running evilwinrm: {e}{RESET}")

def run_crackmapexec_smb_password(url, username, password):
    try:
        command = f"sudo crackmapexec smb {url} -u {username} -p '{password}'"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running crackmapexec: {e}{RESET}")

def run_crackmapexec_smb_hash(url, username, hash):
    try:
        command = f"sudo crackmapexec smb {url} -u {username} -H {hash}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running crackmapexec: {e}{RESET}")

def run_crackmapexec_evil_password(url, username, password):
    try:
        command = f"sudo crackmapexec winrm {url} -u {username} -p '{password}' -x whoami --local-auth"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running crackmapexec: {e}{RESET}")

def run_crackmapexec_evil_hash(url, username, hash):
    try:
        command = f"sudo crackmapexec winrm {url} -u {username} -H {hash} -x whoami --local-auth"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running crackmapexec: {e}{RESET}")

def run_rpcclient(url):
    try:
        command = f"rpcclient -U '' -N {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running rpcclient: {e}{RESET}")

def run_enum4linux(url):
    try:
        command = f"enum4linux -a {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running enum4linux: {e}{RESET}")

def run_snmpwalk_all(url):
    try:
        command = f"snmpwalk -c public -v1 -t 10 {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running snmpwalk: {e}{RESET}")

def run_snmpwalk_extend(url):
    try:
        command = f"snmpwalk -v1 -c public {url} NET-SNMP-EXTEND-MIB::nsExtendObjects"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running snmpwalk: {e}{RESET}")

def run_xfreerdp(url, username, password):
    try:
        command = f"xfreerdp /u:{username} /p:{password} /v:{url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running xfreerdp: {e}{RESET}")

def run_dnsenum(url, domain):
    try:
        command = f"dnsenum --dnsserver {url} -f /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt {domain} dnsenum VERSION:1.2.6"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running dnsenum: {e}{RESET}")

def run_kerbrute(url, domain, user):
    try:
        command = f"./kerbrute userenum --dc {url} -d {domain} {user}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running kerbrute: {e}{RESET}")

def run_GetNPUsers(url, domain):
    try:
        command = f"impacket-GetNPUsers -dc-ip {url} -request '{domain}/'"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running GetNPUsers: {e}{RESET}")

def run_psexec_password(url, user, password):
    try:
        command = f"impacket-psexec {user}:{password}@{url} cmd.exe"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running psexec: {e}{RESET}")

def run_psexec_hash(url, user, hash):
    try:
        command = f"impacket-psexec -hashes {hash} {user}@{url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running psexec: {e}{RESET}")

def run_GetADUsers(url, domain):
    try:
        command = f"GetADUsers.py -all '{domain}/' -dc-ip {url}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running GetADUsers: {e}{RESET}")

def run_ldap(url, dc_1, dc_2):
    try:
        command = f"ldapsearch -x -H ldap://{url} -b 'DC={dc_1},DC={dc_2}'"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"{RED}Error running GetADUsers: {e}{RESET}")