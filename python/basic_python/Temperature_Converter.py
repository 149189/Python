#USer input arithmetic operations
# todo - make a function that converts temperature celsius to farenheit

print("Welcome to Temperature Converter")

print("The Temperature is in which format: 1. Celsius\n 2.Farenheit")
number = int(input("Type the following number: "))

if number==1:
    celsius = float(input("Give Celsius:  "))
    farenheit = 9/5*celsius +32
    print("The celsius to farenheit Convergene is ",farenheit)

elif number==2:
    farenheit = float(input("Give farenheit:  "))
    celsius = (farenheit-32)*9/5
    print("The farenheit to celsius convergence is ",celsius)    
else:
    print("Wrong input please run the application again!")
        



