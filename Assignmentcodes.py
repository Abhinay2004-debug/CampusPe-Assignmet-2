# 20 Questions
# Question 1:Personal Bio Card

#Using variables to store personal information and print a formatted bio card.
name = "Sai Naga Abhinay"
age = 21
course = "GenAI"
college = "CMR Institute of Technology "
email = "sade22aiml@cmrit.ac.in"

print("||===================================||")
print("||         Personal Bio Card         ||")
print("|| ================================= ||")
print("|| Name:  ", name )
print("|| Age:   ", age  )
print("|| Course: ", course)
print("|| College: ", college )
print("|| Email:  ", email  )
print("||===================================||")

# Question 2: Simple Calculator
# Take 2 inputs of integer type and perform basic arithmatic operations
num1 = (int(input("Enter first number: ")))
num2 = (int(input("Enter second number: ")))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division and Modulus by zero is not allowed.")

print("Exponentiation:", num1 ** num2)

# Question 3: String Manipulator
# Take a string input and perform various string operations
sentence = input("Enter a sentence: ")
print("Original Sentence:", sentence)
print("Characters with space:",len(sentence))
count_no_space = 0 #initially 0 then incremented for each character except space
for ch in sentence:
    if ch != " ":
        count_no_space += 1
print("Characters without space:", count_no_space)
word_count = 1 # initially 1 then incremented for each space to count words
for ch in sentence:
    if ch == " ":
        word_count += 1
print("Number of words:", word_count)
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())   
print("Title case:",sentence.title())
# first word

first_word = ""
for ch in sentence:
    if ch == " ":
        break
    first_word += ch
print("First word:", first_word)

# last word
last_word = ""
for ch in reversed(sentence):
    if ch == " ":
        break
    last_word = ch + last_word
print("Last word:", last_word)

# reverse sentence
reverse_sentence = ""
for ch in reversed(sentence):
    reverse_sentence += ch
print("Reversed Sentence:", reverse_sentence)

#Question 4: Age Calculator
# Take birth year as input and use basic math to calculate age in hours, minutes, and seconds, and also calculate how many years until the user turns 100.
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Age", age)
print("Age in months:", age*12)
print("Age in days:", age*365)
print(" Age in hours:", age *365*24)
print("Age in minutes:", age*365*24*60)
print(" Age until 100:", 100 - age)

#Question 5: Bill Splitter
# Take total bill amount and number of people as input and calculate how much each person should pay
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
if people > 0:
    bill_per_person = total_bill / people
    print("Each person should pay: ", bill_per_person)
else:    print("Number of people must be greater than zero.")
tip_percentage = float(input("Enter tip percentage:"))
tax_percentage = float(input("Enter tax percentage:"))
subtotal = total_bill

# Calculate tax amount
tax_amount = subtotal * tax_percentage / 100

after_tax = subtotal + tax_amount

tip_amount = after_tax * tip_percentage / 100

total_bill = after_tax + tip_amount
# Calculate amount per person
if people > 0:
    per_person = total_bill / people
else:
    per_person = 0

# Display results in formatted way (2 decimal places)
print("\n=== BILL BREAKDOWN ===")
print("Subtotal: ₹{:.2f}".format(subtotal))
print("Tax ({}%): ₹{:.2f}".format(tax_percentage, tax_amount))
print("After tax: ₹{:.2f}".format(after_tax))
print("Tip ({}%): ₹{:.2f}".format(tip_percentage, tip_amount))
print("Total: ₹{:.2f}".format(total_bill))
print("Per person: ₹{:.2f}".format(per_person))

# Question 6: Grade Calculator
# Take marks as input and calculate grade based on a grading scale by if-else conditions and nested if-else conditions. Also calculate total marks and percentage.
total = 0
pass_all = True
for i in range(1,6):
    marks = int(input("Enter marks for subject"+str(i)+": "))
    total += marks
    if marks< 40:
        pass_all = False
percentage = total / 5
print("Total Marks:", total)
print("Percentage:", percentage)
if pass_all:
    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C ")
    elif percentage >= 50:
        print("Grade: D")
    else:        
        print("Grade: F")
    
if pass_all:
    print("Result: Pass")
else:    
    print("Result: Fail")

# Question 7: Temperature Converter
#Define functions to convert temperatures between Celsius, Fahrenheit, and Kelvin using formula given for each.Then you input the users choice of conversion and the temperature value, and call the appropriate function to perform the conversion and display the result in a formatted way. Use a loop to allow multiple conversions until the user chooses to exit.

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    return celsius + 273.15

def k_to_c(kelvin):
    return kelvin - 273.15

