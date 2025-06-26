import time
import random

# List of [question, options, correct_option]
questions = [
    ["What is the capital of India?",
     ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"], "B"],
    ["Who is known as the Father of the Nation?",
     ["A. Nehru", "B. Patel", "C. Mahatma Gandhi", "D. Subhas Bose"], "C"],
    ["Which planet is known as the Red Planet?",
     ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"], "D"],
    ["Who wrote the national anthem of India?",
     ["A. Bankim Chandra", "B. Premchand", "C. Rabindranath Tagore", "D. Bhagat Singh"], "C"],
    ["Which is the largest animal on land?",
     ["A. Elephant", "B. Lion", "C. Giraffe", "D. Tiger"], "A"],
    ["How many continents are there on Earth?",
     ["A. 6", "B. 5", "C. 7", "D. 8"], "C"],
    ["Which gas do plants use for photosynthesis?",
     ["A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Carbon dioxide"], "D"],
    ["What is H2O commonly known as?",
     ["A. Oxygen", "B. Hydrogen", "C. Water", "D. Salt"], "C"],
    ["Who was the first Prime Minister of India?",
     ["A. Indira Gandhi", "B. Rajendra Prasad", "C. Narendra Modi", "D. Jawaharlal Nehru"], "D"],
    ["Which is the largest ocean in the world?",
     ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"], "B"]
]

# Prize list (1K to 10K)
prizes = [1000, 2000, 3000, 4000, 5000,
          6000, 7000, 8000, 9000, 10000]
safe_level = 5000

used_5050 = False
used_skip = False
amount_won = 0

print("Welcome to Kaun Banega Crorepati (KBC)")
print("You will be asked 10 general knowledge questions.")
print("Each question has 4 options. Answer correctly to win money.")
print("Available lifelines: '5050' (removes 2 wrong options), 'skip' (skip a question).")
print("Safe level: ₹5000 after 5 questions.\n")
input("Press Enter to start the game...")

for i in range(len(questions)):
    question, options, correct = questions[i]

    print(f"\nQuestion {i + 1} for ₹{prizes[i]}")
    print(question)

    option_map = {"A": 0, "B": 1, "C": 2, "D": 3}
    current_options = options.copy()
    for opt in current_options:
        print(opt)

    while True:
        print("\nEnter your answer (A/B/C/D), or type '5050' or 'skip':")
        answer = input("Your choice: ").strip().upper()

        if answer == "5050":
            if used_5050:
                print("You have already used the 50-50 lifeline.")
                continue
            used_5050 = True
            print("Using 50-50 lifeline. Removing two wrong options...")
            correct_index = option_map[correct]
            remaining = [correct_index]
            while len(remaining) < 2:
                rand = random.randint(0, 3)
                if rand != correct_index and rand not in remaining:
                    remaining.append(rand)
            remaining.sort()
            for idx in remaining:
                print(current_options[idx])
            continue

        elif answer == "SKIP":
            if used_skip:
                print("You have already used the skip lifeline.")
                continue
            used_skip = True
            print("Skipping this question.")
            amount_won += prizes[i]
            break

        elif answer in option_map:
            if answer == correct:
                amount_won += prizes[i]
                print("Correct answer.")
                print(f"Total won so far: ₹{amount_won}")
                time.sleep(1)
                break
            else:
                print("Wrong answer.")
                print(f"The correct answer was: {correct}")
                if i >= 4:
                    amount_won = safe_level
                    print(f"You reached the safe level. You take home ₹{safe_level}")
                else:
                    amount_won = 0
                break
        else:
            print("Invalid input. Please try again.")

    if answer not in option_map or answer != correct:
        break

print("\nGame Over.")
print(f"You take home: ₹{amount_won}")
print("Thank you for playing Kaun Banega Crorepati!")
if amount_won >= 10000:
    print("Congratulations! You are a KBC winner!")



# End of the KBC game code
# Note: This code is a simple text-based version of the KBC game.