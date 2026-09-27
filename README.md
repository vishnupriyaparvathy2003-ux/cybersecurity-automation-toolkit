# 🛡️ Automated Cybersecurity Log Parser & Anomaly Detector

A lightweight, automated network log parsing utility designed to scan system and network traffic logs for potential security anomalies, unencrypted communication protocols, cleartext data leaks, and critical transport-level disruption patterns.

## 🚀 Features

- **Protocol Audit:** Scans for unencrypted transmission vectors (e.g., plain HTTP flags).
- **Data Leakage Detection:** Identifies indicators showing potential cleartext exposure or asset leaks (e.g., mDNS plain text anomalies).
- **Transport Layer Analysis:** Flags aggressive connection resets (`[RST]` flags) or suspicious `TCP` network degradation markers.
- **Automated Incident Reporting:** Generates a structured Markdown incident alert report (`alerts_report.md`) containing all isolated high-priority threats upon script termination.

## 📁 Repository Structure

```text
├── network_log_parser.py   # Main Python utility engine 
└── README.md               # Project documentation
```

## 🛠️ Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your workstation.

```bash
python --version
```

### Installation
1. Clone this repository to your local directory:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the toolkit project folder:
   ```bash
   cd cybersecurity-automation-toolkit
   ```

### Execution
Run the automated parser directly via terminal or command prompt:
```bash
python network_log_parser.py
```

## 📊 Sample Analysis Output

```text
----------------------------------------------------------------------
🛡️  AUTOMATED CYBERSECURITY LOG PARSER & ANOMALY DETECTOR 🛡️
----------------------------------------------------------------------
[⚠️ INSECURE TRANSPORT DETECTED]: 2026-09-18 10:14:22 INFO 192.168.0.232 -> 34.223.124.45 HTTP GET /index.html
[🚨 INFORMATION DISCLOSURE LEAK]: 2026-09-18 10:15:01 WARN 192.168.0.7 -> 224.0.0.251 mDNS Query - Cleartext String Asset Leakage
[💥 TRANSPORT LEVEL ANOMALY CRITICAL]: 2026-09-18 10:16:14 ERROR 192.168.0.232 -> 10.0.0.5 TCP [RST] Connection Reset Flag Detected

[📝 INFO] Report successfully generated and saved to 'alerts_report.md'
```
