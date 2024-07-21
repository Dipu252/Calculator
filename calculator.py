print("Welocme to calcutor with basic arithmetic operations.")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
opertor=input("Enter the arithmetic operator: ")

match opertor:
    case "+":print(f"{num1} + {num2} =",num1+num2)

    case "-":print(f"{num1} - {num2} =",num1-num2)

    case "*":print(f"{num1} X {num2} =",num1*num2)

    case "/":print(f"{num1} / {num2} =",num1/num2)

    case default:print("Please enter correct operator!")