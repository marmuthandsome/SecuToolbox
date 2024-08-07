# menu.py
from commands import run_GetADUsers, run_GetNPUsers, run_GetNPUsers_file, run_GetUserSPNs, run_addhosts, run_crackmapexec_evil_hash, run_crackmapexec_evil_password, run_crackmapexec_smb_hash, run_crackmapexec_smb_password, run_dirsearch, run_dnsenum, run_enum4linux, run_evilwinrm_hash, run_evilwinrm_password, run_feroxbuster, run_ffuf, run_ffuf_subdomain, run_gobuster_dir, run_gobuster_dns, run_gobuster_vhost, run_kerbrute, run_ldap, run_mssqlclient, run_nmap_full, run_nmap_udp, run_psexec_hash, run_psexec_password, run_rpcclient, run_secretsdump, run_smbclient, run_smbclient_login, run_smbclient_user, run_smbmap, run_smbmap_user, run_snmpwalk_all, run_snmpwalk_extend, run_wfuzz, run_whatweb, run_xfreerdp
from constants import BOLD, GREEN, LCYAN, LPURPLE, RESET, RED
import commands

def print_menu():
    print(f"{LCYAN}{BOLD}"
          f"                                                                                \n"
          f" ,---.                       ,--------.             ,--.,--.                    \n"
          f"'   .-'  ,---.  ,---.,--.,--.'--.  .--',---.  ,---. |  ||  |-.  ,---.,--.  ,--. \n"
          f"`.  `-. | .-. :| .--'|  ||  |   |  |  | .-. || .-. ||  || .-. '| .-. |\  `'  /  \n"
          f".-'    |\   --.\ `--.'  ''  '   |  |  ' '-' '' '-' '|  || `-' |' '-' '/  /.  \  \n"
          f"`-----'  `----' `---' `----'    `--'   `---'  `---' `--' `---'  `---''--'  '--' \n"
          f"                                                                                \n"
          f"{RESET}")

def display_menu():
    print(f"{BOLD}{GREEN}\nTools :{RESET}")
    print(f"{LCYAN}\nLinux & Windows{RESET}")
    print("1. Run ffuf (subdomain)")
    print("2. Run ffuf (directory)")
    print("3. Run nmap (full)")
    print("4. Run nmap (udp)")
    print("5. Run whatweb")
    print("6. Run wfuzz (subdomain)")
    print("7. Run gobuster (directory)")
    print("8. Run gobuster (dns)")
    print("9. Run gobuster (vhost)")
    print("10. Run dirsearch")
    print("11. Run feroxbuster")
    print(f"{LPURPLE}\nActive Directory{RESET}")
    print("20. Run smbclient (guest)")
    print("21. Run smbclient (user & password)")
    print("22. Run smbclient (login)")
    print("23. Run smbmap")
    print("24. Run smbmap (user & password)")
    print("25. Run evilwinrm (password)")
    print("26. Run evilwinrm (hash)")
    print("27. Run crackmapexec smb (password)")
    print("28. Run crackmapexec smb (hash)")
    print("29. Run crackmapexec evilwinrm (password)")
    print("30. Run crackmapexec evilwinrm (hash)")
    print("31. Run rpcclient")
    print("32. Run enum4linux")
    print("33. Run snmpwalk")
    print("34. Run snmpwalk extend")
    print("35. Run xfreerdp")
    print("36. Run dnsenum")
    print("37. Run kerbrute (userenum)")
    print("38. Run GetNPUsers")
    print("39. Run Psexec (password)")
    print("40. Run Psexec (hash)")
    print("41. Run GetADUsers (optional User & Password)")
    print("42. Run ldapsearch")
    print("43. Run secretsdump (username & password)")
    print("44. Run mssqlclient (username, password & database)")
    print("45. Run getUserSPNs (username & password)")
    print("46. Run GetNPUsers (BruteForce Username.txt)")
    print("99. Addhosts")
    print("0. Exit")

def get_user_choice():
    return input(f"{BOLD}{GREEN}\nEnter your choice: {RESET}")

