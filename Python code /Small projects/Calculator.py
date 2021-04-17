print("What operation do you want?")
operator = input(" enter either +, -, * or divide: ")
n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))

if operator == '+':
    print(n1, operator, n2, "=", n1 + n2)
elif operator == '-':
    print(n1, operator, n2, "=", n1 - n2)
elif operator == '*':
    print(n1, operator, n2, "=", n1 * n2)
elif operator == 'divide':
    print(n1, operator, n2, "=", n1 / n2)
else:
    print("Invlid operator")
