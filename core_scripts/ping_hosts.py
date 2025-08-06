import subprocess
try:
    with open("../files/hosts.txt") as f:
        for host in f:
            host = host.strip()
            try:
                output = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                if (output.returncode == 0):
                    print(f"status of {host} is UP")
                else:
                    print(f"status of {host} is DOWN")
            except Exception as e:
                print(f"Unexpected error {e}")
except FileNotFoundError:
    print("host file does not exist.")
except Exception as e:
    print(f"Unexpected error {e}")
        