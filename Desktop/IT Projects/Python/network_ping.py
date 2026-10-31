import subprocess

# Your home network subnet
subnet = "192.168.0"

print(f"🔍 Scanning subnet {subnet}.1 to {subnet}.254...\n")

active_devices = []

for host in range(1, 255):
    ip = f"{subnet}.{host}"
    # Send 1 quick ping with a 1-second timeout (-W 1)
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    if result.returncode == 0:
        print(f"✅ [ONLINE]  {ip}")
        active_devices.append(ip)

print(f"\n🎉 Scan complete! Found {len(active_devices)} active device(s) on your Wi-Fi.")