import socket
import sys
from datetime import datetime

# Banner
print("-" * 60)
print("PYTHON TCP PORT SCANNER")
print("-" * 60)

# Hedef IP Alımı
target_input = input("Hedef IP veya Alan Adı (Örn: scanme.nmap.org): ")

try:
    # DNS Cozumleme
    target_ip = socket.gethostbyname(target_input)
    print(f"\n[+] Hedef IP: {target_ip}")
    print(f"[+] Tarama Baslangici: {datetime.now()}")
    print("-" * 60)

except socket.gaierror:
    print("\n[!] Hata: Hostname cozumlenemedi.")
    sys.exit()

# Tarama Dongusu (Standart 1-1024 Portlari)
try:
    for port in range(1, 1025):
        # Canli ilerlemeyi goster (Opsiyonel, terminali kirletmemesi icin yorum satiri yapilabilir)
        # print(f"Taraniyor: {port}", end='\r') 
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) # Timeout suresi
        
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[*] Port {port} \t[ACIK]")
            
        sock.close()

except KeyboardInterrupt:
    print("\n\n[!] Kullanici islemi iptal etti.")
    sys.exit()

except socket.error:
    print("\n[!] Sunucuya baglanilamadi.")
    sys.exit()

print("-" * 60)
print(f"Tarama Tamamlandi: {datetime.now()}")