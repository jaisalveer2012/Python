vlans = ["vlan1", "vlan3", "vlan5", "vlan10"]
remove = vlans.pop(1)                      #poping vlan from position 1
print(remove)

vlans = ["vlan1", "vlan3", "vlan5", "vlan10"]
remove = vlans.insert(1, "vlan77")                      #insert vlan77 from position 1
print(vlans)

vlans = ["vlan1", "vlan3", "vlan5", "vlan10"]
remove = vlans.append("vlan99")                      #Append vlan99 in last postion
print(vlans)

vlans = ["vlan1", "vlan3", "vlan5", "vlan10"]
remove = vlans.remove("vlan10")                      #Remove vlan10
print(vlans)