from colorama import init, Fore
from Attacks import ping_test, dns_lookup, port_scan, traceroute, whois_lookup, \
    check_open_port, reverse_dns_lookup, local_network_scan, port_forwarding_check, ddos_ip
init(autoreset=True)
def main():
    while True:
        print("")
        print(Fore.RED + """
        ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
        ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
        ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
        ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
        ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
        ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
        """)

        print("\n\n\n")
        print(Fore.RED + "Choose your option")
        print(Fore.YELLOW + "1. Ping Test")
        print(Fore.YELLOW + "2. DNS Lookup")
        print(Fore.YELLOW + "3. Port Scan")
        print(Fore.YELLOW + "4. Traceroute")
        print(Fore.YELLOW + "5. WHOIS Lookup")
        print(Fore.YELLOW + "6. Check Open Port")
        print(Fore.YELLOW + "7. Reverse DNS Lookup")
        print(Fore.YELLOW + "8. Local Network Scan")
        print(Fore.YELLOW + "9. Port Forwarding Check")
        print(Fore.YELLOW + "10. DoSS IP Address")
        print(Fore.YELLOW + "11. Exit")
        print()

        choice = input(Fore.CYAN + "Choose an option (1-11): ")

        if choice == "1":
            ping_test()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            port_scan()
        elif choice == "4":
            traceroute()
        elif choice == "5":
            whois_lookup()
        elif choice == "6":
            check_open_port()
        elif choice == "7":
            reverse_dns_lookup()
        elif choice == "8":
            local_network_scan()
        elif choice == "9":
            port_forwarding_check()
        elif choice == "10":
            ddos_ip()
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
            input("Press Enter to continue...")
            continue

if __name__ == "__main__":
    main()
