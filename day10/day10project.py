import calculator_logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(calculator_logo.logo)
    should_accumulate = True
    number = float(input("What's the first number?: "))
    
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        
        methods = input("Pick an operation: ")
        add_number = float(input("What's the next number?: "))
        result = operations[methods](number, add_number)
        print(f"{number} {methods} {add_number} = {result}")
        
        next = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation ")

        if next == "y":
            number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()