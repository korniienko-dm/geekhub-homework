"""
Task_5:
Create a Python program that repeatedly prompts the user for a number until
a valid integer is provided. Use a try/except block to handle any ValueError
exceptions, and keep asking for input until a valid integer is entered.
Display the final valid integer.
"""


hello_string = f"\n**************\nSIMPLE CAPTCHA\n**************"
captcha_condition = "\nEnter result of the expression:"
captcha_task = "\n(5 + 5)"

captcha_valid_answer = 10

while True:
    print(hello_string, captcha_condition, captcha_task)
    
    try:
        user_input = input("\nPlease enter your answer: ")

        if int(user_input) == captcha_valid_answer:
            print(f"\nValidation passed your value: {user_input} is correct!")
            break
    
    except ValueError:
        print(f"\n\n\nValueError: {user_input} is not correct value. Please enter the value again.")
        continue

    else:
        print(f"\n\nWrong answer: {user_input} is not correct value. Please enter the value again.")
