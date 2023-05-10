from plyer import notification
import time

print(f"""
Masaüstü hatırlatıcıya hoşgeldiniz.
İstenen bilgileri doğru bir şekilde giriniz.
Günün Tarihi : {time.asctime()}
""")

girdi = input("""Hatırlatmanın verileceği tarihi gün, ay, ayın kaçıncı günü, saat ve yıl 
şeklinde aralarında boşluk olacak şekilde giriniz : """)

title = input("Hatırlatma pencere başlığı : ")
message = input("Hatırlatma mesajı: ")
sure = int(input("Hatırlatmanın nekadar süre gösterileceği : "))

while True:
    if girdi.replace(" ","") == time.asctime().replace(" ",""):
        print("süreye gelindi")
        notification.notify(title=title, message=message, timeout=sure)
        break
