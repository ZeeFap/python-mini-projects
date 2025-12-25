a = float(input("A: "))
op = input("Operation (+ - * /): ").strip()
b = float(input("B: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Division by zero")
else:
    print("Unknown operation")
