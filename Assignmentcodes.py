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