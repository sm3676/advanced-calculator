from app.calculator import Calculator

def main():
    calc = Calculator()

    while True:
        print("\n--- Advanced Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. History")
        print("6. Undo")
        print("7. Redo")
        print("8. Clear History")
        print("9. Exit")

        choice = input("Choose option: ")

        try:
            if choice in ["1", "2", "3", "4"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                operations = {
                    "1": "add",
                    "2": "subtract",
                    "3": "multiply",
                    "4": "divide"
                }

                result = calc.perform_calculation(operations[choice], a, b)
                print("Result:", result)

            elif choice == "5":
                history = calc.get_history()
                for item in history:
                    print(item)

            elif choice == "6":
                calc.undo()
                print("Undo successful")

            elif choice == "7":
                calc.redo()
                print("Redo successful")

            elif choice == "8":
                calc.clear_history()
                print("History cleared")

            elif choice == "9":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()