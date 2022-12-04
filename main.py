import random
import datetime
import time

kişiler =list()

def kişiekle(x):
   print("-" * 30)
   ekle=input("çekilişe katılacak kişinin ismi?")
   kişiler.append(ekle)
   print("-" *30)

def kişigör(x):
    print("-" * 30)
    say=1
    for i in x:
       print(str(say)+".kişinin ismi",i)
       say=+1
    print("-" * 30)
def kişiseç(x):
    print("-" * 30)
    seçileceksayı=int(input("kaç kişi seçilsin?"))
    seçilen=random.sample(x,seçileceksayı)
    say=1
    for i in seçilen:
        print(str(say)+ "seçilen kişinin ismi",i)
        say+=1
    print("-" * 30)
def karıştır(x):
    print("-" * 30)
    say=1
    random.shuffle(x)
    for i in x:
        print(str(say)+ ".kişinin ismi", i)
        say+=1

while True:
    print("ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ")
    seç=int(input("1-kişiler 2-çekiliş 3-kişileri 4karıştırma"))
    if seç==1:
        print("ekran yükleniyor...")
        time.sleep(3)
        kişiekle(kişiler)
    elif seç==2:
        print("ekran yükleniyor...")
        time.sleep(3)
        kişiseç(kişiler)
    elif seç==3:
        print("ekran yükleniyor...")
        time.sleep(3)
        kişigör(kişiler)
    elif seç==4:
        print("ekran yükleniyor...")
        time.sleep(3)
        karıştır(kişiler)
    else:
        print("ekran yükleniyor...")
        time.sleep(3)
        print("yanlış seçim yaptınız")