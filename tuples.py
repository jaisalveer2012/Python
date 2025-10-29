vlan_tuple = ("vlan5", "vlan10", "vlan7", "vlan33")
print(vlan_tuple)
print(len(vlan_tuple))
print(min(vlan_tuple))      # min function in tuple string match each character till tie not breaked,
                            #thats y take vlan10 as min value because vlan is common then it compare 3 vs 5 vs 7 vs 1
                            # as 1 is lowest so taken vlan10
