def build_nmap_command(args):
    command = ["nmap"]

    if args.quick_scan:
        command.extend(["-sS", "-F", "-T3"])

    if args.full_scan:
        command.extend(["-sV", "-sC"])

    if args.ports:
        command.extend(["-p", args.ports])

    command.append(args.target)

    return command