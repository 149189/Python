print("Welcome to My calculator")

print("Give two numbers on which you want to perfrom arithmetic operations: ")
num1 = float(input("Give First number: "))


print("Arithmetic Menu:\n 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division")
a = int(input("Select appropriate number for required arithmetic operation: "))

if a==1:
    result = num1+num2
    print("The result is ",result)
elif a==2:
    result = num1-num2    
    print("The result is",result)
elif a==3:
    result = num1*num2
    print("The result is ",result)
elif a==4:
    result = num1/num2
    print("The result is ",result)
else:
    print("Wrong Input please run the application again")            
