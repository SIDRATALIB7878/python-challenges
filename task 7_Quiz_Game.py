import random
import time

# 50 Python Basics Questions
question_bank = [
    {"question": "What is Python?", "options": ["A) A type of snake", "B) A programming language", "C) A web framework", "D) A database"], "answer": "B"},
    {"question": "Who developed Python?", "options": ["A) Dennis Ritchie", "B) James Gosling", "C) Guido van Rossum", "D) Mark Zuckerberg"], "answer": "C"},
    {"question": "In which year was Python first released?", "options": ["A) 1989", "B) 1991", "C) 1995", "D) 2000"], "answer": "B"},
    {"question": "What is the correct syntax to output 'Hello, World!' in Python?", "options": ["A) echo 'Hello, World!'", "B) print('Hello, World!')", "C) print(Hello, World!)", "D) console.log('Hello, World!')"], "answer": "B"},
    {"question": "Which of the following is a Python data type?", "options": ["A) int", "B) float", "C) str", "D) All of the above"], "answer": "D"},
    {"question": "What is the correct way to create a list in Python?", "options": ["A) list = (1, 2, 3)", "B) list = [1, 2, 3]", "C) list = {1, 2, 3}", "D) list = <1, 2, 3>"], "answer": "B"},
    {"question": "Which function is used to get the length of a list in Python?", "options": ["A) length()", "B) len()", "C) getLength()", "D) size()"], "answer": "B"},
    {"question": "Which of the following is used to comment a line in Python?", "options": ["A) //", "B) /* */", "C) #", "D) --"], "answer": "C"},
    {"question": "What is the output of 'print(2 + 3 * 4)' in Python?", "options": ["A) 14", "B) 20", "C) 26", "D) 12"], "answer": "A"},
    {"question": "What is the type of the variable 'x = 5.0'?", "options": ["A) int", "B) str", "C) float", "D) bool"], "answer": "C"},
    {"question": "How do you define a function in Python?", "options": ["A) function myFunction():", "B) def myFunction():", "C) func myFunction():", "D) define myFunction():"], "answer": "B"},
    {"question": "Which operator is used for exponentiation in Python?", "options": ["A) ^", "B) **", "C) ^", "D) *"], "answer": "B"},
    {"question": "What is the output of 'print(7 // 3)'?", "options": ["A) 2.33", "B) 2", "C) 3", "D) 3.0"], "answer": "B"},
    {"question": "Which of the following is a valid variable name in Python?", "options": ["A) 2variable", "B) my-variable", "C) _variable", "D) !variable"], "answer": "C"},
    {"question": "What does 'break' do in a loop in Python?", "options": ["A) Stops the loop", "B) Continues the loop", "C) Exits the program", "D) Pauses the loop"], "answer": "A"},
    {"question": "What is the result of 'True + 1' in Python?", "options": ["A) 1", "B) 0", "C) True", "D) Error"], "answer": "A"},
    {"question": "How do you open a file for writing in Python?", "options": ["A) open('file.txt', 'w')", "B) file('file.txt', 'write')", "C) open('file.txt', 'r')", "D) open('file.txt', 'wb')"], "answer": "A"},
    {"question": "What is the correct syntax to import a module in Python?", "options": ["A) import module_name", "B) #include module_name", "C) import module", "D) use module_name"], "answer": "A"},
    {"question": "What is the output of 'print('hello'.upper())'?", "options": ["A) hello", "B) HELLO", "C) Hello", "D) hello. upper"], "answer": "B"},
    {"question": "Which of the following is not a valid Python data type?", "options": ["A) List", "B) Set", "C) Dictionary", "D) Array"], "answer": "D"},
    {"question": "Which of the following is the correct syntax for an if statement in Python?", "options": ["A) if x > 10 then:", "B) if x > 10:", "C) if x > 10 then", "D) if(x > 10):"], "answer": "B"},
    {"question": "What is the correct syntax for defining a class in Python?", "options": ["A) class MyClass:", "B) MyClass class:", "C) class MyClass():", "D) define MyClass:"], "answer": "A"},
    {"question": "Which function returns the type of a variable in Python?", "options": ["A) type()", "B) typeof()", "C) varType()", "D) gettype()"], "answer": "A"},
    {"question": "Which of the following methods removes all elements from a list in Python?", "options": ["A) clear()", "B) remove()", "C) del()", "D) reset()"], "answer": "A"},
    {"question": "What is the keyword used to create a loop in Python?", "options": ["A) for", "B) while", "C) loop", "D) Both A and B"], "answer": "D"},
    {"question": "What is used to indicate the end of a block of code in Python?", "options": ["A) }", "B) ]", "C) :", "D) ;"], "answer": "C"},
    {"question": "Which of the following is not a valid operator in Python?", "options": ["A) +", "B) -", "C) *", "D) /", "E) &"], "answer": "E"},
    {"question": "Which of the following is used to handle exceptions in Python?", "options": ["A) try", "B) except", "C) finally", "D) All of the above"], "answer": "D"},
    {"question": "What is the default value of a boolean variable in Python?", "options": ["A) True", "B) False", "C) 0", "D) None"], "answer": "B"},
    {"question": "How do you write a comment in Python?", "options": ["A) /* comment */", "B) // comment", "C) # comment", "D) comment//"], "answer": "C"},
    {"question": "Which of the following data types is immutable in Python?", "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"], "answer": "C"},
    {"question": "What is the output of 'print(10 == 10)' in Python?", "options": ["A) 1", "B) True", "C) False", "D) Error"], "answer": "B"},
    {"question": "Which of the following is used to create an empty set in Python?", "options": ["A) set = {}", "B) set = set()", "C) set = []", "D) set = ()"], "answer": "B"},
    {"question": "Which of the following is the correct way to declare a string in Python?", "options": ["A) str = 'Hello'", "B) str = \"Hello\"", "C) Both A and B", "D) str = Hello"], "answer": "C"},
    {"question": "Which of the following is not a valid function in Python?", "options": ["A) abs()", "B) pow()", "C) sqrt()", "D) round()"], "answer": "C"},
    {"question": "Which of the following is a valid list method in Python?", "options": ["A) append()", "B) insert()", "C) pop()", "D) All of the above"], "answer": "D"},
    {"question": "How do you write a string literal in Python?", "options": ["A) 'Hello World'", "B) 'Hello World'", "C) \"Hello World\"", "D) Both A and C"], "answer": "D"},
    {"question": "Which of the following keywords is used to define a function in Python?", "options": ["A) function", "B) def", "C) func", "D) define"], "answer": "B"},
    {"question": "What is the default value of a variable if it is not initialized in Python?", "options": ["A) None", "B) 0", "C) False", "D) Undefined"], "answer": "A"},
    {"question": "Which of the following is used to escape characters in Python?", "options": ["A) /", "B) \\", "C) &", "D) @"], "answer": "B"},
    {"question": "Which operator is used to find the remainder in Python?", "options": ["A) //", "B) %", "C) /", "D) **"], "answer": "B"},
    {"question": "Which of the following is the correct syntax for a while loop in Python?", "options": ["A) while x < 10:", "B) while (x < 10):", "C) while x < 10", "D) while x: < 10"], "answer": "A"},
    {"question": "Which method is used to remove an element from a dictionary in Python?", "options": ["A) remove()", "B) pop()", "C) del()", "D) clear()"], "answer": "B"},
    {"question": "Which function returns the largest value from a list?", "options": ["A) max()", "B) largest()", "C) getMax()", "D) maxValue()"], "answer": "A"},
]

# Ask for student details
name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")
section = input("Enter your section: ")

# Start the quiz
print(f"\nWelcome, {name} (Roll No: {roll_number}, Section: {section})!")
print("\n-------------------- PYTHON QUIZ --------------------\n")
print("You will have 30 seconds to answer each question. Good luck!\n")

# Select 20 random questions from the question bank
selected_questions = random.sample(question_bank, 20)
random.shuffle(selected_questions)  # Shuffle for randomness

score = 0

# Loop through selected questions
for i, q in enumerate(selected_questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q["options"]:
        print(option)

    start_time = time.time()  # Start timer
    answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
    elapsed_time = time.time() - start_time  # Calculate time taken

    # Time check
    if elapsed_time > 30:
        print("⏳ Time's up! No points awarded.\n")
        continue

    # Answer check
    if answer == q["answer"]:
        print("✅ Correct! 🎉\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was {q['answer']}.\n")

# Final Score
print(f"🎯 Final Score: {score}/20")
