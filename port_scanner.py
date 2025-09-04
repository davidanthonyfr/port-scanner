import socket

# Step 1: Ask the user for a target
target = input("Enter a host to scan (e.g., 127.0.0.1): ")

# Step 2: Define which ports to check (just 20–1024 for this demo)
print(f"\nScanning {target}...\n")
#for port in range(20, 1025):
for port in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # don’t wait forever
    result = s.connect_ex((target, port))  # 0 = success, something is open
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

print("\nScan complete.")
