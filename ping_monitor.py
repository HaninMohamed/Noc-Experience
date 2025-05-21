import os

hosts = ["8.8.8.8", "1.1.1.1"]

for host in hosts:
    response = os.system(f"ping -n 1 {host}")
    if response == 0:
        print(f"{host} is up")
    else:
        print(f"{host} is down")
