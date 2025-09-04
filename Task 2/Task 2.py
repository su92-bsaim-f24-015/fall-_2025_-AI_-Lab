import random

def fizzbuzz_check(number1: int, number2: int = None) -> str:
    
    total = number1 if number2 is None else number1 + number2
    if total % 15 == 0:
        return "Fizz Buzz"
    elif total % 3 == 0:
        return "Fizz"
    elif total % 5 == 0:
        return "Buzz"
    else:
        return str(total)

def process_input(user_input: str) -> str:
    
    cleaned = user_input.lower().replace(" ", "")
    if cleaned == "fizzbuzz":
        return "Fizz Buzz"
    elif cleaned == "fizz":
        return "Fizz"
    elif cleaned == "buzz":
        return "Buzz"
    else:
        return cleaned  

def fizzbuzz_alternate_game(rounds=30, min_val=1, max_val=20):
    print("🎮 Welcome to Alternate FizzBuzz Game! 🎮")
    print("Rules:")
    print("1. Turn 1: check the first number.")
    print("2. Turn 2+: sum previous + current number.")
    print("3. Answer: 'Fizz', 'Buzz', 'Fizz Buzz' or number.")
    print("4. One mistake ends the game.\n")

    score = 0
    prev_num = None

    for turn in range(1, rounds + 1):
        current_num = random.randint(min_val, max_val)
        correct_answer = fizzbuzz_check(current_num, prev_num)

        print(f"Round {turn}: Number chosen = {current_num}")
        user_guess = input("Your answer: ").strip()
        user_guess = process_input(user_guess)

        if user_guess.lower() == correct_answer.lower():
            score += 1
            print(f" Correct! ({correct_answer}) | Score: {score}\n")
            prev_num = current_num
        else:
            print(f" Wrong! Correct answer was: {correct_answer}")
            print(f"Game Over! Final Score: {score}")
            return

    print(f"🎉 Congratulations! You cleared all {rounds} rounds! Final Score: {score}")


fizzbuzz_alternate_game(10)
