import math

def display_banner():
    print("=" * 40)
    print("        PYTHON CALCULATOR")
    print("=" * 40)
    print(" Operators: + - * / // % ** sqrt")
    print(" Type 'history' to see past results")
    print(" Type 'clear' to reset history")
    print(" Type 'quit' to exit")
    print("=" * 40)

def get_history_display(history):
    if not history:
        print("\n  No history yet.\n")
        return
    print("\n--- Calculation History ---")
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")
    print()

def calculate(expression, history):
    expr = expression.strip()

    # Handle sqrt separately
    if expr.lower().startswith("sqrt"):
        try:
            num = float(expr[4:].strip("() "))
            if num < 0:
                return None, "Error: Cannot take sqrt of a negative number."
            result = math.sqrt(num)
            entry = f"sqrt({num}) = {result}"
            history.append(entry)
            return result, None
        except ValueError:
            return None, "Error: Invalid number for sqrt."

    # Replace ^ with ** for convenience
    expr = expr.replace("^", "**")

    # Safe eval with only math operations allowed
    allowed_names = {
        "__builtins__": {},
        "abs": abs, "round": round,
        "pi": math.pi, "e": math.e,
    }
    try:
        result = eval(expr, allowed_names)
        entry = f"{expression.strip()} = {result}"
        history.append(entry)
        return result, None
    except ZeroDivisionError:
        return None, "Error: Division by zero."
    except SyntaxError:
        return None, "Error: Invalid expression syntax."
    except Exception as e:
        return None, f"Error: {e}"

def main():
    history = []
    display_banner()

    while True:
        try:
            user_input = input("\n  Enter expression: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Goodbye!\n")
            break

        if not user_input:
            continue
        elif user_input.lower() == "quit":
            print("\n  Goodbye!\n")
            break
        elif user_input.lower() == "history":
            get_history_display(history)
        elif user_input.lower() == "clear":
            history.clear()
            print("\n  History cleared.\n")
        else:
            result, error = calculate(user_input, history)
            if error:
                print(f"\n  {error}")
            else:
                print(f"\n  = {result}")

if __name__ == "__main__":
    main()
