from safe_tools import safe_number, safe_divide

print("--- Unbreakable Program Demo ---")

while True:
    user_input = input("Enter a number to double (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Exiting program safely. Goodbye!")
        break
    
    num = safe_number(user_input)
    if num == "Not a number":
        print("That's not a valid number, but the program didn't crash! Try again.")
    else:
        print(f"Double your number is: {num * 2}")

print("\nTesting safe division:")
print(f"100 / 5 = {safe_divide(100, 5)}")
print(f"100 / 0 = {safe_divide(100, 0)}")
