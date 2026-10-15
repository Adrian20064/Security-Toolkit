import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="security-toolkit",
        description="Security Toolkit network reconnaissance module"
    )

    parser.add_argument(
        "target",
        help="Target IP, hostname, or CIDR range"
    )

    parser.add_argument(
        "--quick-scan",
        action="store_true",
        help="Run a quick Nmap scan"
    )

    parser.add_argument(
        "--full-scan",
        action="store_true",
        help="Run a full Nmap scan"
    )

    parser.add_argument(
        "--ports",
        help="Scan specific ports, e.g. 22,80,443"
    )

    return parser