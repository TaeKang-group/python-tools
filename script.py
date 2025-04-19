import subprocess

def add_port_forwarding(listen_ip, public_port, internal_port):
    cmd_proxy = [
        "netsh", "interface", "portproxy", "add", "v4tov4",
        f"listenaddress={listen_ip}",
        f"listenport={public_port}",
        "connectaddresss=127.0.0.1",
        f"connectport={internal_port}",
    ]

    cmd_firewall = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name=Allow {public_port}",
        "dir=in", "action=allow", "protocol=TCP",
        f"localport={public_port}",
    ]

    print(f"Adding port forwarding : {listen_ip}:{public_port} -> 127.0.0.1:{internal_port}")

    subprocess.run(cmd_proxy, shell=True)
    subprocess.run(cmd_firewall, shell=True)
    print("Done. \n")

if __name__ == "__main__":
    listen_ip = input("Please enter the your Windows IP : ").strip()

    while True:
        public_port = input("🌐 Port to expose externally (public): ").strip()
        internal_port = input("🎯 Port to connect internally (inside WSL/Docker): ").strip()

        add_port_forwarding(listen_ip, public_port, internal_port)

        cont = input("➕ Add another? (y/n): ").strip().lower()
        if cont != 'y':
            break