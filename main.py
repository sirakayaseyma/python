print("kodlama")
baslik = "Taşıt Kredisi"
print(baslik)
#stringg => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
#integer=tam sayı
vade = 36
vade2 = "36"

aylikOdeme = 200.50

yukselisteMi = True

# yeniVade = vade / 2
# print(yeniVade)

sayi1 = 15
sayi2 = 15
#else olduğunda herhangi bir açıklama yapmıyorum.
if sayi1 <= sayi2:
    print("sayi1 sayi2 den büyüktür")
elif sayi1 == sayi2:
    print("iki sayi eşittir.")
else: 
    print("sayi1 sayi2den küçüktür")
print("burası if bloğunun dışı")   

# if bloklarında sadece bir blok okunur karar çıkmıştır diğer bloklara gerek kalmaz
# her yeni if yapısı kontrole baslatır yani alt alta koyduğum if bloklarının hepsi çalısır.