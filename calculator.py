print("Simple Calculator")
result = float(input("First number: "))

while True:
    op = input("Operator (+, -, *, /, //, %, ** or 'exit'): ")
    if op == 'exit':
        print("Final result:", result)
        break

    num = float(input("Next number: "))

    if op == '+':
        result = result + num
    elif op == '-':
        result = result - num
    elif op == '*':
        result = result * num
    elif op == '/':
        if num != 0:
            result = result / num
        else:
            print("Cannot divide by zero.")
            continue
    elif op == '//':
        if num != 0:
            result = result // num
        else:
            print("Cannot divide by zero.")
            continue
    elif op == '%':
        if num != 0:
            result = result % num
        else:
            print("Cannot divide by zero.")
            continue
    elif op == '**':
        result = result ** num
    else:
        print("Invalid operator.")
        continue

    print("Result:", result)

