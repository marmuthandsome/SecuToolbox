# menu.py
from commands import run_GetADUsers, run_GetNPUsers, run_addhosts, run_crackmapexec_evil_hash, run_crackmapexec_evil_password, run_crackmapexec_smb_hash, run_crackmapexec_smb_password, run_dirsearch, run_dnsenum, run_enum4linux, run_evilwinrm_hash, run_evilwinrm_password, run_feroxbuster, run_ffuf, run_ffuf_subdomain, run_gobuster_dir, run_gobuster_dns, run_gobuster_vhost, run_kerbrute, run_nmap_full, run_nmap_udp, run_psexec_hash, run_psexec_password, run_rpcclient, run_smbclient, run_smbclient_login, run_smbclient_user, run_smbmap, run_smbmap_user, run_snmpwalk_all, run_snmpwalk_extend, run_wfuzz, run_whatweb, run_xfreerdp
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
    print("41. Run GetADUsers")
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
        run_ffuf_subdomain(url, wordlist, word)
    elif choice == '2':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        run_ffuf(url, wordlist)
    elif choice == '3':
        target = input("Enter the target: ")
        run_nmap_full(target)
    elif choice == '4':
        target = input("Enter the target: ")
        run_nmap_udp(target)
    elif choice == '5':
        url = input("Enter the URL: ")
        run_whatweb(url)
    elif choice == '6':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        word = input("Enter size word to filter: ")
        run_wfuzz(url, wordlist, word)
    elif choice == '7':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        run_gobuster_dir(url, wordlist)
    elif choice == '8':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        need = input("Need --wildcard: ")
        run_gobuster_dns(url, wordlist, need)
    elif choice == '9':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        run_gobuster_vhost(url, wordlist)
    elif choice == '10':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        run_dirsearch(url, wordlist)
    elif choice == '11':
        url = input("Enter the URL: ")
        wordlist = input("Enter the path to the wordlist: ")
        run_feroxbuster(url, wordlist)



    # Active Directory

    elif choice == '20':
        url = input("Enter the URL: ")
        run_smbclient(url)
    elif choice == '21':
        url = input("Enter the URL: ")
        user = input("Enter User: ")
        password = input("Enter Password: ")
        run_smbclient_user(url, user, password)
    elif choice == '22':
        url = input("Enter the URL: ")
        user = input("Enter User: ")
        share = input("Enter SMB Share: ")
        run_smbclient_login(url, user, share)
    elif choice == '23':
        url = input("Enter the URL: ")
        run_smbmap(url)
    elif choice == '24':
        url = input("Enter the URL: ")
        user = input("Enter User: ")
        password = input("Enter Password: ")
        run_smbmap_user(url, user, password)
    elif choice == '25':
        url = input("Enter the URL: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        run_evilwinrm_password(url, username, password)
    elif choice == '26':
        url = input("Enter the URL: ")
        username = input("Enter username: ")
        hash = input("Enter hash: ")
        run_evilwinrm_hash(url, username, hash)
    elif choice == '27':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        password = input("Enter password/password.txt: ")
        run_crackmapexec_smb_password(url, username, password)
    elif choice == '28':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        hash = input("Enter hash: ")
        run_crackmapexec_smb_hash(url, username, hash)
    elif choice == '29':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        password = input("Enter password/password.txt: ")
        run_crackmapexec_evil_password(url, username, password)
    elif choice == '30':
        url = input("Enter the URL: ")
        username = input("Enter username/username.txt: ")
        hash = input("Enter hash: ")
        run_crackmapexec_evil_hash(url, username, hash)
    elif choice == '31':
        url = input("Enter the URL: ")
        run_rpcclient(url)
    elif choice == '32':
        url = input("Enter the URL: ")
        run_enum4linux(url)
    elif choice == '33':
        url = input("Enter the URL: ")
        run_snmpwalk_all(url)
    elif choice == '34':
        url = input("Enter the URL: ")
        run_snmpwalk_extend(url)
    elif choice == '35':
        url = input("Enter the URL: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        run_xfreerdp(url, username, password)
    elif choice == '36':
        url = input("Enter the URL: ")
        domain = input("Enter domain: ")
        run_dnsenum(url, domain)
    elif choice == '37':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        user = input("Enter username/username.txt: ")
        run_kerbrute(url, domain, user)
    elif choice == '38':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        run_GetNPUsers(url, domain)
    elif choice == '39':
        url = input("Enter the IP: ")
        user = input("Enter username: ")
        password = input("Enter password: ")
        run_psexec_password(url, user, password)
    elif choice == '40':
        url = input("Enter the IP: ")
        user = input("Enter username: ")
        hash = input("Enter hash: ")
        run_psexec_hash(url, user, hash)
    elif choice == '41':
        url = input("Enter the IP: ")
        domain = input("Enter domain: ")
        run_GetADUsers(url, domain)
    elif choice == '99':
        ip = input("Enter the IP: ")
        host = input("Enter host: ")
        run_addhosts(host, ip)
    elif choice == '0':
        return False
    else:
        print(f"{RED}Invalid choice. Please try again.{RESET}")
    return True
