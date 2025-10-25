# device_list = ["G0/0", "G0/1", "G0/2", "loopback0"]
# for device in device_list:
#     if device == "loopback0":
#         continue
#     print (device)

device_list = ["G0/0", "G0/1", "G0/2", "loopback0"]
for device in device_list:
    if device.startswith("G"):    
        continue
    print (device)
