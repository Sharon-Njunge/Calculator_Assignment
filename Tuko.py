print("select option")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")





operation = input()
if operation == "1":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("the sum is:" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("the subtraction is:" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("the multiplication is:" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("the division is:" + str(int(num1) / int(num2)))


