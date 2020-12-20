count = 0
for number1 in range(1,10):
    for number2 in range(0,10):
        for number3 in range(0,10):
            if number1!= number2 and number2 !=number3 and number1 != number3:
               print(str(number1)+str(number2)+str(number3))
               count += 1
print("toplam",count, "tane sayı vardır")