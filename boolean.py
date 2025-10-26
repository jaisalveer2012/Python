my_protocol_list = ["ISIS", "EIGRP", "OSPF", "BGP"]
if "BGP" not in my_protocol_list:
    print("No boader protocol")
else:
    print("Boader protocol")

my_protocol_list = ["ISIS", "EIGRP", "OSPF", "BGP"]
if "ISIS" and "OSPF" in my_protocol_list:
    print("Link state protocol")
else:
    print("No Link State protocol")