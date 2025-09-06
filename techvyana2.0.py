import os
import socket
import subprocess
import requests
import random
import string
import base64

# Port Scanner
def port_scanner():
    target = input("Enter target IP (e.g., 192.168.1.1): ")
    print("Scanning ports 1-1024...")
    for port in range(1, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    print(f"Port {port} is open")
        except Exception:
            continue
    print("Port scanning completed.")

# Password Tools - Generate Random Password
def password_tools():
    length = int(input("Enter desired password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)

# File Encrypt / Decrypt using Base64 (for demonstration)
def file_encrypt_decrypt():
    choice = input("Encrypt or Decrypt? (e/d): ").lower()
    file_path = input("Enter file path: ")
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return
    with open(file_path, 'rb') as file:
        content = file.read()
    if choice == 'e':
        encoded = base64.b64encode(content)
        with open(file_path + ".enc", 'wb') as file:
            file.write(encoded)
        print(f"File encrypted as {file_path}.enc")
    elif choice == 'd':
        decoded = base64.b64decode(content)
        output_file = file_path.replace(".enc", ".dec")
        with open(output_file, 'wb') as file:
            file.write(decoded)
        print(f"File decrypted as {output_file}")
    else:
        print("Invalid choice.")

# Network Speed Test using speedtest-cli
def network_speed_test():
    print("Testing network speed...")
    try:
        from speedtest import Speedtest
        st = Speedtest()
        st.download()
        st.upload()
        res = st.results.dict()
        print(f"Download Speed: {res['download'] / 1_000_000:.2f} Mbps")
        print(f"Upload Speed: {res['upload'] / 1_000_000:.2f} Mbps")
    except ImportError:
        print("Install speedtest-cli: pip install speedtest-cli")

# Device Information
def device_info():
    print("Device Info:")
    print(f"Hostname: {socket.gethostname()}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except socket.error:
        ip = "Unable to fetch"
    print(f"IP Address: {ip}")

# Network Info - Local and Public IP
def network_info():
    print("Network Information:")
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except socket.error:
        local_ip = "Unable to fetch"
    try:
        public_ip = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        public_ip = "Unable to fetch"
    print(f"Local IP: {local_ip}")
    print(f"Public IP: {public_ip}")

# Wi-Fi Info (for Termux or Linux systems)
def wifi_info():
    print("Wi-Fi Information:")
    try:
        result = subprocess.run(["termux-wifi-connectioninfo"], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("termux-wifi-connectioninfo not found. Trying 'iwconfig'")
        try:
            result = subprocess.run(["iwconfig"], capture_output=True, text=True)
            print(result.stdout)
        except FileNotFoundError:
            print("iwconfig not found. Wi-Fi info cannot be retrieved.")

# Main Menu
def main():
    while True:
        print("\n======= Security & Network Tools =======")
        print("[1] Port Scanner")
        print("[2] Password Tools")
        print("[3] File Encrypt / Decrypt")
        print("[4] Network Speed Test")
        print("[5] Device Info")
        print("[6] Network Info (Local/Public IP)")
        print("[7] Wi-Fi Info (Termux/Linux)")
        print("[0] Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            port_scanner()
        elif choice == '2':
            password_tools()
        elif choice == '3':
            file_encrypt_decrypt()
        elif choice == '4':
            network_speed_test()
        elif choice == '5':
            device_info()
        elif choice == '6':
            network_info()
        elif choice == '7':
            wifi_info()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
