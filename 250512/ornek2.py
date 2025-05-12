liste=[]
toplam=0

for i in range(8):
    liste.append(int(input("bir sayi girin")))
for sayi in liste:
    if sayi %2==0:
        toplam=toplam+sayi
print("çift sayıların toplamı :",toplam)