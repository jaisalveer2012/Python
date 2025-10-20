device_list = ["R1", "R2", "R3"]
interface_list = ["interface g0/0", "interface g0/1", "interface g0/2"]
for device in device_list:
    for interface in interface_list:
        print (f"{interface}\n description connected to {device}")
    