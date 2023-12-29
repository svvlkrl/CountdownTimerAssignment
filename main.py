from datetime import datetime

while True:
    try:
        countdown_time = input("Geri sayım için tarih giriniz (GG/AA/YYYY formatında): ")
        countdown_time_obj = datetime.strptime(countdown_time,"%d/%m/%Y")

        if countdown_time_obj < datetime.now():
            print("Geçmiş bir tarih girdiniz. Lütfen ileri bir tarih girin.")
        else:
            break
    except ValueError:
        print("Hatalı giriş yaptınız.Lütfen GG/AA/YYYY formatında doğru bir tarih girin.")
while True:
    current_time = datetime.now()
    time_left = countdown_time_obj - current_time
    if time_left.total_seconds() <= 0:
        print("Geri sayım tamamlandı!!")
        break
    else:
        print(f"Geri sayım için kalan süre: {time_left}")

