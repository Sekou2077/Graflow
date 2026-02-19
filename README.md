# Graflow 🌐
A lightweight, easy-to-use network monitoring script that displays host-specific network metrics, socket connections, network interfaces, and live packet capture, all from your terminal.

> *Why did the TCP packet break up with UDP? Because UDP never acknowledged its feelings.*

---

## Motivation

I built Graflow primarily for myself because I wanted a simple way to observe how several networking constructs interact with one another in real time, without drowning in noise.

---

## Usage

Because networking at its core is just a ballet of protocols dancing in more or less glorious harmony, its data can be very noisy if not filtered correctly. I had to make deliberate choices about what to surface, which socket connections are most worth showing, which address families matter, which states are meaningful.

So the information displayed at any time is far from exhaustive, but intentionally limited to what I deemed interesting for each situation. Computer Science is all about trade-offs anyway.

I've also consistently tried to make outputs as human-friendly as possible, translating things like `AF_INET` to `IPv4` and `SOCK_DGRAM` to `UDP` so you spend less time context-switching and more time actually understanding your network.

**The four things Graflow can do:**
- Display system-wide network I/O statistics
- Show active socket connections (TCP/UDP, IPv4/IPv6)
- List network interface status and specs
- Live capture packets involving any IP address of your choice

---

## Installation

```bash
git clone https://github.com/Sekou2077/Graflow
cd Graflow
```

Create and activate a virtual environment:

```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your target IP:

```bash
echo "IP_ADDRESS=127.0.0.1" > .env
```

Then run:

```bash
python Graflow.py
```

> **Note:** Live packet capture (option 4) requires [Npcap](https://npcap.com/) on Windows and administrative privileges on all platforms. Use `sudo python Graflow.py` on Mac/Linux, or run as Administrator on Windows.

---

## Dependencies

- `psutil` — system and network info
- `scapy` — packet sniffing
- `rich` — terminal formatting
- `python-dotenv` — environment variable management