def handle_choice(choice):

    # Linux & Windows

    if choice == '1':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        word = input("Enter word size to filter: ")
        command = f"ffuf -u '{url}' -H 'Host: FUZZ.{url}' -w {wordlist} -c -t 100 -fw {word}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_ffuf_subdomain(url, wordlist, word)
    elif choice == '2':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        command = f"ffuf -u {url}/FUZZ -w {wordlist} -t 100"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_ffuf(url, wordlist)
    elif choice == '3':
        target = input("Enter the target: ")
        command = f"sudo nmap -sC -sV -O --open -p- {target} -Pn"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_nmap_full(target)
    elif choice == '4':
        target = input("Enter the target: ")
        command = f"sudo nmap -Pn -sU -sV -sC --top-ports=20 {target}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_nmap_udp(target)
    elif choice == '5':
        url = input("Enter the URL: ")
        command = f"whatweb {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_whatweb(url)
    elif choice == '6':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        word = input("Enter size word to filter: ")
        command = f"wfuzz -c -t 100 -w {wordlist} -u http://{url} -H 'Host: FUZZ.{url}' --hw {word}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_wfuzz(url, wordlist, word)
    elif choice == '7':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        command = f"gobuster dir -u {url} -w {wordlist} -t 100"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_gobuster_dir(url, wordlist)
    elif choice == '8':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        need = input("Need --wildcard: ")
        command = f"gobuster dns -d {url} -t 50 -w {wordlist} {need}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_gobuster_dns(url, wordlist, need)
    elif choice == '9':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        command = f"gobuster vhost -u {url} -t 50 -w {wordlist} --append-domain"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_gobuster_vhost(url, wordlist)
    elif choice == '10':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        command = f"dirsearch -u {url} -e txt,bak,php,html,js,asp,aspx -x 403,404 -w {wordlist}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_dirsearch(url, wordlist)
    elif choice == '11':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        command = f"feroxbuster -u {url} -w {wordlist} -k -x txt,bak,php,html,js,asp,aspx -C 503"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_feroxbuster(url, wordlist)


    # Active Directory

    elif choice == '20':
        url = input("Enter the URL: ")
        command = f"smbclient -L \\\\{url} -N"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_smbclient(url)
    elif choice == '21':
        url = input("Enter the URL: ")
        user = input("Enter User: ")
        password = input("Enter Password: ")
        command = f"smbclient -U {user}%{password} -L //{url}/"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_smbclient_user(url, user, password)
    elif choice == '22':
        url = input("Enter the URL: ")
        user = input("Enter User: ")
        share = input("Enter SMB Share: ")
        command = f"smbclient -U {user} //{url}/{share}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_smbclient_login(url, user, share)
    elif choice == '23':
        url = input("Enter the URL: ")
        command = f"smbmap -u '' -p '' -H {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_smbmap(url)
    elif choice == '24':
        url = input("Enter the URL: ")
        user = input("Enter User: ")
        password = input("Enter Password: ")
        command = f"smbmap -u {user} -p {password} -H {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_smbmap_user(url, user, password)
    elif choice == '25':
        url = input("Enter the URL: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        command = f"evil-winrm -i {url} -u {username} -p '{password}'"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_evilwinrm_password(url, username, password)
    elif choice == '26':
        url = input("Enter the URL: ")
        username = input("Enter username: ")
        hash = input("Enter hash: ")
        command = f"evil-winrm -i {url} -u {username} -H {hash}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_evilwinrm_hash(url, username, hash)
    elif choice == '27':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        password = input("Enter password/password.txt: ")
        command = f"sudo crackmapexec smb {url} -u {username} -p '{password}'"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_crackmapexec_smb_password(url, username, password)
    elif choice == '28':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        hash = input("Enter hash: ")
        command = f"sudo crackmapexec smb {url} -u {username} -H {hash}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_crackmapexec_smb_hash(url, username, hash)
    elif choice == '29':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        password = input("Enter password/password.txt: ")
        command = f"sudo crackmapexec winrm {url} -u {username} -p '{password}' -x whoami --local-auth"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_crackmapexec_evil_password(url, username, password)
    elif choice == '30':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        hash = input("Enter hash: ")
        command = f"sudo crackmapexec winrm {url} -u {username} -H {hash} -x whoami --local-auth"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_crackmapexec_evil_hash(url, username, hash)
    elif choice == '31':
        url = input("Enter the URL: ")
        command = f"rpcclient -U '' -N {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_rpcclient(url)
    elif choice == '32':
        url = input("Enter the URL: ")
        command = f"enum4linux -a {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_enum4linux(url)
    elif choice == '33':
        url = input("Enter the URL: ")
        command = f"snmpwalk -c public -v1 -t 10 {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_snmpwalk_all(url)
    elif choice == '34':
        url = input("Enter the URL: ")
        command = f"snmpwalk -v1 -c public {url} NET-SNMP-EXTEND-MIB::nsExtendObjects"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_snmpwalk_extend(url)
    elif choice == '35':
        url = input("Enter the URL: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        command = f"xfreerdp /u:{username} /p:{password} /v:{url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_xfreerdp(url, username, password)
    elif choice == '36':
        url = input("Enter the URL: ")
        domain = input("Enter domain: ")
        command = f"dnsenum --dnsserver {url} -f /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt {domain} dnsenum VERSION:1.2.6"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_dnsenum(url, domain)
    elif choice == '37':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        user = input("Enter username/username.txt: ")
        command = f"./kerbrute userenum --dc {url} -d {domain} {user}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_kerbrute(url, domain, user)
    elif choice == '38':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        command = f"impacket-GetNPUsers -dc-ip {url} -request '{domain}/'"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_GetNPUsers(url, domain)
    elif choice == '39':
        url = input("Enter the IP: ")
        user = input("Enter username: ")
        password = input("Enter password: ")
        command = f"impacket-psexec {user}:{password}@{url} cmd.exe"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_psexec_password(url, user, password)
    elif choice == '40':
        url = input("Enter the IP: ")
        user = input("Enter username: ")
        hash = input("Enter hash: ")
        command = f"impacket-psexec -hashes {hash} {user}@{url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_psexec_hash(url, user, hash)
    elif choice == '41':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        user = input("Enter user: ")
        command = f"GetADUsers.py -all '{domain}/{user}' -dc-ip {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_GetADUsers(url, domain, user)
    elif choice == '42':
        url = input("Enter the IP: ")
        dc_1 = input("Enter DC_1: ")
        dc_2 = input("Enter DC_2: ")
        command = f"ldapsearch -x -H ldap://{url} -b 'DC={dc_1},DC={dc_2}'"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_ldap(url, dc_1, dc_2)
    elif choice == '43':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        command = f"secretsdump.py {domain}/{username}:'{password}'@{url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_secretsdump(url, domain, username, password)
    elif choice == '44':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        db = input("Enter database/volume: ")
        command = f"mssqlclient.py -db {db} {domain}/{username}:'{password}'@{url} -windows-auth"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_mssqlclient(url, domain, username, password, db)
    elif choice == '45':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        username = input("Enter username: ")
        command = f"GetUserSPNs.py {domain}/{user} -dc-ip {url} -request"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_GetUserSPNs(url, domain, username)
    elif choice == '46':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        username = input("Enter username.txt: ")
        command = f"GetNPUsers.py '{domain}/' -usersfile {username} -dc-ip {url}"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_GetNPUsers_file(url, domain, username)
    elif choice == '99':
        ip = input("Enter the IP: ")
        host = input("Enter host: ")
        command = f"sudo -- sh -c -e \"echo '{ip} {host}' >> /etc/hosts\";"
        print(f"{LPURPLE}Executing:{RESET} {command}")
        run_addhosts(host, ip)
    elif choice == '0':
        return False
    else:
        print(f"{RED}Invalid choice. Please try again.{RESET}")
    return True