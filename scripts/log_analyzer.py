import sys
from pathlib import Path


def analyze_log(file_name):
    log_file = Path(file_name)

    if not log_file.exists():
        print("Error: Log file was not found.")
        return

    suspicious_words = {
        "failed login": "Failed login",
        "malware detected": "Malware detected",
        "connection blocked": "Blocked connection"
    }

    total_incidents = 0

    print("Security Log Analysis Report")
    print("--------------------------------")

    with log_file.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            for keyword, incident_type in suspicious_words.items():
                if keyword in line.lower():
                    total_incidents += 1
                    print(f"Line {line_number}: {incident_type}")
                    print(line.strip())
                    print("--------------------------------")

    print(f"Total suspicious incidents: {total_incidents}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/log_analyzer.py samples/security.log")
    else:
        analyze_log(sys.argv[1])