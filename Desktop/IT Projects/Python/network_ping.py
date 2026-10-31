import os

# Store IP addresses with friendly labels
devices = {
    "HP Ubuntu (Loopback)": "127.0.0.1",
    "HP Ubuntu (LAN IP)": "192.168.0.65",
    "Virgin Router / Gateway": "192.168.0.1",
    "Steam Deck": "192.168.0.108",
    "Alienware Laptop": "192.168.0.176",
    "Gaming PC": "192.168.0.179",
    "Google (Internet)": "8.8.8.8"
}

print("\n==========================================")
print("      🔍 HOME LAB NETWORK AUDIT           ")
print("==========================================\n")

for name, ip in devices.items():
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    
    if response == 0:
        print(f"  ✅ {name:<25} ({ip}) --> ONLINE")
    else:
        print(f"  ❌ {name:<25} ({ip}) --> OFFLINE")

print("\n==========================================\n")