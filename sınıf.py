class Human:
    # name= "Osman"
    def __init__(self,name):
        self.name = name
        print("Bir human insance üretildi")
    def __str__(self):
        return f"STr fonk dönen değer : {self.name}"

    def talk(self, sentence):
        name = "Şeyma"
        print(f"{self.name}: {sentence}")
        self.walk()
    def walk(self):
        print(f"{self.name} is walking") 

#self alanı ilgili nesnenin kullanıldığı alanın alınması gerektiğini bilmeliyiz. Yani bir yapı tanımlanmalı
# instance => örnek
human1 = Human("Sude")
human1.talk("Selam")   
human1.walk()
print(human1)
human2 = Human("Osman")
human2.talk("Selam")
human2.walk()