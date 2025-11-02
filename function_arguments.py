# def device_login(username, hostname, platform):   # positional arguments
#     print(f"ssh {username}@{hostname}")
#     if platform == "cisco":
#         print("enable\nconfigure terminal\n")

# device_login("john", "192.168.1.1", "cisco")


def device_login(username, hostname, platform="cisco"):   
    print(f"ssh {username}@{hostname}")
    if platform == "cisco":
        print("enable\nconfigure terminal\n")
    elif platform == "junos":
        print("cli\nedit\n")

# device_login("john", "192.168.1.1", "junos") # Default arguments

device_login(hostname="192.168.1.1", platform="junos", username="john") #keyword arguments

