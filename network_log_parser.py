import re

# Simulated network log file content representing a traffic alert scenario
log_data = [
    "2026-09-18 10:14:22 INFO  192.168.0.232 -> 34.223.124.45 HTTP GET /index.html",
    "2026-09-18 10:15:01 WARN  192.168.0.7 -> 224.0.0.251 mDNS Query - Cleartext String Asset Leakage",
    "2026-09-18 10:16:14 ERROR 192.168.0.232 -> 10.0.0.5 TCP [RST] Connection Reset Flag Detected",
    "2026-09-18 10:17:05 INFO  192.168.0.232 -> 142.250.190.46 HTTPS POST /secure/login"
]

def audit_network_logs(logs):
    print("=" * 70)
    print("🛡️  AUTOMATED CYBERSECURITY LOG PARSER & ANOMALY DETECTOR 🛡️")
    print("=" * 70)
    
    for entry in logs:
        # Check for unencrypted HTTP transport protocols
        if "HTTP " in entry:
            print(f"[⚠️ INSECURE TRANSPORT DETECTED]: {entry}")
            
        # Check for cleartext asset leakage indicators
        elif "mDNS" in entry or "Cleartext" in entry:
            print(f"[🚨 INFORMATION DISCLOSURE LEAK]: {entry}")
            
        # Check for stateful connection resets / transport degradation anomalies
        elif "[RST]" in entry or "TCP" in entry:
            print(f"[🔥 TRANSPORT LEVEL ANOMALY CRITICAL]: {entry}")

if __name__ == "__main__":
    audit_network_logs(log_data)