def f_to_k(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def k_to_f(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

conversions = {
    '1': (c_to_f, "{:.2f}°C is {:.2f}°F"),
    '2': (f_to_c, "{:.2f}°F is {:.2f}°C"),
    '3': (c_to_k, "{:.2f}°C is {:.2f}K"),
    '4': (k_to_c, "{:.2f}K is {:.2f}°C"),
    '5': (f_to_k, "{:.2f}°F is {:.2f}K"),
    '6': (k_to_f, "{:.2f}K is {:.2f}°F"),
}

while True:
    print("\nTemperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Exiting temperature converter. Goodbye!")
        break

    if choice in conversions:
        value = float(input("Enter the temperature value: "))
        func, format_string = conversions[choice]
        result = func(value)
        print(format_string.format(value, result))
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

# Question 8: Leap Year Checker
# Take a year as input and determine if it is a leap year using if-else conditions and logical operators. 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:    
    print(year, "is not a leap year.")

# Question 9:  Ticket Pricing System 
# Input
age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# Determine base price based on age
if age < 3:
    base_price = 0
    category = "Free"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Calculate total base amount
total_base = base_price * tickets

# Determine discount
if day in ["friday", "saturday", "sunday"]:
    discount = 0.20 * total_base
else:
    discount = 0

# total amount

final_amount = total_base - discount

# Final display

print("\n----- Ticket Summary -----")
print("Category:", category)
print("Base price per ticket: ₹", base_price)
print("Total base amount: ₹", total_base)
print("Discount: ₹", discount)
print("Final amount to pay: ₹", final_amount)

# Question 10:  ATM Simulator
# Create a simple ATM simulator that allows users to check their balance, deposit money, and withdraw money. Use variables to store the balance and a loop to allow multiple transactions until the user chooses to exit. Implement basic error handling for invalid inputs and insufficient money.
# Initial setup
balance = 10000
MIN_BALANCE = 500
transactions = []   # Array to store transaction history

while True:

    print("\n ATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    # Check Balance
    if choice == "1":
        print(f"Current Balance: ₹{balance}")
    
    # Deposit Money
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited ₹{amount}")
            print("Deposit successful!")
            print(f"New balance: ₹{balance}")
        else:
            print("Invalid deposit amount.")
    
    #Withdraw Money
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount <= 0:
            print("Invalid withdrawal amount.")
        
        elif amount > balance:
            print("Insufficient balance!")
        
        elif balance - amount < MIN_BALANCE:
            print(f"Minimum balance of ₹{MIN_BALANCE} must be maintained.")
        
        else:
            balance -= amount
            transactions.append(f"Withdrew ₹{amount}")
            print("Withdrawal successful!")
            print(f"New balance: ₹{balance}")
    
    # Exit
    elif choice == "4":
        print("\nTransaction History:")
        for t in transactions:
            print("-", t)
        print("Thank you for using the ATM!")
        break
    
    else:
        print("Invalid choice! Please select 1-4.")

#Question 11:  Number pattern printer
#Create various patterns by using the simple looping conditions by understanding the height condition behind every pattern.
print("NUMBER PATTERN PRINTER")

print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

choice = int(input("Enter pattern number (1-4): "))
n = int(input("Enter pattern height: "))

print()

for i in range(1, n + 1):
    
    # First Pattern 
    if choice == 1:
        for j in range(1, i + 1):
            print(j, end=" ")

    
    # Second Pattern 
    elif choice == 2:
        for j in range(i):
            print(i, end=" ")
    
    # Third Pattern 
    elif choice == 3:
        for j in range(n - i + 1, 0, -1):
            print(j, end=" ")
    
    # Fourth Pattern 
    elif choice == 4:
        # Ascending component
        for j in range(1, i + 1):
            print(j, end="")
        # Descending component
        for j in range(i - 1, 0, -1):
            print(j, end="")
    
    else:
        print("Incorrect choice")

        break
    
    print() 

# Question 12:  Multiplication Table Generator
# Take a number as input and generate its multiplication table up to given range using a loop.
num = int(input("Enter a number"))
range_limit = int(input("Enter range limit:"))

for i in range(1,range_limit+1):
    print(f"{num} x {i} = {num*i}")


# Question 13:  Sum and Average Calculator
#Take a list of numbers as input and compute simple sum , average of those numbers , find largest and smallest numbers using for loop and conditional functions. 
count = int(input("Enter count of numbers: "))


if count <= 0:
    print("Invalid count")
else:
    first = float(input("Enter number 1: "))
    total = first
    maximum = first
    minimum = first

    for i in range(2, count + 1):
        num = float(input(f"Enter number {i}: "))
        total += num

        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    average = total / count

    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")  


#Question 14: Factorial Calculator
# Take a number as input and calculate its factorial using a loop.
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f" {num}! = 1.")
else:
    factorial = 1
    expression = ""
    for i in range(1, num + 1):
        factorial *= i
        expression += str(i)
        if i != num:
            expression += " x "# Trailing x for all numbers except the last one to create the expression string
    
    print(f"{num}! = {expression} = {factorial}")


# Question 15: Prime Number Checker
# Simple condition of modulus will help to check if it is prime or not.Here if modulus is 0 then it is not prime else it is prime.

num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
elif num == 2:
    print(num, "is a prime number.")

else:
    is_prime = True
    for i in range(2,num):
        if num%i == 0:
            is_prime = False
            break   
    if is_prime:
        print(num, "is a prime number.")    
    else:
        print(num, "is not a prime number.")

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

primes = []   # Array to store prime numbers

for num in range(start, end + 1):

    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

print("Prime numbers:", end=" ")
for p in primes:
    print(p, end="  ")

# Question 16: Random Number Guessing Game
import random

while True:
    print("\n    NUMBER GUESSING GAME \n")
    
    secret_number = random.randint(1, 100)
    attempts = 7
    guessed_correctly = False

    print(" A number between 1 and 100 has been randomly selected.")
    print("You have 7 attempts to guess it.")

    while attempts > 0:
        guess = int(input("\nEnter your guess: "))

        if guess == secret_number:
            print(f" Congratulations! You guessed it in {8 - attempts} attempts.")
            guessed_correctly = True
            break

        elif guess < secret_number:
            attempts -= 1
            print("Too low!")
            print(f"Attempts remaining: {attempts}")

        else:
            attempts -= 1
            print("Too high!")
            print(f"Attempts remaining: {attempts}")

    if not guessed_correctly:
        print(f"\nYou failed! The correct number was {secret_number}.")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break


    # Question 17:  Palindrome Checker
# The original string is converted to lowercase to ensure the palindrome check is case-insensitive. Then, a loop iterates through the string in reverse order to construct the reversed version. Finally, the original and reversed strings are compared to determine if it's a palindrome or not.

value = input("Enter a string or number: ")
original = value
process = original.lower()
reversed_value = ""

for i in range(len(process)-1,-1,-1):
    reversed_value += process[i]
    
print("Original:", original)
print("Reversed:", reversed_value)  

if process == reversed_value:
    print("Result: Palindrome") 
else:
    print("Result: Not a palindrome")


   # Question 18: Calculator with Functions
# Here u create functions for each arithmetic operation (addition, subtraction, multiplication, division, modulus, and exponentiation) where simple formula is enclosed in each function. Then you create a menu-driven interface that allows the user to select an operation and input the required numbers. The program calls the appropriate function based on the user's choice and displays the result in a formatted way. A loop is used to allow multiple calculations until the user chooses to exit.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
    
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Modulus by zero is not allowed."
    
def exponentiate(a, b):
    return a ** b

def calculator():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting Calculator")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))

            elif choice == "2":
                print("Result:", subtract(a, b))

            elif choice == "3":
                print("Result:", multiply(a, b))

            elif choice == "4":
                print("Result:", divide(a, b))

            elif choice == "5":
                print("Result:", modulus(a, b))

            elif choice == "6":
                print("Result:", exponentiate(a, b))

        else:
            print("Invalid choice. Please select 1-7.")


# Run the calculator
calculator()


#  Question 20: Number System Functions

# 1. Factorial
def fact(n):
    if n < 0:
        return "Invalid input "
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2. Prime Check
def is_prim(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 3. Fibonacci (nth term)
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# 4. Sum of Digits
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# 5. Reverse Number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n //= 10
    return sign * reverse


# 6. Armstrong Number
def is_armstrong(n):
    temp = abs(n)
    digits = len(str(temp))
    total = 0
    original = temp

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == original


# 7. GCD (Euclidean Algorithm)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# 8. LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# 9. Perfect Number
def is_perfect_number(g):
    if g <= 1:
        return False

    total = 0
    for i in range(1, g):

        if g % i == 0:
            total += i

    return total == g


# 10. Menu
def math_menu():
    while True:
        print("\n            NUMBER SYSTEM MENU       \n")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "10":
            print("Exiting Program.")
            break

        elif choice == "1":
            n = int(input("Enter number: "))
            print("Result:", fact(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print( is_prim(n))

        elif choice == "3":
            n = int(input("Enter n: "))
            print("Fibonacci term:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print( is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect number?", is_perfect_number(n))

        else:
            print("Invalid choice. Please try again.")


# Main program
math_menu()