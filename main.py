print("Kodlamaio")
baslik = "Taşit Kredisi"
print("baslik")
#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36
ekVade = 12 #Boslugun okuma kolaylıgı için zorunlu degıl
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True veye False
yukselisteMi = False

#matematiksel operatorler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade-12)
print(vade + ekVade)
print(36-6)

# *
print(5*5)
print(vade * 2)
print(vade * ekVade)
print(10*10)

# /
print(5/5)
print(vade / 2)
print(vade / ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

#% => mod operatoru
print(10%2) #kalan veriyor
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


#mantıksal operatörler
print(1 == 1)
print(1 ==2)

#secılen yeri yorum satırı yapar #edıt-> toogle lıne comment de kullanılabilir
#Ctrl K + Ctrl c
print(1 > 2)
print(3 > 1)
print(1>1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and

print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)  

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 >2 and 3 > 2) #or önce okunur and'den


# karar yapıları
# if else

sayi1 = 10
sayi2 = 15
#sayi1 sayi2'den buyukse erkrana sayi 1 daha buyuk yazdır
#condition

#indent
if sayi1 <= sayi2:
    print("Sayi 1 sayi 2'den kucuktur.") #1 tab bosluk suslu parantez gorevı goruyor
    print("Hala if blogunun içindeyim.")
#eger if bloguna girmez ise
elif sayi1 == sayi2:  # elif = else if
    print("iki sayi esittir.")
#eger if ve else if bloklarında hıc bırıne gırmezse 
else:
    print("sayi 1 sayi 2'den buyuktur.")

print("*************************************")

if sayi1 <= sayi2:  #iki if ayrı algılanır 
    print("Sayi 1 sayi 2'den kucuk veya esittir.") 
if sayi1 == sayi2:  # bu dsa ayrı algılanır ve else ile bağlantısı olan kod satırı budur
    print("iki sayi esittir.")
else:
    print("sayi 1 sayi 2'den buyuktur.")



print("Burasi if blogunun disidir.")
