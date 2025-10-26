ip_address = ["192.168.1.1", "192.168.2.1", "192.168.3.3", "4.2.2.2", "8.8.8.8", "1.1.1.1"]
public_address = []

for public_ip in ip_address:
    if "192.168"  not in public_ip:
        public_address.append(public_ip)
print(f"Public ip {public_address}")
