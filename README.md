# Basit TCP Port Tarayıcı
-Shodan kullanıldığını biliyorum proje mantığı anlamak adına yapılmıştır.
Bu proje, ağ güvenliği ve Python "Socket" programlama mantığını kavramak amacıyla geliştirdiğim temel seviye bir ağ tarama aracıdır.

Projenin Amacı
Bu proje, hedef bir sistem üzerinde hangi servislerin açık olduğunu tespit etmeye yarar. Hazır araçlar (Nmap vb.) kullanmak yerine, arka planda dönen TCP bağlantı (handshake) mantığını anlamak için bu aracı kendim kodladım.

Nasıl Çalışır? (Port Scanner Mantığı)
Bir bilgisayarda iletişim sağlayan binlerce sanal gate (port) bulunur. Bu yazılım:
1. Hedef IP adresini veya alan adını alır.
2. Belirtilen aralıktaki (bende 1-1024) portlara tek tek TCP Request gönderir.
3. Eğer hedef sistemden olumlu yanıt gelirse, o portun available olduğunu raporlar.
4. Bu işlem Python'un yerleşik socket kütüphanesi ile gerçekleştirilir.

- Python 3
- Socket Library
- Datetime 

Kurulum ve Kullanım
1. Python yüklü olmalı 
2. python scanner.py
3. Hedef adresi girin (kendi adresinizde de deneyebilirsiniz(localhost)).

-Not
Bu yazılım sadece eğitim amaçlıdır.Başkalarına ait sistemlerde izinsiz tarama yapmak yasal suçtur.

Emircan Bingöl
