"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    status = determine_status(score)

    print(f"User score {score} is {status}")

    if status == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    determine_status(random_score)
    print(f"Random: {random_score} = {determine_status(random_score)}")

def determine_status(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()