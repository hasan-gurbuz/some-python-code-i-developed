primenbr = 0
x = 1
while 1 == 1:
    sayi = int(input("entere a number"))
    if sayi == -1:
        print("number",x," = ",sayi)
        break
    else:
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    primenbr += 1
        print("number",x," = ",sayi)
    x += 1
print("the quantity of prime numbers:",primenbr)