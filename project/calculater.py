#reating a calculater by asking user 
num1 = int (input("enter your first num : "))
ope = input("emer ypur operator : ")
num2 = int (input("enter your second num : "))

if ope =="+":
    print(f"your sum of {num1} + {num2} is {num1+num2} ")

elif ope =="*":
    print(f"your mul of {num1} * {num2} is {num1*num2} ")

elif ope =="/":
    print(f"your div of {num1} / {num2} is {num1/num2} ")

elif ope =="%":
    print(f"your reminder of {num1} % {num2} is {num1%num2} ")


elif ope =="-":
    print(f"your diff of {num1} - {num2} is {num1-num2} ")

else:
    print("invalid opertaor")