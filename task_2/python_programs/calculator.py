# x = int(input("Enter the value of x = "))
# y = int(input("Enter the value of y = "))


x = float(input("Enter the value of x = "))
y = float(input("Enter the value of y = "))


#sum
#round(number [, noOfDigits])
z = round(x+y)

print("Sum : ", end = " ")
print(z)
print(f"{z}")
print(f"{z:,}")   #format

#division
z = x / y

print("Divison: ", end = " ")
print(z)

print(f"{z:.3f}")

z = round(z, 2)
print(z)