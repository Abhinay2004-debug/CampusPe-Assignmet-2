# CampusPe-Assignmet-2
Full name : Sai Naga Abhinay Devulapalli

# Project Description:
----------------------------------------

This assignment contains a collection of beginner-level Python programs designed to strengthen understanding of core programming concepts.

The programs cover:

- Variables and Data Types
- Conditional Statements (if-else, nested conditions)
- Loops (for, while)
- Functions
- String Manipulation
- Mathematical Computations
- Menu-Driven Programs
- Number System Logic
- Basic Game Implementation

Each program is written using structured logic with proper validations wherever necessary (e.g., division by zero handling, minimum balance validation in ATM simulator, invalid input checks, etc.).

----------------------------------------
Special Instructions:
----------------------------------------

1. Some programs are menu-driven and will continue running until the user chooses to exit.
2. The ATM Simulator maintains a minimum balance requirement.
3. The Temperature Converter and Calculator programs use function-based modular implementation.
4. The Random Number Guessing Game uses Python's built-in 'random' module.
5. All programs are written using only built-in Python libraries.
6. The entire assignment can be run as a single Python file.

----------------------------------------
Challenges Faced:
----------------------------------------

1. Handling edge cases such as division by zero and invalid user inputs.
2. Designing menu-driven programs that repeatedly execute until exit.
3. Implementing number system logic like Armstrong number, GCD (Euclidean algorithm), and Perfect number.
4. Managing nested loops for pattern printing.
5. Ensuring clean logic flow when multiple interactive programs are combined in a single file.

These challenges helped improve logical thinking and structured problem-solving ability.

#  Python 20 Practice Programs

A collection of 20 beginner-friendly Python programs covering core programming concepts such as variables, loops, conditionals, functions, number systems, and menu-driven applications.

This project is designed to strengthen logical thinking and foundational Python skills.

---

# Concepts Covered

- Variables and Data Types  
- User Input and Output  
- Conditional Statements (if-else, nested conditions)  
- Loops (for, while)  
- Functions  
- String Operations  
- Mathematical Computations  
- Menu-Driven Programs  
- Basic Games  
- Number System Logic  

---

## Program List

### 1. Personal Bio Card
Stores personal details in variables and prints a formatted bio card.

### 2. Simple Calculator
Performs arithmetic operations:
- Addition  
- Subtraction  
- Multiplication  
- Division  
- Modulus  
- Exponentiation  
Includes division-by-zero validation.

### 3. String Manipulator
- Character count (with and without spaces)  
- Word count  
- Uppercase / Lowercase / Title case  
- First and last word extraction  
- Reverse sentence  

### 4. Age Calculator
Calculates:
- Age in years  
- Months  
- Days  
- Hours  
- Minutes  
- Years remaining to turn 100  

### 5. Bill Splitter
- Calculates tax and tip  
- Splits bill among people  
- Displays formatted bill breakdown  

### 6. Grade Calculator
- Takes marks for 5 subjects  
- Calculates total and percentage  
- Assigns grade (A+, A, B, C, D, F)  
- Displays Pass/Fail result  

### 7. Temperature Converter
Menu-driven conversion between:
- Celsius  
- Fahrenheit  
- Kelvin  

Runs continuously until user exits.

### 8. Leap Year Checker
Determines whether a given year is a leap year using logical conditions.

### 9. Ticket Pricing System
Calculates ticket price based on:
- Age category  
- Day of the week  
- Weekend discount  

### 10. ATM Simulator
Features:
- Check balance  
- Deposit money  
- Withdraw money  
- Minimum balance validation  
- Transaction history  

### 11. Number Pattern Printer
Prints 4 different number patterns based on user choice and height.

### 12. Multiplication Table Generator
Generates multiplication table for a given number up to a specified range.

### 13. Sum and Average Calculator
- Calculates sum  
- Computes average  
- Finds maximum and minimum values  

### 14. Factorial Calculator
Computes factorial using loop and displays step-by-step expression.

### 15. Prime Number Checker
- Checks if a number is prime  
- Displays all prime numbers within a range  

### 16. Random Number Guessing Game
- Generates random number (1–100)  
- User gets 7 attempts  
- Provides high/low hints  
- Option to replay  

### 17. Palindrome Checker
Checks whether a string or number is a palindrome (case-insensitive).

### 18. Calculator Using Functions
Menu-driven calculator using separate functions for:
- Add  
- Subtract  
- Multiply  
- Divide  
- Modulus  
- Power  

### 19. ( Not Included as was not able to solve it with ease and without certain built-in functions.Also failure in certain test cases.) 

### 20. Number System Functions
Menu-driven mathematical utility including:
- Factorial  
- Prime Check  
- Fibonacci  
- Sum of Digits  
- Reverse Number  
- Armstrong Number  
- GCD (Euclidean Algorithm)  
- LCM  
- Perfect Number  

---

## How to Run

1. Install Python (3.x recommended).
2. Clone this repository or download the file.
3. Open terminal or command prompt.
4. Run:

```bash
python filename.py
```

---

## Purpose

This project is created for:
- Python beginners  
- Students practicing core programming  
- Strengthening logical problem-solving skills  
- Academic lab practice  

---

##  Requirements

- Python 3.x  
- No external libraries required (uses only built-in modules like `random`)  

---

##  License

This project is for educational purposes.


# Generative AI API Integration (Assignment)

##  Overview

This project demonstrates integration of multiple Generative AI APIs using Python.
Each API is implemented in a separate Python file that:

* Accepts user input
* Sends request to the API
* Displays AI-generated response
* Handles errors where applicable

---

##  APIs Implemented

### 1. Groq API

* File: `groq_api.py`
* Model: `llama-3.3-70b-versatile`
* Description: Uses Groq platform for fast LLM inference.

---

### 2. Google Gemini API

* File: `gemini_api.py`
* Model: `gemini-3-flash-preview`
* Description: Uses Google Gemini models via `google-genai` SDK.

---

### 3. Hugging Face API

* File: `huggingface_api.py`
* Model: `MiniMaxAI/MiniMax-M2.5:novita`
* Description: Uses Hugging Face InferenceClient with chat completion.

---

### 4. Cohere API

* File: `cohere_api.py`
* Model: `command-r7b-12-2024`
* Description: Uses Cohere chat API (ClientV2) for text generation.

---

### 5. Ollama API (Local)

* File: `ollama_api.py`
* Model: `gemma3:1b`
* Description: Runs locally using Ollama (no external API cost).

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd CampusPe-Assignmet-2
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` File

Add your API keys:

```env
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key
HF_API_KEY=your_key
COHERE_API_KEY=your_key
```

---

##  Running the Programs

Run each file individually:

```bash
python groq_api.py
python gemini_api.py
python huggingface_api.py
python cohere_api.py
python ollama_api.py
```

---

##  Screenshots

Screenshots of outputs are included in the `screenshots/` folder and uploaded in seperate document.

---

##  Notes

* API keys are stored securely using environment variables
* `.env` file is not uploaded for security reasons
* Some APIs may have:

  * Rate limits
  * Model availability issues
* Ollama requires local installation:

  ```
  https://ollama.com
  ```

---

## Features

* Multiple AI API integrations
* Consistent program structure
* User input handling
* Error handling
* Secure API key management

---

##  Conclusion

This project demonstrates practical integration of multiple AI providers and highlights differences in API design, model usage, and response handling across platforms.
