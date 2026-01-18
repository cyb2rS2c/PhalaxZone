# PhalaxZone (DDoS Protection System)
> A cyber defense system that detects,logs and mitigates DDoS attacks by blocking malicious traffic in real-time.It acts as a digital shield for your network, blocking malicious IPs while allowing legitimate traffic.
---

## Features

- **Real-time DDoS detection:** Monitors network interfaces for SYN floods and other suspicious traffic.
- **Automatic mitigation:** Blocks malicious IPs at the kernel level using iptables.
- **Persistent blocks:** Blocked IPs remain blocked even after system restarts until manually removed.
- **False positive management:** Easily unblock hosts mistakenly flagged.
- **Colorful, animated interface:** Command-line menu with animated ASCII banners and color-coded logs.
- **Detailed logging:** Maintains `blocked.txt`, `allowed.txt`, and `reason.txt` for auditing.

---

## Installation
### Method 1 (Manually)
Clone the repository:

```bash
git clone https://github.com/cyb2rS2c/PhalaxZone.git
cd PhalaxZone/phalaxzone
```
## Requirements
```bash
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
```
## Usage

Run the main program:
```bash
chmod +x phx.sh; sudo python3 phalaxzone.py
```
### Method 2 (Automatically)
---
## Automatic setup
```bash
curl -LO raw.githubusercontent.com/cyb2rS2c/PhalaxZone/refs/heads/main/setup.sh
chmod +x setup.sh;./setup.sh
```
---
### Example

1) Start DDoS detector: Monitors network traffic on the specified interface (default: wlan0).
2) Unblock host: Remove a host mistakenly blocked.
3) Show blocked hosts: Lists currently blocked IPs.
4) Exit: Close the program.

## Notes
```
Must run as root to apply iptables rules.
Blocks are persistent but can be manually removed.
Designed for educational and controlled environments. Use responsibly.
```
## Screenshots:
<img width="600" height="612" alt="image" src="https://github.com/user-attachments/assets/25daa62f-b02a-439a-8c5f-8a38cbdc92fc" />
<img width="600" height="213" alt="image" src="https://github.com/user-attachments/assets/9e9e53c4-42c0-466d-9ac0-f53ce2796573" />

## Author
**cyb2rS2c** - [GitHub Profile](https://github.com/cyb2rS2c)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.
