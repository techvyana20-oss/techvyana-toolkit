# TechVyana Toolkit (Network & Security Tools)

This is a toolkit containing various network and security tools like port scanner, password generator, file encryption/decryption, network speed test, device info, network info, and Wi-Fi information. It is designed to run in **Termux** on Android.

---

## 📦 Installation Instructions (for Termux)

1. **Update and upgrade packages**
   ```bash
   pkg update && pkg upgrade -y
   ```

2. **Install Python, Git and other required packages**
   ```bash
   pkg install python git -y
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/techvyana20-oss/techvyana-toolkit.git
   cd techvyana-toolkit
   ```

4. **Install Python dependencies**
   ```bash
   pip install cryptography psutil speedtest-cli requests
   ```

5. **Install additional tools**
   ```bash
   pkg install nmap termux-api -y
   ```

6. **Setup storage permissions**
   ```bash
   termux-setup-storage
   ```

7. **Run the script**
   ```bash
   python techvyana2.0.py
   ```

---

## 📂 Features

- ✅ Port Scanner (1–1024 ports)
- ✅ Password Generator
- ✅ File Encrypt / Decrypt (using Base64 or advanced algorithms)
- ✅ Network Speed Test
- ✅ Device Info (hostname, IP)
- ✅ Network Info (Local and Public IP)
- ✅ Wi-Fi Info (using Termux API or Linux commands)

---

## ⚙️ Notes

- Make sure you allow storage permissions when running `termux-setup-storage`.
- The script requires active internet access for some features like public IP and speed test.
- Wi-Fi info requires either `termux-api` or `iwconfig` (Linux environment).
- For encryption, additional libraries like `cryptography` can be used for enhanced security.

---

## 📢 Disclaimer

This toolkit is intended for educational purposes and ethical testing on networks you own or have permission to test. Unauthorized scanning or hacking is illegal.

---

## 🚀 Enjoy using TechVyana Toolkit!
