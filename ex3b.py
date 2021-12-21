#normal_calculator program




#input choice
operation =input('''please type the operation you want to perform :
    + for addition
    - for subtraction 
    * for mutliplication
    / for divide
    ''')
#taking user input
num1 = int(input('enter the first number:'))
num2 = int(input('enter the secound number:'))

#condition
if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)    

elif operation == '/':
    print(num1 / num2)
else:
    print("invalid choice")
