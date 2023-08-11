print("merhaba")

faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz)) #faiz değerinin tipi


print(int(vade) + 12)


vade = int(input("Lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
print(vade + 12)

vade = vade + 12
#string interpolition
#seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = "Halit"
metin = "Merhaba {name}".format(name=isim)
print(metin)

#f-string
isim = "Osman"
metin = f"Hoşgeldiniz {isim}"
print(metin)