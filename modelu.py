import math_1 as m
import random
# from math_1 import bol => burası sadece istediğim işlemi alıyorum ve direk o ismi çağırıyorum.as ile kendi istediğim ismi kullanabilirim.
from sınıf import Human
from selenium import webdriver

print(m.bol(10,2))
print(m.topla(20,10))

print(random.randint(0,100)) #rastgele sayı üretir


human1 = Human("Şeyma")
human1.talk("Selam")

chromeDriver = webdriver.Chrome()

#packages => pip 
