ders_notu=[]
toplam=0
for i in range(6):
    ders_notu(int(input("ders notlarının girin")))
for sayi in ders_notu:
    toplam=toplam+ders_notu
ortalama=toplam/6

print("ortalamayı ekrana yazdır")