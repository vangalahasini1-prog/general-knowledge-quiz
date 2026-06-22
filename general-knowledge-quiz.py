# General Knowledge Quiz

score = 0

print("Welcome to the General Knowledge Quiz!")
print()

# Question 1
answer = input("1. What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

print()

# Question 2
answer = input("2. Which planet is known as the Red Planet? ")

if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Mars.")

print()

# Question 3
answer = input("3. How many continents are there in the world? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 7.")

print()
print("Quiz Completed!")
print("Your Final Score:", score, "/ 3")