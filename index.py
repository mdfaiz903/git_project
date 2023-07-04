num1 = 120
num2 = 4000
num3 = 3000
num5 = 8000
num4=8000
if num1>num2 and num1>num3 and num1>num4:
    print(num1)
elif num2 > num3 and num2 > num1 and num2>num4:
    print(num2)
elif num3 > num1 and num2 > num1:
    print(num2)
else:
    print(num3)
