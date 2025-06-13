from scapy.all import *
import sys

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        proto_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto, f"Protocol {proto}")
        
        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {proto_name}")
        
        if packet.haslayer(TCP):
            print("TCP Payload (first 64 bytes):")
            print(packet[TCP].payload[:64])
        elif packet.haslayer(UDP):
            print("UDP Payload (first 64 bytes):")
            print(packet[UDP].payload[:64])
        elif packet.haslayer(ICMP):
            print("ICMP Payload (first 64 bytes):")
            print(packet[ICMP].payload[:64])
        print("-" * 60)

def main():
    if len(sys.argv) < 2:
        print("Usage: python packet_sniffer.py <interface>")
        print("Example: python packet_sniffer.py eth0")
        sys.exit(1)
    interface = sys.argv[1]
    print(f"Starting packet sniffer on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
