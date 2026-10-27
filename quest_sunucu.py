"""Meta Quest icin yerel HTTPS sunucu.

WebXR (VR modu) yalnizca HTTPS veya localhost uzerinde calisir. Bu betik
klasoru ag uzerinden HTTPS ile yayinlar; Quest ayni Wi-Fi'deyken tarayicidan acilir.
Ilk calistirmada kendinden imzali sertifika uretir (.cert klasoru).
"""
import datetime
import http.server
import ipaddress
import os
import socket
import ssl
import sys

PORT = 8443
ROOT = os.path.dirname(os.path.abspath(__file__))
CERT_DIR = os.path.join(ROOT, ".cert")
CERT, KEY = os.path.join(CERT_DIR, "cert.pem"), os.path.join(CERT_DIR, "key.pem")


def lan_ips():
    ips = set()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ips.add(s.getsockname()[0])
        s.close()
    except OSError:
        pass
    for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
        ips.add(info[4][0])
    return sorted(i for i in ips if not i.startswith("127."))


def make_cert(ips):
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Tartim Simulasyonu")])
    san = [x509.DNSName("localhost"), x509.IPAddress(ipaddress.ip_address("127.0.0.1"))]
    san += [x509.IPAddress(ipaddress.ip_address(ip)) for ip in ips]
    now = datetime.datetime.now(datetime.timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name).issuer_name(name).public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=1))
        .not_valid_after(now + datetime.timedelta(days=825))
        .add_extension(x509.SubjectAlternativeName(san), critical=False)
        .sign(key, hashes.SHA256())
    )
    os.makedirs(CERT_DIR, exist_ok=True)
    with open(KEY, "wb") as f:
        f.write(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption()))
    with open(CERT, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    with open(os.path.join(CERT_DIR, "ips.txt"), "w") as f:
        f.write(",".join(ips))


def main():
    ips = lan_ips()
    old = ""
    if os.path.exists(os.path.join(CERT_DIR, "ips.txt")):
        old = open(os.path.join(CERT_DIR, "ips.txt")).read()
    if not (os.path.exists(CERT) and os.path.exists(KEY)) or old != ",".join(ips):
        try:
            make_cert(ips)
        except ImportError:
            sys.exit("Eksik paket: once 'pip install cryptography' calistirin.")

    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=ROOT, **k)
    httpd = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(CERT, KEY)
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

    print("\n  Tartim simulasyonu HTTPS ile yayinda.\n")
    for ip in ips:
        print(f"  Quest tarayicisinda acin:  https://{ip}:{PORT}")
    print(f"  Bu bilgisayarda:           https://localhost:{PORT}\n")
    print("  Ilk acilista 'baglanti gizli degil' uyarisi cikar:")
    print("  Gelismis > Devam et. Sonra 'Operator olarak uygula' > 'VR'da ac'.\n")
    print("  Kapatmak icin bu pencereyi kapatin veya Ctrl+C.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
