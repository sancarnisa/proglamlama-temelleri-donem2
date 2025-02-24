sinav_notu=int(input("sinav notunu giriniz : "))
sinav_notu2=int(input("sinav notunu giriniz : "))
performans_notu=int(input("performans notunu girin : "))
ortalama=(sinav_notu+sinav_notu2+performans_notu)/3
if ortalama>50:
    print("başarılı")
else:
    print("başarısız")