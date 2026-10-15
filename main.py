from modules.recon.cli import create_parser
from modules.recon.command_builder import build_nmap_command


def main():
    parser = create_parser()
    args = parser.parse_args()

    command = build_nmap_command(args)

    print(command)


if __name__ == "__main__":
    main()