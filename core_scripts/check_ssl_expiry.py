import ssl, socket
from datetime import datetime

hostname = "npps-dev.test.ai"
try:
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.connect((hostname,443))
        cert = s.getpeercert()
        print(f"{hostname} expires after {cert['notAfter']}")
except Exception as e:
    print(f"Error connecting hostname {hostname}")