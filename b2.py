#listeler
#döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi" , 10 , 5.2 , True]
print(dizi)

krediler = ["İhtiyaç Kredisi" , "Taşıt Kredisi" , "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) # uzunluğu bulmamı sağlar. Kaç eleman varsa elemanın bir eksiği index

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")

krediler.pop(0) #pop içine index vermexsek -1 de bulunan yani son elemanı siler.
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi") #index sırasına göre bulduğu ilk elemanı siler.
print(krediler)


#for
# i= 0 i<10

for i in range(10):
    print(i)
print("++++++")
for i in range(5,10):
    print(i)
print("********")
for i in range(0,51,10): #0dan başla 10ar 10ar arttır 51e kadar git
    print(i)
print("%%%%%")

krediler = ["İhtiyaç Kredisi" , "Taşıt Kredisi" , "Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("??????????")

for j in range(len(krediler)):
    print(krediler[j])

print("************************")

#sonsuz döngü
i=0
while i < 10:
    print("x")
    i += 1     
print("y")

print("************************")

while True:
    print("X")
    break

print("************************")
i = 0 
while i < len(krediler):
    i+=1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

#fonksiyonlar

print("****Fonksiyonlar****")

fiyat = 100
indirim = 20

yeniFiyat = fiyat - indirim

# definition define fonksiyon tanımlar
def calculate():
    print(100-20)

def calculateWithParams(a,b):
    print(a-b)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Osman")
sayHello("Şeyma")

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("*****")
fonk1 = calculatePrice(100,50) #bu fonksiyon geriye bir değer dönmüyor. return değer döndürmemi sağlar.
fonk2 = calculatePriceAndReturn(300,100)
print("fonk1:" , fonk1)
print("fonk2:" ,fonk2)
print("********")
