HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    if len(lines) == 0:
        print("No history found")
    else:
        for line in reversed(lines):
            print(line.strip())


def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("history cleared...")


def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid number input")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Invalid input: division by zero")
            return
        result = num1 / num2
    else:
        print("Invalid Operator ...")
        return

    if result.is_integer():
        result = int(result)

    print("Result", result)
    save_to_history(user_input, result)


def main():
    print("________Simple Calculator___________")
    while True:
        user_input = input("Enter calculation (or type: history | clear | exit): ")

        if user_input == "exit":
            print("BYE BYE ...")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)


main()
