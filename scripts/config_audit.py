import json
import sys
from pathlib import Path


def check_configuration(file_name):
    config_file = Path(file_name)

    if not config_file.exists():
        print("Error: Configuration file was not found.")
        return

    try:
        with config_file.open("r", encoding="utf-8") as file:
            config = json.load(file)
    except json.JSONDecodeError:
        print("Error: The configuration file is not valid JSON.")
        return

    vulnerabilities = []

    if not config.get("firewall_enabled", False):
        vulnerabilities.append(
            "High: Firewall is disabled. Enable the firewall."
        )

    if not config.get("mfa_enabled", False):
        vulnerabilities.append(
            "High: Multifactor authentication is disabled. Enable MFA."
        )

    password_length = config.get("minimum_password_length", 0)

    if password_length < 12:
        vulnerabilities.append(
            f"Medium: Minimum password length is {password_length}. "
            "Increase it to at least 12 characters."
        )

    if config.get("default_admin_enabled", True):
        vulnerabilities.append(
            "High: Default administrator account is enabled. "
            "Disable or rename the account."
        )

    if not config.get("automatic_updates_enabled", False):
        vulnerabilities.append(
            "Medium: Automatic updates are disabled. "
            "Enable automatic security updates."
        )

    print("Vulnerability Assessment Report")
    print("--------------------------------")

    for number, vulnerability in enumerate(vulnerabilities, start=1):
        print(f"{number}. {vulnerability}")

    print("--------------------------------")
    print(f"Total vulnerabilities: {len(vulnerabilities)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/config_audit.py samples/system_config.json")
    else:
        check_configuration(sys.argv[1])
